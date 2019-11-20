## 1. URL 与 URI
URI : 统一资源标识符

URL : 统一资源定位符

(URN : 统一资源名称  只命名资源 而不指定如何定位资源)

URL 是 URI 的子集 


## 2. 超文本
Hypertext ,用超链接的方法，将各种不同空间的文字信息组织在一起的网状文本。

网页源代码 HTML 可以称之为超文本。 

## 3. HTTP HTTPS
HTTP : 超文本传输协议，用于从网络传输超文本数据到本地浏览器的传送协议

HTTPS ： 以安全为目标的 HTTP通道。即 HTTP 下加入 SSL 层。通过其传输的内容都经过 SSL 加密。
1. 建立一个安全信息通道，来保证数据传输的安全。 
2. 确认网站的真实性。

## 4. HTTP 请求过程
浏览器（客户端） 输入 URL ,向服务器发送一个 Request (请求), 服务器收到 Request 后，返回对应的一个 Response (响应), Response 中包含
页面的源代码等内容，浏览器再进行解析，便将网页呈现出来。

## 5. Request 
**Request 可分为四部分**
1. Request Method (请求方式)
2. Request URL （请求连接）
3. Request Headers （请求头）
4. Request Body （请求体）

### 5.1 Request Method
请求方式，常见有 **GET** , **POST**

**GET** 请求参数会直接包含在URL里， （eg:https://www.baidu.com/s?wd=Python wd 就是要搜寻的关键字）

**POST** 一般用于表单提交发起，数据常以 Form Data 即表单形式传输，不会体现在 URL 中。（包含在 Request Body 中）

**GET** 请求提交的数据最多只有1024字节。

**其他请求方式**

1. HEAD
2. PUT
3. DELETE
4. CONNECT
5. OPTIONS
6. TRACE

### 5.2 Request URL

**请求的网址，即统一资源定位符，可以唯一确定我们想请求的资源**

### 5.3 Request Headers
 
**请求头， 用来说明服务器要使用的附加信息，比较重要的有Cookie,Refer,User-Agent等**

1. Accept : 请求报头域，用于指定客户端可接受的语言类型
2. Accept-Language : 指定客户端可接受的语言类型
3. Accept-Encoding : 指定客户端可接受的内容编码
4. HOST : 用于指定请求资源的主机和端口号
5. Cookie : 是网站为了辨别用户进行 Session 跟踪而储存在用户本地的数据。
6. Referer : 用来标识这个请求是从哪个页面发出来的
7. User-Agent : UA,特殊的字符串头，使得服务器能够识别客户使用的操作系统及版本、浏览器及版本等信息。（爬虫时可加次信息伪装成浏览器）
8. Content-type : 互联网媒体类型，在 HTTP 协议消息中，使用它来表示具体请求中的媒体类型信息。（Application/josn ,image/gif, text/html等）

### 5.4 Request Body 

**一般承载的内容为 POST 请求中的Form Data , 而对于 GET 请求  Request Body 则为空。**


## 6. Response 

**由服务端返回给客服端。Response可以分为三部分**

1. Request Status Code (响应状态码)
2. Response Headers （响应头）
3. Response Body （响应体）

### 6.1 Request Status Code
200 表示正常。 404 表示页面未找到。 500 表示服务器内部异常。

**一般情况下**

2开头 （请求成功）表示成功处理了请求的状态代码。

3开头 （请求被重定向）表示要完成请求，需要进一步操作。 通常，这些状态代码用来重定向。

4开头 （请求错误）这些状态代码表示请求可能出错，妨碍了服务器的处理。

5开头（服务器错误）这些状态代码表示服务器在尝试处理请求时发生内部错误。 这些错误可能是服务器本身的错误，而不是请求出错。

### 6.2 Response Headers
**包含了服务器对请求的应答信息**

部分信息

1. date : 标识 Response 产生的时间
2. Last-Modified : 指定资源的最后修改时间
3. Content-Encoding ：指定 Response 内容的编码
4. Server : 包含了服务器的信息
5. Content-type ： 同Request
6. Set-Cookie : 设置Cookie, 即告诉浏览器需要将此内容放到Cookies中，下次请求携带Cookies请求。
7. Expires : 指定 Response 的过期时间，使用它可以控制代理服务器或浏览器将内容更新到缓存中，如再次访问，直接从缓存中加载，降低服务器荷载，缩短加载时间。



### 6.3 Response Body

**响应的正文数据都是在响应体中**
（爬虫请求网页后要解析的数据就是解析响应体）

在浏览器开发工具中点击Preview,就可以看到网页源代码、json数据等，然后从中做相应内容的提取






