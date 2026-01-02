import json
from dns_parser import parse_dns
from eldorado_parser import parse_eldorado
from mvideo_parser import parse_mvideo

data = {
    "dns": parse_dns(),
    "eldorado": parse_eldorado(),
    "mvideo": parse_mvideo()
}

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)