# Docker Machine
- 此篇 for CentOS7 及 Mac
- 2018/01/02

## For CentOS7
### Prerequest:
- 安裝好 Docker
- 安裝好 Virtual Box

```sh
# 下載並安裝 Docker-Machine
$ curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine && chmod +x /tmp/docker-machine && sudo cp /tmp/docker-machine /usr/local/bin/docker-machine

$ docker-machine version
docker-machine version 0.13.0, build 9ba6da9
```

## For Mac
### 安裝 virtual box會發生的問題額外備註
```sh
## Install VirtualBox on Mac
# First, install Homebrew
$ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

# Install Virtualbox
$ brew update
$ brew tap phinze/homebrew-cask
$ brew install brew-cask
$ brew cask install virtualbox
```

##### On Mac, the Virtualbox instlall is not properly integrated -- so it asks for a permission after it fails. Simply re-run the installation for a second time after having granted the OS driver the install permission. No need for uninstalls.

![Allow-Oracle](https://user-images.githubusercontent.com/1438457/31966122-81e98806-b8be-11e7-947e-388d5cf13095.png)
> 簡單說就是第一次安裝會失敗是因為Mac系統安全隱私等問題阻擋，所以`Open System Preferences > Security & Privacy and click the allow "Oracle" button`，再重新安裝一次即可。
```sh
# Reinstall VirtualBox
$ brew cask reinstall --force virtualbox.

# Checkout virtualbox version
$ virtualbox version
```
