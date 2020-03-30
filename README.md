# scrapy_astro
## 程式解說：
1.items.py：定義了day, constellation, overall, love, carrer, money等六個欄位，來進行資料處理。  
2.pipelines.py：將處理完的資料分為上述六個欄位儲存到資料庫(sqlite3)中。  
3.crawler.py：定義了如何去parse資料並將資料存為上述的格式。  

## 使用此程式：
1.下載檔案後，進入astro目錄  
2.執行以下指令 $ scrapy crawl astro  
3.即可將爬取到的網頁資料儲存至資料庫  
4.同時生成astro.json檔案  


