thonfrom datetime import datetime

def parse_instagram_date(timestamp):
    if timestamp is None:
        return None
    return datetime.utcfromtimestamp(timestamp).isoformat() + "Z"