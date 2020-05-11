:: Windows 時間校正 ex: TimeServer = 192.168.100.101
w32tm /config /update /manualpeerlist:192.168.100.101
w32tm /resync