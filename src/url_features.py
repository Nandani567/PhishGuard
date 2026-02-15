import re
from urllib.parse import urlparse

def url_length(url: str) -> int:
    return len(url)

def count_dots(url: str) -> int:
    return url.count(".")

def has_ip_address(url: str) -> int:
    pattern = r"(http[s]?://)?(\d{1,3}\.){3}\d{1,3}"
    return 1 if re.search(pattern, url) else 0

def has_https(url: str) -> int:
    return 1 if url.startswith("https") else 0

def extract_features(url: str) -> dict:
    return {
        "": url_length(url),
        "dot_count": count_dots(url),
        "has_ip": has_ip_address(url),
        "has_https": has_https(url),
    }
