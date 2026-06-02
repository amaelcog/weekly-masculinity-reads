
import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

def create_page(article, ai):
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Title": {"title":[{"text":{"content":article["title"][:200]}}]},
            "Authors": {"rich_text":[{"text":{"content":article.get("authors","")[:2000]}}]},
            "Source": {"rich_text":[{"text":{"content":article.get("source","")[:2000]}}]},
            "URL": {"url": article.get("url","")}
        },
        children=[
            {
                "object":"block",
                "type":"paragraph",
                "paragraph":{"rich_text":[{"type":"text","text":{"content":
f"Relevance: {ai.get('relevance','')}\n\nMethodology: {ai.get('methodology','')}\n\nFindings: {', '.join(ai.get('findings',[]))}"
                }}]}
            }
        ]
    )
