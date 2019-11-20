## hello world

HelloWorld.java  (源文件名必须和类名相同)
```
public class HelloWorld {
   /* 第一个Java程序.  
    * 它将打印字符串 Hello World
    */
    public static void main(String []args) {  // 主方法入口：所有的Java 程序由public static void main(String args[])方法开始执行
       System.out.println("Hello World"); // 打印 Hello World
    }
} 
```
（cmd在java文件的同一路径下）
1. 编译 `javac -encoding utf-8 HelloWorld.java`  (含中文最好使用 -encoding utf-8编译，以免出现错误)
2. 运行 `java HelloWorld`  打印  HelloWorld

## 类和对象
```
public class Puppy{  // Puppy 类  一个源文件中只能有一个public类
   int puppyAge;
   public Puppy(String name){
      // 这个构造器仅有一个参数：name
      System.out.println("Passed Name is :" + name ); 
   }

   public void setAge( int age ){
       puppyAge = age;
   }

   public int getAge( ){
       System.out.println("Puppy's age is :" + puppyAge ); 
       return puppyAge;
   }

   public static void main(String []args){
      /* 创建对象 */
      Puppy myPuppy = new Puppy( "tommy" );  // 声明：声明一个对象，包括对象名称和对象类型 实例化：使用关键字new来创建一个对象 初始化：使用new创建对象时，会调用构造方法初始化对象
      /* 通过方法来设定age */
      myPuppy.setAge( 2 );
      /* 调用另一个方法获取age */
      myPuppy.getAge( );
      /*你也可以像下面这样访问成员变量 */
      System.out.println("Variable Value :" + myPuppy.puppyAge ); 
   }
}
```
## import

Employee.java
```
import java.io.*;  //下面的命令行将会命令编译器载入java_installation/java/io路径下的所有类
public class Employee{
   //salary是静态的私有变量
   private static double salary;
   // DEPARTMENT是一个常量
   public static final String DEPARTMENT = "Development ";
   public static void main(String args[]){
      salary = 1000;
      System.out.println(DEPARTMENT+"average salary:"+salary);
   }
}
```

EmployeeTest.java
```
import java.io.*;
public class EmployeeTest{

   public static void main(String args[]){
      /* 使用构造器创建两个对象 */
      Employee empOne = new Employee("James Smith");
      Employee empTwo = new Employee("Mary Anne");

      // 调用这两个对象的成员方法
      empOne.empAge(26);
      empOne.empDesignation("Senior Software Engineer");
      empOne.empSalary(1000);
      empOne.printEmployee();

      empTwo.empAge(21);
      empTwo.empDesignation("Software Engineer");
      empTwo.empSalary(500);
      empTwo.printEmployee();
   }
}
```
编译后，执行EmployeeTest就可以得到结果
