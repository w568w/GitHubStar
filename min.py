# -*- coding:utf-8 -*-  
# It's tiny python.
import sys
import requests
import json
import traceback
from requests.auth import HTTPBasicAuth
reload(sys)
NAME="w568w"
PASSWORD="xxxx"
GITNAME="w568w"
GITPASSWORD="xxxx"
(lambda __print, __y, __g: [(sys.setdefaultencoding('utf-8'), [[[[(lambda __after, __sentinel, __items: __y(lambda __this: lambda: (lambda __i: [(star(url), (__print('Stared! -->{}'.format(url)), __this())[1])[1] for __g['url'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(lambda: None, [], iter(StarList)) for __g['StarList'] in [(getGitStarList())]][0] for __g['star'], star.__name__ in [(lambda url: (lambda __l: [(requests.put(('https://api.github.com/user/starred/' + __l['url']), headers={'Content-Length': '0'}, auth=AUTH), None)[1] for __l['url'] in [(url)]][0])({}), 'star')]][0] for __g['getGitStarList'], getGitStarList.__name__ in [(lambda : (lambda __l: [[[[[(lambda __after, __sentinel, __items: __y(lambda __this: lambda: (lambda __i: [(__l['list'].append(__l['obj']['Repo']), __this())[1] for __l['obj'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(lambda: __l['list'], [], iter(__l['jsn'])) for __l['list'] in [([])]][0] for __l['jsn'] in [(__l['response'].json())]][0] for __l['response'] in [(requests.get(__l['url'], headers={'Accept': 'application/json', 'Cookie': __l['cookie']}))]][0] for __l['url'] in [('http://gitstar.top:88/api/users/{}/status/recommend'.format(NAME))]][0] for __l['cookie'] in [(loginGitStar())]][0])({}), 'getGitStarList')]][0] for __g['loginGitStar'], loginGitStar.__name__ in [(lambda : (lambda __l: [__l['r'].headers['Set-Cookie'] for __l['r'] in [(requests.post('http://gitstar.top:88/api/user/login', params={'username': NAME, 'password': PASSWORD}))]][0])({}), 'loginGitStar')]][0])[1] for __g['AUTH'] in [(HTTPBasicAuth(GITNAME, GITPASSWORD))]][0])(__import__('__builtin__').__dict__['print'], (lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals())
