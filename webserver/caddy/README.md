# caddyserver

- 2020/04/02
- [官網](https://caddyserver.com/)
- [一堆Caddy使用範例](https://github.com/caddyserver/caddy)
- [Caddy Documentation 1](https://caddyserver.com/v1/docs)
- [Caddy Documentation 2](https://caddyserver.com/docs/getting-started)


## Install

```bash
### macbook
$# brew install caddy
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/cask).
==> Updated Casks
ithoughtsx                                                                                 shinhan-ezplus

==> Downloading https://homebrew.bintray.com/bottles/caddy-1.0.5.catalina.bottle.tar.gz
Already downloaded: /Users/tony/Library/Caches/Homebrew/downloads/d23f06644034092ed9f38815513df252b948766a914d4ea74ecead264d63f6b5--caddy-1.0.5.catalina.bottle.tar.gz
==> Pouring caddy-1.0.5.catalina.bottle.tar.gz
==> Caveats
To have launchd start caddy now and restart at login:
  brew services start caddy
Or, if you don\'t want/need a background service you can just run:
  caddy -conf /usr/local/etc/Caddyfile
==> Summary
🍺  /usr/local/Cellar/caddy/1.0.5: 6 files, 20.7MB
```


# Usage

```bash
### for v1
### http://mygitea.com -> http://localhost:3000
# https://caddy.community/t/redirect-http-port-8080-to-https-80/4680
$# caddy -conf mygitea80_3000
Activating privacy features... done.

Serving HTTP on port 80
http://mygitea.com
```
