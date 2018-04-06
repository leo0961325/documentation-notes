# token (令牌)

以REST的架構來講, 具有下列6個特色
1. Client-Server
2. Stateless
3. Cache
4. Uniform Interface
5. Layered System
6. Code-on-Demand

> 每次請求之間, Server不會去記錄任何請求之間的片段資訊, 若遇到某些 Resource需要特定權限時, 每次都得去檢查 request.session(來自前端網頁的 cookies). 但是...!!! 如果 Client端的請求不是網頁呢?(通常沒有 cookies這咚咚), 而且, 就算檢查 request.session好了, 每次請求都超級大一包, 誰受的了阿!! 因而有了`Token-Based Authentication`

> 每次請求時, `user credential`都隨著 HTTP被夾帶出去, 有被竊取的風險, 所以最好是做成`HTTPS(加密的 HTTP)`

## Token-Based Authentication
弄好一個特殊的URL, 讓 Client端通過驗證後, 取回一個`短時間內到期的 authentication token`. 所以稍後在短時間內的所有請求, 後端直接驗證這個小巧一包的 token即可.
