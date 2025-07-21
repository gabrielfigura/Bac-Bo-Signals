import requests
from bs4 import BeautifulSoup

def get_last_rounds(n=30):
    url = "https://casinoscores.com/es/bac-bo/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = []
    table = soup.find("div", class_="history")
    
    if table:
        items = table.find_all("div", class_="item")[:n]
        for item in items:
            outcome = item.get("class")[1]  # 'banker', 'player' ou 'tie'
            if outcome == "banker":
                results.append("B")
            elif outcome == "player":
                results.append("P")
            elif outcome == "tie":
                results.append("T")
    return results[::-1]  # mais antigo → mais novo
