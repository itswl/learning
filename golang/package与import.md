## import 原理
此处需要插图

## import 导入包的几种方式：点，别名与下划线
在写Go代码的时候经常用到import这个命令用来导入包文件，看到的方式参考如下：
```
     import(
         "fmt"
     )
```
然后在代码里面可以通过如下的方式调用
`fmt.Println("hello world")`

上面这个fmt是Go语言的标准库，他其实是去GOROOT下去加载该模块，当然Go的import还支持如下两种方式来加载自己写的模块：

相对路径     `import   "./model"`  // 当前文件同一目录的model目录，但是不建议这种方式import

绝对路径    `import   "shorturl/model"`  // 加载GOPATH/src/shorturl/model模块

## 三种导入包的使用方法。

1. 点操作` import( . "fmt" )` 
可以省略前缀的包名，`fmt.Println("hello world") ` 可以省略的写成Println("hello world")

2. 别名操作`import( f “fmt” )`   调用包函数时前缀变成了重命名的前缀，即f.Println("hello world")

3.  _操作`import ( "database/sql" _ "github.com/ziutek/mymysql/godrv" ) `

_操作其实只是引入该包。即使用_操作引用包是无法通过包名来调用包中的导出函数，而是只是为了简单的调用其init函数()

