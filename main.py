# -*- coding:utf-8 -*-  
import urllib2
import urllib
import httplib  
import sys
import re
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
reload(sys)
NAME="w568w"
PASSWORD="xd20021111"
GITNAME="w568w"
GITPASSWORD="xd20021111,./"
sys.setdefaultencoding('utf-8')
#obj = webdriver.PhantomJS("/bin/phantomjs")
print "Start WebDriver..."
# service_log_path = "{}/chromedriver.log".format("/home/w568w")
# service_args = ['--verbose']
# driver = webdriver.Chrome('/usr/bin/chromedriver',
#         service_args=service_args,
#         service_log_path=service_log_path)
binary = FirefoxBinary('/home/w568w/下载/firefox/firefox')
obj = webdriver.Firefox(executable_path="/bin/geckodriver",firefox_binary=binary)
print "OK"
def loginGitStar():
	global NAME
	global PASSWORD
	obj.get("http://gitstar.top:88/login")
	obj.find_element_by_id("username").send_keys(NAME)
	obj.find_element_by_id("password").send_keys(PASSWORD)
	obj.find_element_by_css_selector(".btn").submit()

def loginGitHub():
	global GITNAME
	global GITPASSWORD
	obj.get("https://github.com/login")
	obj.find_element_by_css_selector("#login_field").send_keys(GITNAME)
	obj.find_element_by_id("password").send_keys(GITPASSWORD)
	obj.find_element_by_css_selector(".btn").submit()
def getGitStarList():
	list=obj.find_elements_by_class_name("media")
	print "List length-->{}".format(len(list))
	ll=[]
	for l in list:
		try:
			ll.append(l.find_element_by_tag_name("a").get_attribute("href"))
		except Exception as e:
			#print traceback.format_exc()
			pass
	return ll
def star(url):
	obj.get(url)
	#
	try:
		obj.find_element_by_css_selector(".unstarred > button:nth-child(2)").click()
		time.sleep(1)
	except Exception as e:
		print traceback.format_exc()
def updateList():
	obj.get("http://gitstar.top:88/")
	obj.find_element_by_id("update").click()

print "Login Github..."
loginGitHub()
print "OK"
time.sleep(3)
print "Login GitStar..."
loginGitStar()
print "OK"
time.sleep(3)
updateList()
print "Get GitStar List..."
StarList=getGitStarList()
for url in StarList:
	print "Start Star! -->{}".format(url)
	star(url)
	print "Stared! -->{}".format(url)
updateList()
