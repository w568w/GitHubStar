# GitHubStar
Auto star for gitstar.cn
# Usage
## Linux
### Step1
Download Firefox Browser 55.0.2 from [here](http://www.firefox.com.cn/download/).
### Step2
Unzip it to a folder.For me,I chose```~/下载/firefox```,the executable file is ```firefox```.
### Step3
Download geckodriver 0.18 from [here](https://github.com/mozilla/geckodriver/releases/).  
Then unzip it as well as Step2.I copied it into ```/bin/```.
### Step4
Install Python 2.x,run```python --version```and```pip```for a test.  
If you have downloaded it,just skip the step.
### Step5
Install Selenium with```sudo pip install -U selenium```.
### Step6
Open```main.py```,replace  
```
#YOUR GITSTAR NAME&PASS
#YOUR GITHUB NAME&PASS
#YOUR FIREFOX PATH
#YOUR GECKODRIVER PATH
```
### Step7
Run```python -u main.py```,  
if everything is ok,a Firefox Browser will be opened automatically,Hooray!
## Windows
I haven't use Windows for a long time.  
You can google ```windows python selenium firefox configure``` for more information.Good luck!
