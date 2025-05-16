
import wget 

url1 = "https://data.epa.gov/efservice/downloads/tri/mv_tri_basic_download/"


for year in range(1989,2024):
    url = url1 + str(year) + "_PR/csv"
    print(url)
    wget.download(url)
