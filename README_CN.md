Engish [here](README.md)
# GitHubStar
Git Star自动点赞工具
# 快速开始 ( 针对 Linux 用户 )
1. 执行```git clone https://github.com/w568w/GitHubStar.git && cd GitHubStar/executable/dist/main/```。  
2. 打开```user```文件，替换以下内容（括号内不用输入）  
```
w568w（GitStar用户名）
123456（GitStar密码）
w568w（GitHub用户名）
123456（GitHub密码）
（最后一行有个换行，请勿删除）
```
3. 执行```./main &lt; user```，完事儿！
# 编译
## Linux
### Step1
安装python2.x

安装pip, 从 这里下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)

接着运行:

> python get-pip.py

安装依赖

> pip install -r requirements.txt

### Step2
打开```settings.py```,替换以下内容  
```
#############settings#############
NAME		= "1" #GitStar用户名
PASSWORD	= "1" #GitStar密码
GITNAME		= "1" #github用户名
GITPASSWORD	= "1" #github密码
#############settings#############
```
把它们改成你自己的信息。  
### Step3
运行```python -u main.py```,  
完事儿！
## Windows
我好久没用过Windows了~    
你可以百度一下```windows python2.x安装教程```看看，祝你好运！:)
