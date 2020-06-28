import requests
from bs4 import BeautifulSoup as bs
import pandas

def getWebResponese():
    url = 'https://maoyan.com/films?showType=3'
    cookie = 'uuid_n_v=v1; uuid=071313D0B8DF11EAB7FDDF490BC946C045F5B84B52D34D1E974F4E7AFF0695A0; _csrf=94c2bc785bcb8f5ec6834122d3a84e85b8b72947b6357c2c4a2c5160494fe54b; _lxsdk_cuid=172f88ca405c8-07d59cdfdf2484-31617402-fa000-172f88ca405c8; _lxsdk=071313D0B8DF11EAB7FDDF490BC946C045F5B84B52D34D1E974F4E7AFF0695A0; mojo-uuid=6a5a062a2f00e5b17c251ecb9920113f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593307865,1593312148; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593349117; __mta=88972836.1593307866208.1593312149288.1593349117023.3; _lxsdk_s=172fb2cb1ce-af8-09a-2db%7C%7C1'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    response = requests.get(url=url, headers={"User-Agent": user_agent,
                                              "Cookie": cookie})
    if response.status_code == 200 :
        return response

def getMovies(response):
    # 处理html
    htmlText = bs(response.text, 'html.parser')
    print(htmlText);
    moviews = []
    for tags in htmlText.find_all('div', attrs={'class', 'movie-hover-info'})[0:10]:
        # 获取电影名称
        name = tags.find('span', {'class', 'name'}).get_text(strip=True)
        for i, attrs in enumerate(tags.find_all('div', attrs={'class', 'movie-hover-title'})):
            if i == 1:
                # 类型
                type = attrs.contents[-1].strip()
            if i == 3:
                # 时间
                time = attrs.contents[-1].strip()
        moviews += [(name, type, time)]
    return moviews



pandas.DataFrame(getMovies(getWebResponese())).to_csv('./movie.csv', encoding='utf8', index=False, header=False)