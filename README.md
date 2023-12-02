# Final Project Data Tidy

## 12/02 公告

Weather資料夾裡有兩個不同的檔案，叫做 Weatherdata.csv跟fixeddata.csv

Weatherdata.csv紀錄的是當日累計雨量，fixeddata.csv紀錄的是過去一小時的小時雨量。

## 11/30 UPD 發布預測資料

型態為： 預報時間 溫度 雨量 相對濕度

每六小時一筆，從11/30 06:00 - 12/08 18:00

存在 Predict weather 資料夾

## 11/29 UPD 拿到觀測坪資料了

整理完放在Weather資料夾裡，叫做 Weatherdata.csv

headers:

ID, month, day, accumulated minutes, temperature, rainfall, relative humidity

不出意外的話，今後的天氣資料會變成日更

## Tidied Status

With every stand have its own and only csv, which include every day and every nonempty minute. A new folder will be created everyday.

## CSV type

### Bike: MMDDversion/stationID.csv
ID, month, day, weekday, accumulated minutes (0-1439), capacity, bike amount

### Weather: weather_data.csv
month, day, accumulated minutes, temperature, rainfall, relative humidity

## 有用的廢話

將來可能可以試試看把其他資料也放上來？

## 沒用的廢話

好想把gitignore也ignore掉
國慶連假連Ubike統計系統也一起放假了嗎？
