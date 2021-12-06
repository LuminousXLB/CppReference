import httpx
from bs4 import BeautifulSoup

GIST_URL = "https://gist.github.com/LuminousXLB/d43f80fba9d765544787bc6c4c6e684f"

resp = httpx.get(GIST_URL)

soup = BeautifulSoup(resp.content, "html.parser")
boxes = soup.find_all("div", {"class": "file"})

files = [
    (
        box.find("strong", {"class": "gist-blob-name"}).text.strip(),
        "#".join([GIST_URL, box.get("id")]),
    )
    for box in boxes
]

with open("SNIPPETS.md", "w") as f:
    f.write("# List of Code Snippets")
    for name, url in files:
        f.write(f"- [{name}]({url})\n")
