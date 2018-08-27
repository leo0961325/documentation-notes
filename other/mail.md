# mail

- 2018/02/14
- [使用其他電子郵件程式讀取 Gmail 郵件 (透過 POP 協定)](https://support.google.com/mail/answer/7104828)
- [變更 SMTP 設定以便使用其他程式查看 Gmail](https://support.google.com/mail/answer/7126229?hl=zh-Hant)
- [利用GMAIL來寄信](http://ec.softking.com.tw/use/use.asp?id=331)
- [mailbox寄信](https://www.cloudmax.com.tw/service/guideline/officemail-outlook)
## IMAP 與 POP 比較

IMAP 和 POP 都可讓您透過其他電子郵件程式讀取 Gmail 郵件。

Protocol             | IMAP           | POP
-------------------- | -------------- | ---------------------------
Device               | 多裝置         | 單一裝置
async                | 即時同步       | 非即時同步, 採用郵件下載方式
Incoming Mail Server | imap.gmail.com | pop.gmail.com
 SSL                 | Yes            | Yes
 port                | 993            | 995
Outgoing Mail Server | smtp.gmail.com | smtp.gmail.com
 SSL                 | Yes            | Yes
 TLS                 | Yes            | Yes
 Authentication      | Yes            | Yes
 SSL port            | 456            | 465
 TLS port/STARTTLS   | 587            | 587
 Server time out     | -              | 大於1分鐘(建議設5分鐘)


smtp: officemail.cloudmax.com.tw
pop3: officemail.cloudmax.com.tw
