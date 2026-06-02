
KEYWORDS = {
    "manosphere": 20, "incel": 20, "mgtow": 20, "redpill": 20,
    "masculinisme": 20, "antiféminisme": 20, "アンチフェミ": 20, "反フェミ": 20,
    "男性権利": 20, "マノスフィア": 20,
    "masculinity": 15, "masculinité": 15, "男性性": 15,
    "misogyny": 15, "ミソジニー": 15, "バックラッシュ": 15,
    "platform": 5, "algorithm": 5, "digital": 5, "online": 5,
    "affect": 5, "emotion": 5, "japan": 10, "japanese": 10, "日本": 10,
}

def score_article(title, abstract):
    text = f"{title} {abstract}".lower()
    score = 0
    for k, v in KEYWORDS.items():
        if k.lower() in text:
            score += v
    return score
