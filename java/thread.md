# Java #
## 執行緒與併行API

備註


### 啟動執行緒的方法
```java
Doing1 job1 = new Doing();
Thread t1 = new Thread(job1);
t1.start();
```


### 將執行緒改為背景執行

t1.setDaemon(true);


### 改變執行緒優先權

setPriority(x);

x為1~10, 數字越大優先權越高


### 讓執行緒睡1秒, 進入Blocked狀態

Thread.sleep(1000); 


### 多執行緒multi-thread Lambda寫法

```
new Thread(() -> {
    ...
});
```


### 安插執行緒

```java
// 主執行緒執行t2.start()後, 馬上被t2.join()插隊
Thread t2 = new Thread(() -> {
    ...
});
t2.start();
t2.join();
...
```


### 停止執行緒

```java
thread.stop();  // 因為某些原因被depreciated了. 停止執行緒教佳的方式, 應該設條件, 讓他達成條件時停止
public class SomeThread implements Runnable {
    private boolean isContinue = true;
    ...
    public void stop() {
        isContinue = false;     //改變開關
    }

    public void run() {
        while (isContinue) {    
            ...
}}}
```












