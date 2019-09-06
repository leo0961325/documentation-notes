# site - Site-specific configuration hook

- https://docs.python.org/3/library/site.html
- 2019/08/12

---

**site 模組初始化時自動 import**

Importing 此模組可:
1. append `site-specific paths` 到 *模組搜尋路徑(sys.path)*
2. 增加一些 builtins

但若使用了 `-S` 則無上述功能

---

`import site` 會驅動 **head** 及 **tail** 兩個部分:
- head
  - sys.prefix
  - sys.exec_prefix
- tail
  - for win10: lib/site-packages
  - for linux: lib/pythonX.Y/site-packages

若上述資料夾存在, 則會被加入到 `sys.path`

---

若 `pyvenv.cfg (bootstrap configuration file)` 存在於 `sys.executable`, 則

- sys.prefix
- sys.exec_prefix

將會被視為 `sys.executable` 所指的位置 && 還會檢查 site-packages. 如此一來:

- sys.base_prefix
- sys.base_exec_prefix

始終為 `"real" prefixes of the Python installation`

此外, 如果 `pyvenv.cfg` 內包含了 `include-system-site-packages` && 此值非為 `false`, 則 system-level prefixes 也會去尋找 site-packages

---

`path configuration file`

---

ex:

- sys.prefix
- sys.exec_prefix

被設定到 `/usr/local`. 則 PythonX.Y library 將會是 `/usr/local/lib/pythonX.Y`

又假設 `/usr/local/lib/pythonX.Y` 底下有 (3 dirs && 2 files)

- /usr/local/lib/pythonX.Y/site-packages/
  - foo/
  - bar/
  - spam/
  - foo.pth
  - bar.pth

而其內檔案內容為:

```ini
### foo.pth
# foo package configuration
foo
bar
bletch
```

 為

```ini
### bar.pth
# bar package configuration

bar
```

則下列資料夾將會被依序加入到 `sys.path` (bletch, spam 不會被加入):

- /usr/local/lib/pythonX.Y/site-packages/bar
- /usr/local/lib/pythonX.Y/site-packages/foo


