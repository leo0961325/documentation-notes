# Web Server
- 2018/05/18
- [What is the point of uWSGI?
](https://stackoverflow.com/questions/38601440/what-is-the-point-of-uwsgi?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
- [python server比較](https://www.digitalocean.com/community/tutorials/django-server-comparison-the-development-server-mod_wsgi-uwsgi-and-gunicorn)
- [寫得很棒的Web Server/App Server - RoR觀點](https://github.com/evenchange4/blog/blob/master/source/_posts/Ruby/2013-07-04-server.md)


## 比較 
- uWSGI: `純 Python的 Web Server`. 本身很大一包, **好像** 只能在 Linux上面運行.
- WSGI : `python web 框架` 需邀遵照的協議 (基本上, web service開發人員不用理這個...)
- uwsgi: `python base Web Server` 與 `Reverse Proxy Server(Nginx)` 溝通的協定 (應該吧!?)
