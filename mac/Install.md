

## Install Postgresql 11

- 2020/01/27
- https://installvirtual.com/install-postgresql-11-on-mac-os-x-via-brew/

```bash
### Install
$# brew search postgresql
$# brew install postgresql@11
# ...PASS...
==> Caveats
To migrate existing data from a previous major version of PostgreSQL run:
  brew postgresql-upgrade-database

postgresql@11 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have postgresql@11 first in your PATH run:
  echo 'export PATH="/usr/local/opt/postgresql@11/bin:$PATH"' >> ~/.bash_profile

For compilers to find postgresql@11 you may need to set:
  export LDFLAGS="-L/usr/local/opt/postgresql@11/lib"
  export CPPFLAGS="-I/usr/local/opt/postgresql@11/include"


To have launchd start postgresql@11 now and restart at login:
  brew services start postgresql@11  # Daemon
Or, if you don\'t want/need a background service you can just run:
  pg_ctl -D /usr/local/var/postgresql@11 start  # 前景執行
== Summary
🍺  /usr/local/Cellar/postgresql@11/11.6: 3,191 files, 36MB

```