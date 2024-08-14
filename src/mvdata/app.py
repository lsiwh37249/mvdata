from typing import Union

from fastapi import FastAPI, HTTPException
import pandas as pd
import os
import requests

app = FastAPI()

def ping():
    print("pong")

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(movie_cd, url_param = {}):
    url = gen_url(movie_cd, url_param)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    print(data)
    return code, data

def gen_url(movie_cd, url_param = {}):
    #base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"

    key = get_key()
    url = f"{base_url}?key={key}&movieCd={movie_cd}"
    for k, v in url_param.items():
        url = url + f"&{k}={v}"
    return url

#df = pd.read_parquet('/home/kim1/code/ffapi/data')

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sample")
def sample_data():
    df = pd.read_parquet('/home/kim1/code/ffapi/data')
    sample_df = df.sample(n=5)
    r = sample_df.to_dict(orient='records')
    return r


@app.get("/movie/{movie_cd}")
def movie_meta(movie_cd: str):
    df = pd.read_parquet('/home/kim1/code/ffapi/data')

    # df 에서 movieCd == movie_cd row 를 조회 df[['a'] === b] ...
    meta_df = df[df['movieCd'] == movie_cd]

    if meta_df.empty:
        raise HTTPException(status_code=404, detail="영화를 찾을 수 없습니다")

    # 조회된 데이터를 .to_dict() 로 만들어 아래에서 return
    r = meta_df.iloc[0].to_dict()

    if r['repNationCd'] is None:
        _,rr = req(movie_cd)
        print(rr)
        new_rr=rr["movieInfoResult"]["movieInfo"]

        nation = new_rr["nations"][0]

        if nation['nationNm'] != '한국':
            r['repNationCd'] = 'F'
        else:
            r['repNationCd'] = 'N'

    return r

