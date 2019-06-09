


```bash
### 一開始, 使用 global pip 安裝 pipenv 於特定 project dir
proj$ pip install pipenv

### 安裝套件
proj$ pipenv install Sanic
Creating a virtualenv for this project…
Pipfile: D:\tmp\ssanic\Pipfile
Using c:\users\tony\appdata\local\programs\python\python37\python.exe (3.7.3) to create virtualenv…
[====] Creating virtual environment...Already using interpreter c:\users\tony\appdata\local\programs\python\python37\python.exe
Using base prefix 'c:\\users\\tony\\appdata\\local\\programs\\python\\python37'
New python executable in C:\Users\tony\.virtualenvs\ssanic-qZ1hHV8u\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

Successfully created virtual environment!
Virtualenv location: C:\Users\tony\.virtualenvs\ssanic-qZ1hHV8u
Creating a Pipfile for this project…
Installing Sanic…
Adding Sanic to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (acb8a0)!
Installing dependencies from Pipfile.lock (acb8a0)…
  ================================ 5/5 - 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
# 結束後, proj 內會出現:
# Pipfile : 紀錄安裝了那些套件
# Pipfile.lock

###
proj$
```