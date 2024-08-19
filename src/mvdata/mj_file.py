import requests 
import os
import json
import time
from tqdm import tqdm

API_KEY = os.getenv('MOVIE_API_KEY')


#API 요청하기
def req(url):
    req = requests.get(url)
    print(req)
    j = req.json()
    return j

def get_movieCd(file_path, data=' '):
    movieCds =[ ]
    with open(file_path,"w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return movieCds 

#json 값 저장하기
# 이미 저장된 파일의 경로를 불러온 뒤에 json.dump를 이용한다.
# with open 하려면 file_path와 모드, encoding을 사용
def save_json(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
         json.dump(data, f, indent=4, ensure_ascii=False) 

#여러 페이지를 요청하기 위해서 for문을 돌려야 한다.
def data2json(year=2015):
    file_path =f"/home/kim1/data/movies/year={year}/data.json"
    
    url_base = f"https://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}"
    
    #url에 요청하기 
    all_data = [ ]
    for page in tqdm(range(1,11)):
        time.sleep(1)
        url_addPage = url_base + f"&curPage={page}"
        r = req(url_addPage)
        print(r)
        d = r['movieListResult']['movieList']
        print(d)
        all_data.extend(d)

    save_json(all_data, file_path)
    return True



