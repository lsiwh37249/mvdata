from mvdata.ml import save_json,req,save_movies,save_moviedetails,get_movieCd

#save_json : data, file_path
    
#req : url

#save_movices : year
def test_save_movies():
    r = save_movies(year=2015, sleep_time=0.1)
    r = save_movies(year=2016, sleep_time=0.1)
    r = save_movies(year=2017, sleep_time=0.1)
    r = save_movies(year=2018, sleep_time=0.1)
    r = save_movies(year=2019, sleep_time=0.1)
    r = save_movies(year=2020, sleep_time=0.1)
    r = save_movies(year=2021, sleep_time=0.1)
    assert r

def test_save_moviedetails():
    save_moviedetails(2015)
    

