# Credentials

- 2019/02/14


## Create Cred

1. Windows auth user > Security > Logins > New Login
    - General
        - Login name (QQ)
        - SQL Server authentication
        - Default database
    - Status
        - Permission to conn : Grant
        - Login : Enabled
2. Databases > [DB] > Security > Users > New User
    - General
        - User type : SQL user with login
        - User name (同QQ)
        - Login name (同QQ)
    - Owned Schemas
        - db_owner

OK後, 會發現將來此 Database 下的使用者無法刪除, 因為已經變成 dbo 了

Databases > [DB] > Security > Schemas > dbo, 將 Schema owner 改回 dbo 即可

以上, 為了開發方便, 直接給 dbo, 但若都沒給, 別說 CRUD, 連預覽 Table 的權限都沒有

```powershell
### Windows auth login
> sqlcmd -E
1> USE master;
2> GO
Changed database context to 'master'.

### SQL auth login
> sqlcmd -U tony -P
1> 


```