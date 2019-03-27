
- 2019/03/03
- https://ithelp.ithome.com.tw/articles/10193649

```sh
### 新增 AppRoutingModule
$ ng generate module app-routing --flat --module=app
# --flat : 產生的文件放在 src/app
# --module=app : 註冊這個 Routing 在 AppModule 的 imports 裏頭
```

上述會產生 `src/app/app-routing.module.ts`

```ts
import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/common'; // 改成這樣
// import { CommonModule } from '@angular/common';      // 原始

@NgModule({
  imports: [
    CommonModule    // 建議刪除
    RouterModule    // 加入這個
  ],
  declarations: []  // 建議刪除
})
export class AppRoutingModule { }
```