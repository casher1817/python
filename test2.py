import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=10):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "q": query,
        "num": num_results
    }
    url = "https://www.google.com/search"
    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for g in soup.find_all('div', class_='tF2Cxc'):
        title = g.find('h3')
        link = g.find('a', href=True)
        if title and link:
            results.append({
                'title': title.text,
                'link': link['href']
            })
    return results

if __name__ == "__main__":
    keyword = "python 爬蟲"
    search_results = google_search(keyword)
    for idx, result in enumerate(search_results, 1):
        print(f"{idx}. {result['title']}\n{result['link']}\n")