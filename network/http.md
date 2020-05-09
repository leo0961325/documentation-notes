# Hypertext Transfer Protocol (HTTP)

- http/1.0
- http/1.1 : [2616](https://tools.ietf.org/html/rfc2616)
- http/2   : [7230](https://tools.ietf.org/html/rfc7230)



# 名詞

- Internet Engineering Task Force (IETF)
- Internet Engineering Steering Group (IESG)



# http 這東西

HTTP/2 為 HTTP/1.1 的替代方案 ; 藉由引入 `header field compression` && `allow multiple concurrent exchange on the same connection` 減少網路傳輸延遲, 來提升網路傳輸效能, 減少延遲的知覺.

> `HTTP/1.0` allowed only one request to be outstanding at
   a time on a given TCP connection.

> `HTTP/1.1` added request pipelining,
   but this only partially addressed request concurrency and still
   suffers from head-of-line blocking.  Therefore, HTTP/1.0 and HTTP/1.1
   clients that need to make many requests use multiple connections to a
   server in order to achieve concurrency and thereby reduce latency.

# HTTP

- [What does enctype='multipart/form-data' mean?](https://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean)

> When you make a POST request, you have to encode the data that forms the body of the request in some way.

HTML form 提供了 3 種方法來做 encoding:

- application/x-www-form-urlencoded (default)
- multipart/form-data
- text/plain