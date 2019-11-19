## java简介
Java分为三个体系：

JavaSE(J2SE)(Java2 Platform Standard Edition，java平台标准版)

JavaEE(J2EE)(Java 2 Platform,Enterprise Edition，java平台企业版)

JavaME(J2ME)(Java 2 Platform Micro Edition，java平台微型版)

### 开发环境配置(windows下)

[java下载](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

下载后安装，配置系统环境变量

此电脑 > 右键属性 > 高级 > 环境变量
```
变量名：JAVA_HOME
变量值：C:\Program Files (x86)\Java\jdk1.8.0_91        // 要根据自己的实际路径配置
变量名：CLASSPATH
变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;         //记得前面有个"."
变量名：Path
变量值：%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;

windows10 变量值已有的上面点开，然后新建加到下方，以免破坏原有的环境变量
```

重启后生效

### 测试JDK是否安装成功

1、"开始"->"运行"，键入"cmd"；

2、键入命令: java -version、java、javac 几个命令
