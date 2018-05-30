# Python 的問題 && 解法

## - Windows 10 找不到 sqlite3
- [解法](https://stackoverflow.com/questions/4578231/error-while-accessing-sqlite3-shell-from-django-application/4578325)
- 2018/04/11



## - Windows 10 egg_info 這東西
- [當看到 egg_info 這東西](https://github.com/thisbejim/Pyrebase/issues/179)
- 2018/05/30

```powershell
> systeminfo 
作業系統名稱:         Microsoft Windows 10 專業版
作業系統版本:         10.0.17134 N/A 組建 17134

> python --version
Python 3.6.2

> pip install -r requirements.txt
...(略)...
Collecting uWSGI==2.0.15 (from -r requirements.txt (line 20))
  Using cached https://files.pythonhosted.org/packages/bb/0a/45e5a...68a1/uwsgi-2.0.15.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "C:\Users\...\pip-install-upntrhyy\uWSGI\setup.py", line 3, in <module>
        import uwsgiconfig as uc
      File "C:\Users\...\pip-install-upntrhyy\uWSGI\uwsgiconfig.py", line 8, in <module>
        uwsgi_os = os.uname()[0]
    AttributeError: module 'os' has no attribute 'uname'

    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in C:\Users\...\pip-install-upntrhyy\uWSGI\
```

搞屁阿!! `Windows 10 沒辦法用 uwsgi啦!!`