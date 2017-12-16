# -*- coding:utf-8 -*-  
global NAME
global PASSWORD
global GITNAME
global GITPASSWORD
import sys
import requests
import json
import traceback
import time
from requests.auth import HTTPBasicAuth
reload(sys)
sys.setdefaultencoding('utf-8')

class Gitstar():
	def __init__(self,url=""):
		self.NAME 		= raw_input("")
		self.PASSWORD 		=  raw_input("")
		self.GITNAME 		= raw_input("")
		self.GITPASSWORD 	= raw_input("")

		self.cookie = None
	def loginGitStar(self):
		r=requests.post("http://gitstar.top:88/api/user/login",params={'username':self.NAME,'password':self.PASSWORD})
		self.cookie = r.headers['Set-Cookie']
		return r.headers['Set-Cookie']
	def getGitStarList(self):
		cookie=self.loginGitStar()
		url="http://gitstar.top:88/api/users/{}/status/recommend".format(self.NAME)
		response = requests.get(url,headers={'Accept': 'application/json','Cookie':cookie})
		jsn=response.json()
		list=[]
		for obj in jsn:
			list.append(obj['Repo'])
		return list
	def star(self,url):
		global AUTH
		AUTH = HTTPBasicAuth(self.GITNAME, self.GITPASSWORD)
		res = requests.put("https://api.github.com/user/starred/"+url
			,headers={'Content-Length': '0'}
			,auth=AUTH)
	def update_gitstar(self):
		url = "http://gitstar.top:88/star_update"
		res = requests.get(url,headers={'Accept': 'application/json','Cookie':self.cookie})
		print "update:" + str(res.status_code == 200)

GS=Gitstar()
urls = GS.getGitStarList()
print "get total github repo:%d" % len(urls)
i = 1
for url in urls:
	GS.star(url)
	print "[%d]Stared! -->%s"%(i,url)
	time.sleep(1.0)
	i = i + 1
if len(urls) > 0:
	GS.update_gitstar()
