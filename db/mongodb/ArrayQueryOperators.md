# [MongoDB v3.4 - Array Query Operators](https://docs.mongodb.com/v3.4/reference/operator/query-array/)
- 2018/04/25

```sh
$ pip install pymysql
```


```py
from pymongo import MongoClient
from bson.objectid import ObjectId
mm = MongoClient("mongodb://127.0.0.1/test")
db = mm.test
```


# $all - array內, 所有條件都要符合才算

```py
# Example
db.inventory.delete_many({'_id': {'$lt': 10}})
db.inventory.insert_many([{
   "_id": 1,
   "tags": [ "school", "book", "bag", "headphone", "appliance" ],
   "qty": [
          { "size": "S", "num": 10, "color": "blue" },
          { "size": "M", "num": 45, "color": "blue" },
          { "size": "L", "num": 100, "color": "green" }
        ]
},{
   "_id": 2,
   "tags": [ "appliance", "school", "book" ],
   "qty": [
          { "size": "6", "num": 100, "color": "green" },
          { "size": "6", "num": 50, "color": "blue" },
          { "size": "8", "num": 100, "color": "brown" }
        ]
},{
   "_id": 3,
   "tags": [ "school", "book" ],
   "qty": [
          { "size": "S", "num": 10, "color": "blue" },
          { "size": "M", "num": 100, "color": "blue" },
          { "size": "L", "num": 100, "color": "green" }
        ]
},{
   "_id": 4,
   "tags": [ "electronics", "school" ],
   "qty": [
          { "size": "M", "num": 100, "color": "green" }
        ]
}])
# <pymongo.results.InsertManyResult at 0x2c92c69dec8>
```

```py
# 找出 tags 要同時具備 ["appliance", "school", "book"]
q1 = db.inventory.find({
    'tags': {
        '$all': [ "appliance", "school", "book"]
    }
})
list(q1) # <pymongo.cursor.Cursor>
"""
[{'_id': 1,
  'qty': [{'color': 'blue', 'num': 10, 'size': 'S'},
   {'color': 'blue', 'num': 45, 'size': 'M'},
   {'color': 'green', 'num': 100, 'size': 'L'}],
  'tags': ['school', 'book', 'bag', 'headphone', 'appliance']},
 {'_id': 2,
  'qty': [{'color': 'green', 'num': 100, 'size': '6'},
   {'color': 'blue', 'num': 50, 'size': '6'},
   {'color': 'brown', 'num': 100, 'size': '8'}],
  'tags': ['appliance', 'school', 'book']}]
"""
```

```py
# 
q2 = db.inventory.find({
    'qty': {
        '$all': [
            {'$elemMatch': {'size': 'M', 'num': {'$gt': 50} } },
            {'$elemMatch': {'num': 100, 'color': 'green'}}
        ]
    }
})
list(q2) # <pymongo.cursor.Cursor>
"""
[{'_id': 3,
  'qty': [{'color': 'blue', 'num': 10, 'size': 'S'},
   {'color': 'blue', 'num': 100, 'size': 'M'},
   {'color': 'green', 'num': 100, 'size': 'L'}],
  'tags': ['school', 'book']},
 {'_id': 4,
  'qty': [{'color': 'green', 'num': 100, 'size': 'M'}],
  'tags': ['electronics', 'school']}]
"""
```

```py
# q3 = db.inventory.find( { "qty.num": { '$all': [ 50 ] } } ) # 兩者結果相同
q3 = db.inventory.find( { "qty.num" : 50 } )                # 兩者結果相同
list(q3) # <pymongo.cursor.Cursor>
"""
[{'_id': 2,
  'qty': [{'color': 'green', 'num': 100, 'size': '6'},
   {'color': 'blue', 'num': 50, 'size': '6'},
   {'color': 'brown', 'num': 100, 'size': '8'}],
  'tags': ['appliance', 'school', 'book']}]
"""
```



# $elemMatch - array內, 至少一個條件符合即可

```py
# Example
# 塞資料
db.scores.delete_many({'_id': {'$lt': 10}})
db.scores.insert_many([
    { '_id': 1, 'results': [ 82, 85, 88 ] },
    { '_id': 2, 'results': [ 75, 88, 89 ] }
])
```

```py
q4 = db.scores.find({
    'results': { '$elemMatch': { '$gte': 80, '$lt': 85}}
}) 
list(q4) # <pymongo.cursor.Cursor>
"""
[{'_id': 1, 'results': [82, 85, 88]}]
"""
```


```py
# Example
db.survey.delete_many({'_id': {'$lt': 10}})
db.survey.insert_many([
    {'_id': 1, 'results': [{'product': "abc", 'score': 10}, {'product': "xyz", 'score': 5}]},
    {'_id': 2, 'results': [{'product': "abc", 'score': 8}, {'product': "xyz", 'score': 7}]},
    {'_id': 3, 'results': [{'product': "abc", 'score': 7}, {'product': "xyz", 'score': 8}]}
])
# <pymongo.results.InsertManyResult at 0x2c92c6a9508>
```

```py
q5 = db.survey.find({
    'results': { '$elemMatch': { 'product': "xyz", 'score': { '$gte': 8 } } } 
})
list(q5) # <pymongo.cursor.Cursor>
"""
[{'_id': 3,
  'results': [{'product': 'abc', 'score': 7}, {'product': 'xyz', 'score': 8}]}]
"""
```



# $size - 官方文件我看不懂....

