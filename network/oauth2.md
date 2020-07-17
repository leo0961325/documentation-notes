# Oauth2

- 2020/06/29
- [OAuth 2.0 筆記](https://blog.yorkxin.org/2013/09/30/oauth2-1-introduction.html)
- [RFC6749-Oauth2.0](https://tools.ietf.org/html/rfc6749)

# Terms

- *RO*, Resource Owner(User): 可悲的你
- Client(Third-party APP): 第三方用戶程序
- *UA*, User Agent: 通常是指瀏覽器
- *AS*, Authorization Server: 認證伺服器, Http Service Provider 用來做認證的伺服器, 頒發 token 用
- *RS*, Resource Server: 資源伺服器. 你得拿 token 來驗證身分, 才可領走你想要的東西


# Client 取得授權的方式

- Authorizaiton code : 最嚴謹 最完整
- Implicit
- Resource Owner Password Credentials
- Client Credentials


## 1. Authorization Code

透過 **Client 後湍** 與 **Service Provider** 互動. 

- Client 將 User 導向 *AS*
- Client 再決定是否授權給 Client
- 若OK, *AS* 將 Client 導向 Client 事先設定好的 **Redirect URI**, URI 會附上 **Authorization Code, AC**
- Client 收到 **AC**, 連同 **Redirect URI** 向 *AS* 申請 token (在 Client Backend Server 完成, User 看不到此流程)
- *AS* 核對 **AC** && **Redirect URI**, 確認無誤後核發 token && refresh token


## 2. Implicit

## 3. Resource Owner Password Credentials

## 4. Client Credentials


# 摘要

- 自己製作出可以讓別人接我們的 OAuth2 的服務 (自己即是 Provider)
- Oauth 引入 authorization layer 來把 Resource Owner && Client 分開
    - 用以解決 Server 與 第三方服務 之間的權限問題
- 在 Oauth 中, Client 向 Resource Owner 索取 存取權(取得 credentials) 來存取 Resource Owner 上的資源(在 Resource Server 上).
- Client 出示 Authorization Grant 來認證自己, Authorization Server 才會頒發 Access Token 給 Client, 用此來存取 Resource Server 上的 Protected Resources (而非使用 Resource Owner 的帳密 來做資源請求)
    - Access Token 記載了 Period && Scope
- Client 取得來自 Resource Owner 的 Authorization Grant. 此類型有 4 種(但可擴充), 至於用哪種類型, 要看 Client 請求授權的方法 or Authorization Server 支援的類型來決定.
- Client 拿 Authorization Server 頒發的 Access Token 去 Resource Server 請求 Protected Resource, Resource Server 驗證 Access Token, 若合法, 則回覆請求.
- Access Token 可以加上用來取得授權資訊的 identifier (ex: 編號 or 識別字) or 內建可以驗證的授權資訊(ex: 數位簽章)
- Authorization Grant type(內建授權流程) 區分為 4 種:
    1. Authorization Code Grant Type Flow
        - 向 Authorization Server 先取得 Grant Code, 再取得 Access Token
        - 適合 Confidential Clients (ex: Server 上的 App)
        - 可核發 Refresh Token
        - 需要 User-Agent Redirection
    2. Implicit Grant Type Flow
        - Authorization Server 先向 Client 核發 Access Token
        - 適合非常特定的 Public Clients(ex: Browser 內的 App)
        - Authorization Server 不必 && 無法 驗證 Client 的身分
        - 無法核發 Refresh Token
        - 需要 User-Agent Redirection
        - 有個資外洩風險
    3. Resource Owner Password Credentials Grant Type Flow
        - Resource Owner 的 帳密 直接拿來當作 Grant
        - 適用於 Resource Owner 高度信任 Client (ex: OS 內建 App, 官方 App)
        - 其他流程無法使用再來用這個
        - 可核發 Refresh Token
        - 無 User-Agent Redirection
    4. Client Credentials Grant Type Flow
        - Client ID && Client Secret 直接來當作 Grant
        - 適用於跑在 Server 上的 Confidential Client (不懂)
        - 不建議核發 Refresh Token
        - 無 User-Agent Redirection
- Clients 類型分為 Public && Confidential 兩種

### 技術要求

- 使用 TLS(HTTPS)
- User-Agent 要支援 HTTP Redirection
    - 




# Compare

- A. Authorization Code
- B. Implicit
- C. Password Credentials
- D. Client Credentials

複雜程度: A > B > C > D

- Refresh Token: A, C, D