
import requests, feedparser

RSS_FEEDS = [
    "https://www.tandfonline.com/feed/rss/rnor20",
    "https://journals.sagepub.com/action/showFeed?type=etoc&feed=rss&jc=jmma",
    "https://journals.sagepub.com/action/showFeed?type=etoc&feed=rss&jc=gasa",
]

def fetch_rss():
    papers = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for e in feed.entries:
            papers.append({
                "title": getattr(e, "title", ""),
                "abstract": getattr(e, "summary", ""),
                "url": getattr(e, "link", ""),
                "source": feed_url,
                "authors": "",
                "journal": ""
            })
    return papers

def fetch_openalex():
    url = "https://api.openalex.org/works?filter=from_publication_date:2026-01-01&per-page=50"
    data = requests.get(url, timeout=30).json()
    papers = []
    for r in data.get("results", []):
        papers.append({
            "title": r.get("title", ""),
            "abstract": "",
            "url": r.get("id", ""),
            "source": "OpenAlex",
            "authors": ", ".join(a["author"]["display_name"] for a in r.get("authorships", [])[:5]),
            "journal": ""
        })
    return papers
