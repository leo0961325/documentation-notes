

```py
>>> db2.users.insert_one({
    "_id": "Tom Benzamin",
    "addresses": ['addr A', 'addr B']
})
<pymongo.results.InsertOneResult at 0x17f6d334788>
```

```py
>>> db2.address.insert_many([{
        "_id": "addr A",
        "building": "22 A, Indiana Apt",
        "pincode": 123456,
        "city": "Los Angeles",
        "state": "California"
    }, {
        "_id": "addr B",
        "building": "170 A, Acropolis Apt",
        "pincode": 456789,
        "city": "Chicago",
        "state": "Illinois"
    }
])
<pymongo.results.InsertManyResult at 0x17f6d334f08>
```

```py
>>> result = db2.users.find_one({'_id': 'Tom Benzamin'})

>>> addr = db2.address.find({'_id': {'$in': result['addresses']}})
>>> list(addr)
[
    {
        '_id': 'addr A',
        'building': '22 A, Indiana Apt',
        'city': 'Los Angeles',
        'pincode': 123456,
        'state': 'California'
    },{
        '_id': 'addr B',
        'building': '170 A, Acropolis Apt',
        'city': 'Chicago',
        'pincode': 456789,
        'state': 'Illinois'
    }
]
```