# Scrapy
## 項目說明：
爬取目標網站(星座運勢網站)上的資料，將12星座的當日運勢資訊儲存至資料庫，並同時輸出json檔。  

## 環境設置：
Python 3.7.5  
Scrapy 2.0.1  

## 程式解說：
1.items.py：定義day, constellation, overall, love, carrer, money等六個欄位，進行資料處理。  
2.pipelines.py：將處理完的資料分為上述六個欄位儲存到資料庫(sqlite3)中。  
3.crawler.py：解析資料並將資料儲存為上述的結構。    

## 使用程式：
1.下載檔案後，進入astro目錄  
2.執行以下指令 $ scrapy crawl astro  
3.即可將爬取到的網頁資料儲存至資料庫  
4.同時將爬取到的資料輸出為astro.json  


