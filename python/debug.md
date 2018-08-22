# Debug

```sh
# https://stackoverflow.com/questions/22834392/understanding-too-many-ancestors-from-pylint
$ pylint -r n snippets/views.py
************* Module snippets.views
snippets\views.py:13:0: R0901: Too many ancestors (12/7) (too-many-ancestors)
snippets\views.py:22:0: R0901: Too many ancestors (12/7) (too-many-ancestors)
snippets\views.py:26:15: E1101: Class 'Snippet' has no 'objects' member (no-member)

------------------------------------------------------------------
Your code has been rated at 5.33/10 (previous run: 8.67/10, -3.33)
# 看起來好像是察看 語法訊息... (廢話!)
```


# RemoteDebug

- [Python debugging configurations in VS Code - Remote debugging](https://code.visualstudio.com/docs/python/debugging#_remote-debugging) Comming Soon...

