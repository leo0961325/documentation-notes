# VSCode - Database Support

VSCode 也可以成為 Database 的 GUI

參考以下的示範

- [MySQL](#MySQL)
- [MongoDB](#MongoDB)

- VSCode version: 1.26.0
- 2018/08/29


## MySQL

- 套件: [MSQL 0.3.0](https://marketplace.visualstudio.com/items?itemName=formulahendry.vscode-mysql)

SideBar(Explorer) / MySQL / Add Connection / (輸入底下的參數)

1. host
2. username
3. password
4. port
5. ssl path


## MongoDB

- 套件: [Azure Cosmos DB](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-cosmosdb)

SideBar(Azure) / Attach Database Account > MongoDB > (輸入底下的連接字串)

`mongodb://<username>:<password>@<host>:<port>/<database>`  此 username 要具有 database 的權限

`mongodb://<username>:<password>@<host>:<port>`             此 username 要具有 任何資料庫的權限

`mongodb://<host>:<port>`                                   無權限機制的連線方式
