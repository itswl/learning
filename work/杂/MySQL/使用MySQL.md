
示例数据 `https://codeload.github.com/datacharmer/test_db/zip/master`
导入 eg: `mysql -u root -p < employees.sql`

## 连接到 MySQL
; \g 输出水平显示
、G 输出垂直显示

```
mssql -h localhost -P 3306 -u root -p  - 连接到mysql
ALTER USER `root`@`localhost` IDENTIFIED BY 'password';  - 修改密码
```
### 创建数据库
数据库是许多表的集合，数据库服务器可以容纳许多这样的数据库

`数据库服务器 → 数据库 → 表（由列定义） → 行`

1. CREATE/ALTER/DROP  数据库对象（数据库和表） 称为 **数据定义语言（DDL）操作**
2. INSERT/UPDATE/DELETE /SELECT  称为 **数据操作语言（DML）** 前三项也称 **写**，SELECT 也称 **读**

```
CREATE DATABASE company;  - 创建数据库 建议都用 ``
CREATE DATABASE `my.contacts`; - 用反标记字符 ``（当数据库和表含特殊字符时） 
USE `company`; - 使用 company 数据库
mysql -u root -p company  - 直接连接到 company 数据库
SELECT DATABASE(); - 查找连接到的数据库
SHOW DATABASES; - 查找有权访问的所有数据库
SHOW VARIABLES LIKE 'company'; - 获取当前的数据目录

```
`sudo ls -lhtr /usr/lcoal/mysql/data/`

### 创建表
```
CREATE TABLE IF NOT EXISITS `company`.`customers`(
`id` int unsigned AUTO_INCREMENT PRIMARY KEY,
`first_name` varchar(20),
`last_name` varchar(20),
`country` varchar(20)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

SHOW TABLES - 查看所有表
SHOW CREATE TABLE customers\G - 查看表结构
DESC customers;
CREATE TABLE new_costomers Like customers - 克隆表结构
```

### 增删改查
参考

删除表的所有行最快的方式 `TRUNCATE TABLE customers`  DDL操作。

## 创建用户
**除非是localhost的管理任务等，一般不推荐使用root 用户连接到 mysql执行语句**



