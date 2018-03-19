# EPEL
cd
wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo rpm -ivh epel-release-latest-7.noarch.rpm

# Chrome
sudo touch /etc/yum.repos.d/google-chrome.repo
sudo echo '[google-chrome]' >> /etc/yum.repos.d/google-chrome.repo
sudo echo 'name=google-chrome' >> /etc/yum.repos.d/google-chrome.repo
sudo echo 'baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64' >> /etc/yum.repos.d/google-chrome.repo
sudo echo 'enabled=1' >> /etc/yum.repos.d/google-chrome.repo
sudo echo 'gpgcheck=1' >> /etc/yum.repos.d/google-chrome.repo
sudo echo 'gpgkey=https://dl.google.com/linux/linux_signing_key.pub' >> /etc/yum.repos.d/google-chrome.repo
sudo yum -y install google-chrome-stable

# Docker
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce
sudo groupadd docker
sudo usermod -aG docker $USERNAME
sudo systemctl start docker
sudo systemctl enable docker

# VSCode
cd
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo yum -y install code

# Git
sudo yum install autoconf libcurl-devel expat-devel gcc gettext-devel kernel-headers openssl-devel perl-devel zlib-devel -y
wget https://github.com/git/git/archive/v2.14.3.tar.gz
tar zxf git-2.14.3.tar.gz
cd git-2.14.3/
make clean
make configure
./configure --prefix=/usr/local
make
sudo make install

#7zip
sudo yum install -y epel-release
sudo yum install -y p7zip

# Anaconda
cd
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
su bash ./Anaconda3-5.0.1-Linux-x86_64.sh
echo '# Anaconda Python3.6' >> .bashrc
echo 'export anaconda_HOME="/opt/anaconda3/"' >> .bashrc
echo 'export PATH=$anaconda_HOME/bin:$PATH' >> .bashrc