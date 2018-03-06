# MySQL 5.7 on CentOS7

> DB目錄: /var/lib/mysql/

> 組態目錄: /etc/mysql/mysql.cnf


## backup
```sh
$ mysqladmin -uroot -p flush-logs

$ mysqldump <DB Name> -uroot -p --opt     >       <備份的文檔名稱.sql>
```

## restore
```sh
$ mysql <DB Name> -uroot -p    <      <備份的文檔名稱.sql>
```


Backup的 Script檔
```sh
#!/bin/sh
#    Note: This script just only backup one database!

# 1. 參數
DBNAME="phpbb2" # Database name
DBUSER="root"   # Database admin's name
DBPASS="password"   # Database admin's password
BINPATH="/usr/bin"  # MySQL command's path  (default: /usr/bin)
BAKDATE=`date +%w`  # Backup date format
BAKPATH="/usr/backup/phpbb" # Path for backup files save to
TMPDIR="tmp.db_bak".$BAKDATE    # Temp directory's name
BAKDIR="$DBNAME"_$BAKDATE   # Backup files's directory 
TABLST="tables_list"    # Database tables list files name
BAKTYPE="0" # Backup Type, 0: All tables in one dump file ; 1: Pre table in one dump file

# 2. Script Start
# 建立 backup站存區
cd /tmp
rm -rf $TMPDIR
mkdir $TMPDIR
cd $TMPDIR
mkdir $BAKDIR
cd $BAKDIR

# 建立 DB table list
$BINPATH/mysql $DBNAME -u$DBUSER -p$DBPASS -N -e "show tables" > $TABLST

# dump前, Flush DB LOG
$BINPATH/mysqladmin -u$DBUSER -p$DBPASS flush-logs

# Choice one type to dump datebase
case $BAKTYPE in
0)
 #
 # Dump database all table in one file
 #
 $BINPATH/mysqldump $DBNAME -u$DBUSER -p$DBPASS --opt > $DBNAME.sql
;;
1)
 #
 # Dump database pre table in one file
 #
 awk '{ print BINPATH"/mysqldump "DBNAME" -u"DBUSER" -p"DBPASS" \
      --opt " $1 " > " $1".sql" }' \
      BINPATH="$BINPATH" DBNAME="$DBNAME" DBUSER="$DBUSER" DBPASS="$DBPASS" \
      $TABLST \
      | /bin/sh
;;
*);;
esac

cd ..

# 壓縮 backup files
tar cfz $BAKDIR.tgz $BAKDIR
mv $BAKDIR.tgz $BAKPATH 
cd ..
rm -rf $TMPDIR

# Script End
```