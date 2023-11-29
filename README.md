# Final Project Data Tidy

## 11/29 拿到觀測坪資料了但我正在想辦法讀懂他zzz

## Tidied Status

With every stand have its own and only csv, which include every day and every nonempty minute. A new folder will be created everyday.

## CSV type

### Bike: MMDDversion/stationID.csv
month, day, weekday, accumulated minutes (0-1439), capacity, bike amount

### Weather: weather_data.csv
month, day, accumulated minutes, temperature, rainfall, relative humidity

## 有用的廢話

將來可能可以試試看把其他資料也放上來？

## 沒用的廢話

好想把gitignore也ignore掉
國慶連假連Ubike統計系統也一起放假了嗎？

## 11/29 Weather UPD

新增填充資料，以對齊分鐘資料，採$[i-5, i+5)$填充為$i$
給予 ID = Epoch timestamp 方便資料對齊
放在 Weather 資料夾
headers:
ID (Epoch timestamp), month, day, accumulated minutes, temperature, rainfall, relative humidity
