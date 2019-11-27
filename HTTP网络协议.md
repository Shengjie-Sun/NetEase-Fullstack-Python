### URL: Uniform Resource Locater (统一资源定位符)

https://e-hentai.org:443

https://www.baidu.com:443/index.html

（协议）+（主机端口，默认443）+（文件名以及路径）

1. 浏览器分析超链接中的URL

2. 浏览器向DNS请求解析

3. DNS将解析出的IP地址返回给浏览器

4. 浏览器于服务器建立TCP连接（443端口）

5. 浏览器请求文档：GET

6. 服务器发出响应，将文档发送给浏览器

7. ...

8. 释放TCP连接

9. 浏览器显示内容

HTTP协议没有状态

### HTTP报文结构

- 请求报文

    1. 请求行：
    
        【方法(GET)】【URL】【版本】CRLF
    2. 首部行：
        
        【首部字段名】【值】CRLF

        Host: e-hentai.org CRLF

        Commection: close CRLF

        User-Agent: MOzilla/5.0 CRLF

        Accept-Language: cn CRLF

        CRLF

    3. 实体：Entity body

- 返回报文

    1. 状态行

        【版本】【状态码】【短语】CRLF

    2. 首部行

        【首部字段名】【值】CRLF

        Date: Wed 08 May 2008 22

        Sever: Apache/1.3.3(Unix)

        CRLF
    3. 实体: Entity body

- 请求报文中的方法

    - GET: 请求读取一个Web页面

    - POST：附加一个命名资源

    - HEAD：请求读取一个Web页面的首部

    - PUT：请求存贮一个Web页面

    - DELETE：删除Web页面

    - TRACE：用于测试，请求服务器送回收到的请求

    - CONNECT：用于代理服务器

    - OPTION：查询特定选项

- 响应报文中的状态码

    - 1xx：通知信息

    - 2xx：成功：200请求成功

    - 3xx：重定向

    - 4xx：客户错误：404页面未找到

    - 5xx：服务器错误：500服务器内部错误

- 首部字段或者消息头
    
    【请求】

    - User-Agent

    - Accept

    - Accept-Charset

    - Accept-Encoding

    - Accept-Language

    - Host

    - Authorization

    - Cookie

    【双向】

    - Date

    【返回】

    - Server

    - Content-Encoding

    - Content-Language

    - Content-Length

    - Content-Type

    - Last-Modified

    - Location

    - Set-Cookie

### HTTP代理

HTTP代理又称Web缓存或代理服务器（Proxy Server）是一种网络实体，能代表浏览器发出HTTP请求，并将最近的一些请求和响应暂存在本地磁盘中，当请求的Web页面先前暂存过，则直接将暂存的页面发送给客户端（浏览器），无需再次方位Internet。