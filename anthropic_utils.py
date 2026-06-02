
import os, json
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def summarize(article):
    prompt = f"""
Article title: {article['title']}
Abstract: {article['abstract']}

Return JSON:
{{
 "relevance":"",
 "methodology":"",
 "findings":["","",""],
 "themes":["",""]
}}
"""
    msg = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=300,
        messages=[{"role":"user","content":prompt}]
    )
    text = msg.content[0].text
    try:
        return json.loads(text)
    except Exception:
        return {
            "relevance":"Potentially relevant",
            "methodology":"Unknown",
            "findings":[],
            "themes":[]
        }
