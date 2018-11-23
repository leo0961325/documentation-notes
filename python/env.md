[Anaconda多环境多版本python配置指导](https://www.jianshu.com/p/d2e15200ee9b)

進入虛擬環境 (安裝完anaconda後)
```sh
# 建立環境變數
conda create -n <EnvName>
python -m venv <EnvName>

# 列出環境變數
conda env list  # Linux

# 啟用環境變數
source activate <EnvName>
<EnvName>\Scripts\activate

# 離開環境變數
source deactivate <EnvName>
<EnvName>\Scripts\deactivate

# 移除環境變數
conda env remove -n <EnvName>


# 安裝虛擬環境下的 pip
conda install -n <EnvName> pip  # 要裝一陣子...
which pip
pip freeze  # 應為空的
```




# Ubuntu - py3 的 virtualenv 及 virtualenvwrapper

```sh
### root
apt-get install -y python3-pip python3-dev		# 抓 python3用的 pip
pip3 install --upgrade pip						# 升級 pip3
pip3 install virtualenv virtualenvwrapper		# 用 pip3 安裝 虛擬環境
# 請確定安裝後, 最後面有出現「Successfully installed ...」的字樣

### User
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
mkvirtualenv -p /usr/bin/python3 <EnvName>
mkdir <EnvName>
cd <EnvName>
setvirtualenvproject .
```



# pip
```sh
$ pip freeze

$ pip freeze -l     # 只顯示目前環境安裝的套件

$ pip freeze > requirement.txt

$ pip install -r requirement.txt
```

