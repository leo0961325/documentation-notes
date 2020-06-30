# DroneCI

## 架構

- [pipeline的環境變數](https://exec-runner.docs.drone.io/configuration/variables/)

- Drone Server        : 負責蒐集 Git Repo 內所有專案的事件(定義在各個專案底下的 `.drone.yml`)
- Drone Runner(Agent) : 負責執行 DroneServer 分派下來的 pipeline流程. runner 有下列幾種:
  - Docker Runner
  - Kubernates Runner
  - Exec Runner : 在 Runner 所在的主機執行(非 Drone Server 上運行)(2020/06, 目前為實驗性質)
  - SSH Runner : 通常透過 ssh 執行遠端命令來做建置
  - Digital Ocean Runner
  - Macstadium Runner

- 一個 Drone Server, 會設定追蹤一個 Git Server (不知道可否多個)
- 可針對每個專案設定是否 啟用(Activate Repository), 讓 Drone Server 針對特定事件去做些什麼
- 一旦專案被啟用後, 須在裡頭設定一個 `.drone.yml` (每個專案會有一個對應的 .drone.yml )
- 一個 `.drone.yml` 裡頭, 可以有 1~N 個 pipeline (community 版本, 只能讓單一 Drone Runner 來跑 pipeline)


```yml
---
kind: pipeline
name: backend
steps:
  - name: Job 1 Name
    image: node
    commands:
    - npm install
    - npm test
    - ...
    settings:
      when:
        branch:
          - master
          - feature/*
```