
from sources import fetch_rss, fetch_openalex
from scoring import score_article
from anthropic_utils import summarize
from notion_utils import create_page

papers = fetch_rss() + fetch_openalex()

for p in papers:
    p["score"] = score_article(p["title"], p["abstract"])

top5 = sorted(papers, key=lambda x: x["score"], reverse=True)[:5]

for article in top5:
    ai = summarize(article)
    create_page(article, ai)

print(f"Added {len(top5)} articles.")
