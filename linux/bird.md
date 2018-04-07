# 鳥哥自學

[第十七章、區網控制者： Proxy 伺服器](http://linux.vbird.org/linux_server/0420squid.php#theory)

(準備把這個廢了)

章節 | 閱讀日期
--- | ---
17.1 什麼是代理伺服器 (Proxy) | -
&nbsp;&nbsp;&nbsp;&nbsp;17.1.1 什麼是代理伺服器 | 2017/12/06 
&nbsp;&nbsp;&nbsp;&nbsp;17.1.2 代理伺服器的運作流程 | 2017/12/06 
&nbsp;&nbsp;&nbsp;&nbsp;17.1.3 上層代理伺服器 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.1.4 代理伺服器與 NAT 伺服器的差異 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.1.5 架設代理伺服器的用途與優缺點 | 
17.2 Proxy 伺服器的基礎設定 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.2.1 Proxy 所需的 squid 軟體及其軟體結構 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.2.2 CentOS 預設的 squid 設定： http_port, cache_dir (SELinux), cache_mem | 
&nbsp;&nbsp;&nbsp;&nbsp;17.2.3 管控信任來源 (如區網) 與目標 (如惡意網站)： acl 與 http_access 的使用 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.2.4 其他額外的功能項目 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.2.5 安全性設定：防火牆, SELinux 與黑名單檔案 | 
17.3 用戶端的使用與測試 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.3.1 瀏覽器的設定： firefox & IE | 
&nbsp;&nbsp;&nbsp;&nbsp;17.3.2 測試 proxy 失敗的畫面 | 
17.4 伺服器的其他應用設定 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.4.1 上層 Proxy 與獲取資料分流的設定 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.4.2 Proxy 服務放在 NAT 伺服器上：通透式代理 (Transparent Proxy) | 
&nbsp;&nbsp;&nbsp;&nbsp;17.4.3 Proxy 的認證設定 | 
&nbsp;&nbsp;&nbsp;&nbsp;17.4.4 末端登錄檔分析： sarg | 