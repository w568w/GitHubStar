# -*- coding:utf-8 -*-  
import sys
import requests
import json
import traceback
from requests.auth import HTTPBasicAuth
reload(sys)
#-----------------------------
NAME="w568w"
PASSWORD="xxxx"
GITNAME="w568w"
GITPASSWORD="xxxx"
#-----------------------------
AUTH = HTTPBasicAuth(GITNAME, GITPASSWORD)
sys.setdefaultencoding('utf-8')
def loginGitStar():
	global NAME
	global PASSWORD
	r=requests.post("http://gitstar.top:88/api/user/login",params={'username':NAME,'password':PASSWORD})
	return r.headers['Set-Cookie']
def getGitStarList():
	global NAME
	cookie=loginGitStar()
	url="http://gitstar.top:88/api/users/{}/status/recommend".format("admin")
	response = requests.get(url,headers={'Accept': 'application/json','Cookie':cookie})
	jsn=response.json()
	list=[]
	for obj in jsn:
		list.append(obj['Repo'])
	return list
def star(url):
	global AUTH
	requests.put("https://api.github.com/user/starred/"+url
		,headers={'Content-Length': '0'}
		,auth=AUTH)

StarList=getGitStarList()
for url in StarList:
	star(url)
	print "Stared! -->{}".format(url)
