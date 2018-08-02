# Django v1.11
- 2018/07

```sh
$ python -m django --version
1.11.4

$ django-admin startproject <Project Name>

$ python manage.py startapp <App Name>  # 建立 App
```


``` sh
# Windows底下首次執行時 (若安裝 Anaconda 才不會有相依套件的問題)
$ pip install mysqlclient

# CentOS7
$ sudo yum install -y python-devel
$ pip install mysqlclient

# Ubuntu16.04
$ sudo apt -y install libmysqlclient-dev
$ pip install mysqlclient
```

```sh
$ python manage.py runserver
$ python manage.py runserver 0:8000     # 開放對外

$ python manage.py shell
```

# Migrate (其實我不是很懂)

```sh
$ python manage.py migrate


$ 
```

# Models

```sh
$ python manage.py inspectdb

# 將資料庫schema寫入「blogapp」裡面的 Model.py
$ python manage.py inspectdb > m.py
```

# Superuser

```sh
$ python manage.py createsuperuser
```