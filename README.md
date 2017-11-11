Chinese [here](README_CN.md)
# GitHubStar
Auto star for gitstar.cn
## Installation
Install Python 2.x,run```python --version```and```pip```for a test.  

To install pip, securely download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)

Then run the following:

> python get-pip.py

If you have downloaded it,skip the step.  
MAKE SURE that you have installed ```requests```.
> pip install -r requirements.txt

## Usage
### Step 1
Clone the repo  
```git clone https://github.com/weilaihui/GitHubStar.git && cd GitHubStar```

### Step 2
Open```settings.py```, replace variables with your own infomation.
```
#############settings#############
NAME		= "1" #GitStar username
PASSWORD	= "1" #GitStar password
GITNAME		= "1" #Gitee username
GITPASSWORD	= "1" #Gitee password
#############settings#############
```
### Step 3
Run```python -u main.py```  
Everything is ok,hooray!
