# Django REST framework
- 2018/08/12
- v3.8.2


## Request parsing

### `r.data`

回傳 json, 此結果幾乎與 `r.POST`, `r.FILES` 相同


### `r.query_params`

較 `r.GET` 使用上語意更加明確.


### `r.parsers` (通常用不到... 別理他)



# Browser enhancements

drf 對於 瀏覽器的 web form 的 `PUT`, `PATCH`, `DELETE` 有提供額外方法:

`.content_type`(而非 .META.get('HTTP_CONTENT_TYPE')) 取出 media_type

`.stream` 取出 stream



# 繼承架構

```
Serializer
    ↑
ModelSerializer
    ↑
HyperlinkedModelSerializer
```

## `ModelSerializer` vs Serializer

使用 serializers.ModelSerializer 取代 serializers.Serializer (兩者皆為 Form 的概念), 而 ModelSerializer 直接給定 Meta
1. 直接套用 models 定義好的 schema 來當作 metadata
2. 預設實作了簡單版的 create() 及 update()



# Models

```py
from django.db import models

class XX(models.Model):

    class Meta:
        ordering = ('a',)                   # 依照欄位排序
        managed = True                      # 允許 Django 建立, 修改, 刪除 Table
        db_table = 'tbl_name'               # Table Name
        unique_together = (('x', 'y'),)     # 唯一值組合
```



# Serializers

```py
# 很容易跟 Models 搞混成一團 @@...
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:     # 改成 ModelSerializer 需要定義 Meta (資料結構吧?!)
        model = Snippet
        fields = '__all__'
```



# auth

- `request.user`
- `request.auth`