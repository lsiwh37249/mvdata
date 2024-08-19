from mvstar.mc import save_movie_company

def test_save_company():
    rst=save_movie_company(sleep_time=0.1)
    assert rst
