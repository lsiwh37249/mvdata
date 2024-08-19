import requests as reqs
import os
import json
import time
from tqdm import tqdm

API_KEY=os.getenv("MOVIE_API_KEY")

def save_json(data, file_path):
    # file path mkdir
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


    return True


def req(url):
    resp = reqs.get(url)
    json = resp.json()
    return json


def save_movie_company(per_page=10, sleep_time=1):
    home_path = os.path.expanduser("~")
    file_path = f"{home_path}/data/movies/movieCompany/data.json"
    
    baseUrl=f"https://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json?key={API_KEY}"

    # 위 경로가 있으면 API 호출을 멈추고 프로그램 종료
    print("영화사 불러오기를 시작합니다.")
    if os.path.exists(file_path):
        print(f"[Warning] 데이터가 이미 존재합니다: [File Path] {file_path}")
        print("영화사 불러오기를 종료합니다.")
        return True

    # total cnt get, total_pages calc

    json=req(baseUrl+"&curPage=1")
    totCnt=json["companyListResult"]["totCnt"]
    total_pages = (totCnt // per_page) +1
    # loop in total pages, call api
    total_data=[]

    for page in tqdm(range(1, total_pages+1)):
        json=req(baseUrl+f"&curPage={page}")
        data=json["companyListResult"]["companyList"]
        total_data.extend(data)
        time.sleep(sleep_time)

    save_json(total_data, file_path)
    print("영화사 불러오기를 종료합니다.")
    return True
