# pymongo筆記
- 2018/04/24


## 增刪查改

### 查 query find

- [find](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.find)

```py
def query(name):
    return db.status.find({'name': name})
    """ return <pymongo.cursor.Cursor>
        <pymongo.cursor.Cursor>.count() 得知查詢的筆數

        list( <pymongo.cursor.Cursor> )
        [
            { 
                'name': xxx, ...
            }, ...
        ]
    """
```


### 增 insert

- insert  **DEPRECATED**
- [insert_one](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.insert_one)
- [insert_many](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.insert_many)

```py
def insert(name):
    return db.status.insert_one({'name': name})
    """ return <pymongo.results.InsertOneResult>
        <pymongo.results.InsertOneResult>.inserted_id 得知新增資料的 _id

        insert_one(document, bypass_document_validation=False, session=None)
    """
```


### 改 update

- update **DEPRECATED**
- [replace_one](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.replace_one)
- [update_one](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.update_one)
- [update_many](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.update_many)

```py
def update(name, new_name):
    return db.status.update_one({'name': name}, {'$set': {'name': new_name}})
    """ return <pymongo.results.UpdateResult>
        <pymongo.results.UpdateResult>.modified_count 得知更新筆數

        update_one(filter, update, upsert=False, bypass_document_validation=False, collation=None, array_filters=None, session=None)
    """
```


### 刪 remove

- remove **DEPRECATED**
- [delete_one](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.delete_one)
- [delete_many](https://api.mongodb.com/python/current/api/pymongo/collection.html?highlight=update_one#pymongo.collection.Collection.delete_many)

```py
def remove(name):
    return db.status.remove({'name': name})
    """ return <dict>
        <dict>.get('n') 得知移除筆數

        dict範例:
        {
            'n': 1,      <--- 表示已經移除一筆
            'ok': 1.0    <--- 表示移除成功
        }
    """
```