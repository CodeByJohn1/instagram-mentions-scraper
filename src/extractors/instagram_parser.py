thonimport aiohttp
import asyncio
from bs4 import BeautifulSoup
from .utils_date import parse_instagram_date
import logging

class InstagramMentionsScraper:
    BASE_URL = "https://www.instagram.com"

    async def fetch_page(self, session, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            return await response.text()

    async def scrape_mentions(self, username):
        url = f"{self.BASE_URL}/{username}/"
        async with aiohttp.ClientSession() as session:
            html = await self.fetch_page(session, url)
            return self.parse_posts(html)

    def parse_posts(self, html):
        soup = BeautifulSoup(html, "html.parser")
        scripts = soup.find_all("script", type="text/javascript")
        results = []

        for script in scripts:
            if "window._sharedData" in script.text:
                try:
                    json_text = script.string.strip().replace("window._sharedData = ", "")[:-1]
                    import json
                    data = json.loads(json_text)
                    edges = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
                    for edge in edges:
                        node = edge["node"]
                        results.append({
                            "id": node.get("id"),
                            "type": node.get("__typename"),
                            "shortCode": node.get("shortcode"),
                            "caption": node.get("edge_media_to_caption", {}).get("edges", [{}])[0].get("node", {}).get("text", ""),
                            "hashtags": [tag.strip("#") for tag in node.get("edge_media_to_caption", {}).get("edges", [{}])[0].get("node", {}).get("text", "").split() if tag.startswith("#")],
                            "mentions": [tag.strip("@") for tag in node.get("edge_media_to_caption", {}).get("edges", [{}])[0].get("node", {}).get("text", "").split() if tag.startswith("@")],
                            "url": f"https://www.instagram.com/p/{node.get('shortcode')}/",
                            "commentsCount": node.get("edge_media_to_comment", {}).get("count"),
                            "firstComment": None,
                            "latestComments": [],
                            "likesCount": node.get("edge_liked_by", {}).get("count"),
                            "timestamp": parse_instagram_date(node.get("taken_at_timestamp")),
                            "location": node.get("location", {}).get("name") if node.get("location") else None,
                            "authorUsername": node.get("owner", {}).get("username"),
                            "videoDuration": node.get("video_duration") if node.get("is_video") else None
                        })
                except Exception as e:
                    logging.error(f"Failed to parse posts: {str(e)}")
        return results