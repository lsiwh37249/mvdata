from mvdata.mj_file import data2json
import json 

#save_json : data, file_path
    
#req : url

#save_movices : year
def test_data2parq():
    #r = data2parq(year=2015)
    print("==============영화사목록==============")
    try:
        r = data2json(year=2015)
        assert r
    except json.JSONDecodeError:
        print('알 수 없는 JsonDecodeError')
    except KeyError:
        print("이상한 key error")
    print("================================")
    

