import requests
from bs4 import BeautifulSoup

def search_ptt(board, keyword, pages=3):
    base_url = f'https://www.ptt.cc/bbs/{board}/index.html'
    session = requests.Session()
    session.cookies.set('over18', '1')  # 通過年齡驗證

    results = []
    for _ in range(pages):
        res = session.get(base_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        articles = soup.select('div.r-ent')
        for article in articles:
            title_tag = article.select_one('div.title a')
            if title_tag and keyword in title_tag.text:
                link = 'https://www.ptt.cc' + title_tag['href']
                results.append({'title': title_tag.text.strip(), 'url': link})
        # 找上一頁
        prev_link = soup.select_one('div.btn-group-paging a.btn.wide:nth-child(2)')
        if prev_link:
            base_url = 'https://www.ptt.cc' + prev_link['href']
        else:
            break
    return results

if __name__ == '__main__':
    board = input('請輸入看板名稱: ')
    keyword = input('請輸入關鍵字: ')
    results = search_ptt(board, keyword)
    for r in results:
        print(r['title'], r['url'])