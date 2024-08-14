import requests
import os
import json
import time
from tqdm import tqdm

API_KEY = os.getenv('MOVIE_API_KEY')

def save_json(data, file_path):
    # 파일저장 경로 MKDIR
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def req(url):
    r = requests.get(url)
    j = r.json()
    return j

def save_movies(year=2015, per_page=10, sleep_time=1):
    file_path = f'/home/kim1/data/movies/year={year}/data.json'
    
    # 위 경로가 있으면 API 호출을 멈추고 프로그램 종료
    if os.path.exists(file_path):
        print("이미 해당 정보가 존재합니다")
        return True

    # totCnt 갖여오고 total_pages 계산
    url_base = f"https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}&openStartDt={year}&openEndDt={year}"
    r = req(url_base + f"&curPage=1")
    tot_cnt = r['movieListResult']['totCnt']
    total_pages = (tot_cnt // per_page) + 1

    # total_pages 만큼 Loop 돌면서 API 호출
    all_data = []
    for page in tqdm(range(1, total_pages + 1)):
        time.sleep(sleep_time)
        
        url_addPage = url_base + f"&curPage={page}"
        r = req(url_addPage)
        d = r['movieListResult']['movieList']
        all_data.extend(d)

    save_json(all_data, file_path)
    return True

