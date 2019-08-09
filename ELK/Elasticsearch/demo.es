/*
    「Elasticsearch The Definitive Guide」 這本書的範例
*/
/* ========== 原始資料 ========== */
PUT /megacorp/employee/1
{
    "first_name": "John",
    "last_name": "Smith",
    "age": 25,
    "about": "I love to go rock climbing",
    "interests": ["sports", "music"]
}

PUT /megacorp/employee/2
{
    "first_name": "Jane",
    "last_name": "Smith",
    "age": 32,
    "about": "I like to collect rock albums",
    "interests": ["music"]
}

PUT /megacorp/employee/3
{
    "first_name": "Douglas",
    "last_name": "Fir",
    "age": 35,
    "about": "I like to build cabinets",
    "interests": ["forestry"]
}
/* ========== 原始資料 ========== */

/* 找出 last_name 為 Smith 的人 */
GET /megacorp/abc/_search
{
    "query": {
        "match": {
            "last_name": "Smith"
        }
    }
}

/* query: > 30 歲的 Smith */
GET /megacorp/employee/_search
{
    "query": {
        "bool": {
            "filter": {
                "range": {
                    "age": {"gt": 30}
                }
            },
            "must": {
                "match": {
                    "last_name": "smith"
                }
            }
        }
    }
}

/* 找出 about 與 「rock climbing」(包含)有關的人 */
GET /megacorp/employee/_search
{
    "query": {
        "match": {
            "about": "rock climbing"
        }
    }
}

/* 找出 about 與 「rock climbing」(符合)有關的人 */
GET /megacorp/employee/_search
{
    "query": {
        "match_phrase": {
            "about": "rock climbing"
        }
    }
}

/* highlight */
GET /megacorp/employee/_search
{
    "query": {
        "match_phrase": {
            "about": "rock climbing"
        }
    },
    "highlight": {
        "fields": {
            "about": {}
        }
    }
}

/* 此作法允許 text 欄位被拿來做分析(相當耗 RAM) */
/* https://blog.csdn.net/u011403655/article/details/71107415 */
/* 使用此前, 考慮清楚為何需要 text field 拿來作 aggregation, sorting(通常 make no sense) */
PUT /megacorp/_mapping/employee
{
    "properties": {
        "interests": {
            "type": "text",
            "fielddata": true
        }
    }
}

/* 最多人感興趣的嗜好 (但必須先 enable Filedata on text fields)*/
GET /megacorp/employee/_search
{
    "aggs": {
        "all_interests": {
            "terms": {
                "field": "interests"
            }
        }
    }
}

/* last_name 含有 smith 的人, 感興趣的嗜好計量 */
GET /megacorp/employee/_search
{
    "query": {
        "match": {
            "last_name": "smith"
        }
    },
    "aggs": {
        "all_interests": {
            "terms": {
                "field": "interests"
            }
        }
    }
}

/* 對特定嗜好感興趣的人們的平均年齡 */
GET /megacorp/employee/_search
{
    "aggs": {
        "all_interests": {
            "terms": { "field": "interests" },
            "aggs": {
                "avg_age": {
                    "avg": { "field": "age" }
                }
            }
        }
    }
}

/* 比較! PUT 新增資料 at the URL */
PUT /website/blog/123
{
    "title": "My first blog entry",
    "text": "Just trying this out...",
    "date": "2019/01/30"
}

/* 比較! POST 新增資料 under the URL */
POST /website/blog
{
    "title": "My second blog entry",
    "text": "Still trying this out...",
    "date": "2019/01/30"
}

/* 查不到資料, 404, "found": false */
GET /website/blog/1234
{}

/* 只找指定的欄位 */
GET /website/blog/123?_source=title,text
{}

/* 此查詢查全部欄位, 而此查詢等同於最後面再加上「_source」 */
GET /website/blog/123
{}

/* 通常用 HEAD 來判斷資源存不存在. ((200, 在 ; 404, 不在)) */
HEAD /website/blog/1234

/* Update (版本會更動) */
PUT /website/blog/123
{
    "title": "My first blog entry",
    "text": "I am starting to get the hang of this...",
    "date": "2019/01/30"
}

/*  */
POST /website/blog/1/_update
{
    "doc": {
        "tags": [ "testing" ],
        "views": 0
    }
}


