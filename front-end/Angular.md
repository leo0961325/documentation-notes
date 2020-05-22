
## Install

- 2020/05/01
- [下載安裝檔](https://nodejs.org/en/download/)
- [如何把 NodeJS 移除乾淨](https://stackabuse.com/how-to-uninstall-node-js-from-mac-osx/)

```bash
### 一定要用 root
$# npm install -g @angular/cli
# (macbook) nodejs 被安裝到 /usr/local/bin/node

# ----------------------------------------------------------
# 2020/05/01 的這天
$ ng version
     _                      _                 ____ _     ___
    / \   _ __   __ _ _   _| | __ _ _ __     / ___| |   |_ _|
   / △ \ | '_ \ / _` | | | | |/ _` | '__|   | |   | |    | |
  / ___ \| | | | (_| | |_| | | (_| | |      | |___| |___ | |
 /_/   \_\_| |_|\__, |\__,_|_|\__,_|_|       \____|_____|___|
                |___/

Angular CLI: 9.1.4
Node: 12.16.3
OS: darwin x64

Angular: 
... 
Ivy Workspace: 

Package                      Version
------------------------------------------------------
@angular-devkit/architect    0.901.4
@angular-devkit/core         9.1.4
@angular-devkit/schematics   9.1.4
@schematics/angular          9.1.4
@schematics/update           0.901.4
rxjs                         6.5.4
# ----------------------------------------------------------
```



## Usage

```bash
### New APP
$# ng new NG_APP_NAME


### New Component
$# ng g c ComponentName


### New Service
$# ng g s ServiceName


### Routing Module (src/app/app-routing.module.ts)
$# ng generate module app-routing --flat --module=app
# --flat: 不增加資料夾結構
```