from mvdata.ml import save_json,req,save_movies

#save_json : data, file_path
    
#req : url

#save_movices : year
def test_save_movies():
    r = save_movies(year=2015, sleep_time=0.1)
    assert r

