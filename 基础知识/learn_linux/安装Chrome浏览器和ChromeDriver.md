## 一、 安装Chrome浏览器
1、安装依赖

`sudo apt-get install libxss1 libappindicator1 libindicator7`

2、下载Chrome安装包 (最新稳定版)

`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`

3、安装

```
sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
```

## 二、安装ChromeDriver
1、安装xvfb以便我们可以无头奔跑地运行Chrome

`sudo apt-get install xvfb`

2、安装依赖

`sudo apt-get install unzip`

3、下载安装包

`wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip`

要下载对应版本 http://chromedriver.storage.googleapis.com/index.html 

4、解压缩+添加执行权限

`unzip chromedriver_linux64.zip`

5、移动

`sudo mv -f chromedriver /usr/local/share/chromedriver`

6、建立软连接

`sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver`
`sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver`

## 三、无头运行Chrome
1、安装Python依赖

`pip3 install selenium`

`pip3 install pyvirtualdisplay`
