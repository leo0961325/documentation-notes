# jupyter notebook allow remote access 允許遠端登入

- 2019/07/03
- [Config file and command line options](https://jupyter-notebook.readthedocs.io/en/latest/config.html)
- [Why I can't access remote Jupyter Notebook server?](https://stackoverflow.com/questions/42848130/why-i-cant-access-remote-jupyter-notebook-server)


```bash
$ jupyter notebook --generate-config
Writing default config to: /home/tony/.jupyter/jupyter_notebook_config.py

$ vim /home/tony/.jupyter/jupyter_notebook_config.py
# 700 多行的設定檔...
# 尋找關鍵字「allow_origin 」
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
c.NotebookApp.allow_origin = '*'    # 改~
c.NotebookApp.ip = '0.0.0.0'        # 改~
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# 但似乎不行...= =

### 直接這樣做更快 XD
$ jupyter notebook --ip 0.0.0.0 --port 8888
# Copy-Paste token 即可
```

# Jupyter Notebook for JavaScript

- 2018/08/21
- [ijavascript](https://github.com/n-riesco/ijavascript)


## 環境

- Windows 10 專業版
- Python 3.6.0 :: Anaconda 4.3.0 (64-bit)

```sh
### 建立虛擬環境
$ python -m venv jbook

# 安裝阿~~~
(jbook)$ conda install nodejs
(jbook)$ npm install -g ijavascript
(jbook)$ ijsinstall

(jbook)$ jupyter notebook
# 安心使用~
```
