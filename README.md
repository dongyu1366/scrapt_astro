# scrapy_astro
##程式解說：
items.py：定義了day, constellation, overall, love, carrer, money等六個欄位，來進行資料處理。  
pipelines.py：將處理完的資料分為上述六個欄位儲存到資料庫(sqlite3)中。  
crawler.py：定義了如何去parse資料並將資料存為上述的格式。  

##使用此程式:



