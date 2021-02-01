import requests
import json
import base64


from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts,NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo



url = "http://professeurgibaud.ovh/xmlrpc.php'"
user = "admin9035"
password = "Fcgp 1ngv iUWi RA8e k3KG YqDG"


wp = Client(url,user,password)
wp.call(GetPosts())




















"""
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())

headers = {'Authorization': 'Basic ' + token.decode('utf-8')}
responce = requests.get(url , headers=header)


post = {'date': '2017-06-19T20:00:35',
        'title': 'First REST API post',
        'slug': 'rest-api-1',
        'status': 'published',
        'content': 'this is the content post',
        'author': '1',
        'excerpt': 'Exceptional post!',
        'format': 'standard'
        }

r = requests.post(url + '/posts', headers=headers, json=post)
responce = requests.post(url , headers=header, json=post)

"""


"""
user = "Gibaud"
pythonapp = "HLlC irEq aDgx 9uAc adz9 KsxV"
url = "http://professeurgibaud.ovh/"
url2 = "http://professeurgibaud.ovh/wp-admin/index.php"

token = base64.standard_b64encode(user + ':' + pythonapp)


data_string = user + ':' + pythonapp
data_bytes = data_string.encode("utf-8")

token = base64.b64encode(data_bytes)

ttoken = str(token)

headers = {'Authorization': 'Basic ' + ttoken}

post = {'date': '2017-06-19T20:00:35',
        'title': 'First REST API post',
        'slug': 'rest-api-1',
        'status': 'publish',
        'content': 'this is the content post',
        'author': '1',
        'excerpt': 'Exceptional post!',
        'format': 'standard'
        }

r = requests.post(url + '/posts', headers=headers, json=post)
print('Your post is published on ' + json.loads(r.content)['link'])
"""