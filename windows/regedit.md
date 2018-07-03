# 登錄編輯程式

```powershell
> systeminfo

主機名稱:             3200-PM0024-1
作業系統名稱:         Microsoft Windows 10 專業版
作業系統版本:         10.0.17134 N/A 組建 17134
# 後略...
# 1803版
```

# 移除快速釘選上面的 OneDrive

Win+r

regedit

HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}

修改值 1 -> 0

done