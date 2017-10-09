# django 1.11.4
- 2017/9/27


---
## 基本設定

### settings.py

``` python
# 設定時間
TIME_ZONE = 'Asia/Taipei'
```

``` python
# 設定資料庫
## SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 資料庫會放在 'BASE_DIR'裡面
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

``` python
# 設定資料庫
## MySQL, Oracle, or PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.<DB>', # ex: MySQL 

        # 載入組態檔案
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },

        'NAME': '<dbName>',        
        'USER': '<user>',       
        'PASSWORD': '<passWord>',  
        'HOST': '<host>', 
        'PORT': '<port>', 
    }
}
```
```python
# 完成上述設定後, 進入python, 執行看看, 沒報錯表示資料庫設定OK
from django.db import connection
cursor = connection.cursor()
```

### 建立使用者
``` sh
$ python manage.py createsuperuser
```

###
```
$ 
```

---

## 模組內的職責

## 指令

``` sh
# Windows底下首次執行時
$ pip install mysqlclient

# 檢查串接資料庫後的結果(會印出一堆東西)
$ python manage.py inspectdb

# 將資料庫schema寫入「blogapp」裡面的 Model.py
$ python manage.py inspectdb > blogapp/models.py
```