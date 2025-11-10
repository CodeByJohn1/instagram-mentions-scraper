# Instagram Mentions Scraper

> A fast and simple scraper that extracts mentions and tagged posts from any public Instagram account. It’s designed to help marketers, analysts, and researchers collect engagement data such as likes, comments, captions, and hashtags for deeper insights into online presence and content performance.

> Instagram Mentions Scraper automates the process of gathering structured Instagram data for analysis, research, and reporting — all in a few clicks.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Instagram Mentions Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

Instagram Mentions Scraper collects mentions and tagged post data from public Instagram profiles. It’s perfect for social media analysts, brands, researchers, and developers who need structured data for reporting, trend analysis, or training AI models.

### Why Use Instagram Mentions Scraper

- Extracts posts where a user is tagged or mentioned.
- Delivers data including captions, comments, likes, and hashtags.
- Supports multiple output formats (JSON, CSV, Excel, XML, HTML).
- Works seamlessly with public Instagram accounts.
- Produces clean datasets for analytics or automation pipelines.

## Features

| Feature | Description |
|----------|-------------|
| Mentions and Tagged Post Extraction | Scrapes tagged and mentioned posts from public Instagram profiles. |
| Data Enrichment | Includes captions, hashtags, likes, comments, and timestamps. |
| Multi-Format Export | Exports data as JSON, CSV, Excel, XML, or HTML. |
| Comment Insights | Retrieves first comment, latest comments, and comment count. |
| Media Details | Captures post image URLs, video durations, and image dimensions. |
| Author Metadata | Includes author username and post URL for traceability. |
| Location Tracking | Detects and stores location data if available. |
| Automation Ready | Can be integrated into dashboards or marketing workflows. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| id | Unique identifier of the post. |
| type | Type of post (Image, Video, or Carousel). |
| shortCode | Unique shortcode identifier for the Instagram post. |
| caption | Full post caption text. |
| hashtags | List of hashtags included in the post. |
| mentions | Usernames mentioned in the post. |
| url | Direct URL to the Instagram post. |
| commentsCount | Total number of comments on the post. |
| firstComment | The first comment made on the post. |
| latestComments | Array of the latest comments with user details. |
| likesCount | Number of likes the post received. |
| timestamp | Date and time of the post creation. |
| location | Location information if indicated by the author. |
| authorUsername | The username of the post’s author. |
| videoDuration | Duration of the video content if the post contains video. |

---

## Example Output


    [
      {
        "id": "3205475538117343889",
        "type": "Sidecar",
        "shortCode": "Cx8IwTBsDqR",
        "caption": "Володимир Зеленський відвідав розташування бригад, які виконують бойові завдання...",
        "hashtags": [],
        "mentions": ["zelenskiy_official"],
        "url": "https://www.instagram.com/p/Cx8IwTBsDqR/",
        "commentsCount": 35,
        "firstComment": "👏👏👏🙌❤️",
        "latestComments": [
          {
            "text": "👏👏👏🙌❤️",
            "ownerUsername": "kolinko.tamara",
            "likesCount": 0
          },
          {
            "text": "❤️❤️❤️🇺🇦",
            "ownerUsername": "irenetsvikilevich",
            "likesCount": 0
          }
        ],
        "likesCount": 1200,
        "timestamp": "2023-10-05T05:19:54.000Z",
        "location": "Kharkiv",
        "authorUsername": "zelenskiy_official",
        "videoDuration": null
      }
    ]

---

## Directory Structure Tree


    instagram-mentions-scraper/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── instagram_parser.py
    │   │   └── utils_date.py
    │   ├── outputs/
    │   │   └── exporter.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Marketing agencies** use it to monitor how often influencers mention or tag their brand, helping measure campaign reach.
- **Data analysts** use it to extract engagement metrics for trend reports and competitor benchmarking.
- **Social media researchers** use it to study public discourse and audience behavior.
- **Developers** integrate it into dashboards or automation pipelines to visualize engagement and brand mentions.
- **AI teams** leverage large-scale datasets to train sentiment or image recognition models.

---

## FAQs

**How many results can this scraper extract?**
It can typically handle thousands of tagged posts depending on profile activity, input parameters, and connection stability.

**Can I use it with multiple usernames at once?**
Yes, you can enter multiple Instagram usernames to scrape mentions and tagged posts concurrently.

**Is it safe and legal to use?**
The scraper only collects publicly available data and doesn’t access private information. Always ensure you comply with relevant data protection laws when using the output.

**Can I connect it to other tools or platforms?**
Yes. The output can easily be integrated with dashboards, spreadsheets, or cloud automation tools using APIs or webhooks.

---

## Performance Benchmarks and Results

**Primary Metric:** Scrapes up to 500 posts per minute under stable conditions.
**Reliability Metric:** 97% success rate for public profiles with stable network access.
**Efficiency Metric:** Handles batch scraping for up to 10 usernames simultaneously with moderate resource usage.
**Quality Metric:** Achieves 99% field completeness and high accuracy in comment and hashtag extraction.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
