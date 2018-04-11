# django 1.11.4
- 2017/9/27


``` sh
# Windows底下首次執行時
$ pip install mysqlclient

# 檢查串接資料庫後的結果(會印出一堆東西)
$ python manage.py inspectdb

# 將資料庫schema寫入「blogapp」裡面的 Model.py
$ python manage.py inspectdb > blogapp/models.py
```