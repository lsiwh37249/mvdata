from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("Dynamic Schema Example").getOrCreate()

# pyspark 에서 multiline(배열) 구조 데이터 읽기
jdf = spark.read.option("multiline","true").json('/home/kim1/data/movies/year=2015/data.json')

#jdf.show()

## companys, directors 값이 다중으로 들어가 있는 경우 찾기 위해 count 컬럼 추가
from pyspark.sql.functions import explode, col, size, explode_outer

ccdf = jdf.withColumn("company_count", size("companys")).withColumn("directors_count", size("directors"))
ccdf.show()

# companys, directors 값이 다중으로 들어가 있는 경우 찾기
fdf = ccdf.filter(ccdf.company_count > 1).filter(ccdf.directors_count > 1)

# 2015년 movieCd 20141663 인 영화는 company_count = 2, directors_count = 3 임

fdf.collect()[0]['movieCd']
fdf.collect()[0]['companys'][0]['companyCd']
fdf.collect()[0]['companys'][0]['companyNm']

# 펼치기
from pyspark.sql.functions import explode, col, size
edf = fdf.withColumn("company", explode_outer("companys"))
edf.show()

# 또 펼치기
eedf = edf.withColumn("director", explode_outer("directors"))
eedf.show()
