## 准备工作
### 安装wsl linux
1. 开启Linux子系统，以**管理员权限**打开 PowerShell
```
# 启用虚拟机平台
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
# 开启Linux子系统
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
2. 开启开发者模式，`WIN + S` 搜索 开发者设置，打开后选择 开发者模式
3. `WIN + S` 搜索 store， 打开 Microsoft Store（微软应用商店）,eg: 搜索 Ubuntu ，选择 Ubuntu 18.04 LST 进行安装
4. 待安装完成后，从应用中打开 Ubuntu 18.04 LST

### 安装docker
实际上是在Win10中安装Docker桌面服务，Linux子系统中安装客户端，连接Win10上的Docker服务，进行操作

在Ubuntu子系统中安装Docker
```
# 更新apt包管理列表
sudo apt-get update -y

# 安装依赖包
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# 加入Docker官方PGP公钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 确认指纹
sudo apt-key fingerprint 0EBFCD88

# 将stable（稳定版）Docker加入apt源中
#
# If you want to live on the edge, you can change "stable" below to "test" or
# "nightly". I highly recommend sticking with stable!
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# 更新apt包管理列表
sudo apt-get update -y

# 安装Docker CE最新版本
sudo apt-get install -y docker-ce

# 允许当前用户访问Docker CLI，不必使用root
sudo usermod -aG docker $USER

# 此时执行 docker version 会提示如下错误：
# Cannot connect to the Docker daemon at unix:///var/run/docker.sock.

# 配置Windows Docker服务地址 （Settings => General => Expose daemon on tcp://localhost:2375 without TLS）
echo "export DOCKER_HOST=localhost:2375" >> ~/.bashrc  
# 使配置生效
. ~/.bashrc
```
### powershell其他操作
使用管理员模式，打开PowerShell
```
启动停止 wsl 服务
# 停止子系统服务
net stop LxssManager
# 启动子系统服务
net start LxssManager
```
备份恢复，导出、导入子系统
```
# d:\Ubuntu-18.04.tar 导出文件路径
wsl --export Ubuntu-18.04 d:\Ubuntu-18.04.tar
# d:\wsl\u18.04 子系统导入后的安装路径
wsl --import Ubuntu-18.04 d:\wsl\u18.04 d:\Ubuntu-18.04.tar
```
