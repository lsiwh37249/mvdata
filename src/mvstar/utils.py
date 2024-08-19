import json

def extractCol(colNm="movieCd",year=2015):
    with open(f"/home/kim1/data/movies/year={year}/data.json") as f:
        data=json.load(f)

    return list(map(lambda x:x[colNm],data))
