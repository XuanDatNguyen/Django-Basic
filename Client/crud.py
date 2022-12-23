import requests
from requests.auth import HTTPBasicAuth

base_url = "http://localhost:8000"
uname = "admin"
pwd = 123456


def get_posts():
    url = F"{base_url}/posts"
    res = requests.get(url, auth=HTTPBasicAuth(username=uname, password=pwd))
    return res.text
# print(get_posts())


def create_post(body):
    url = F"{base_url}/posts/"
    res = requests.post(url, auth=HTTPBasicAuth(
        username=uname, password=pwd), json=body)
    return res.text
# print(create_post({"title": "Bài viết test", "description": "Nội dung test"}))


def update_post(post_id, body):
    url = F"{base_url}/posts/{post_id}"
    res = requests.put(url, auth=HTTPBasicAuth(
        username=uname, password=pwd), json=body)
    return res.text


# print(update_post(4, {"title": "Bài viết test update",
#       "description": "Nội dung update"}))

def delete_post(post_id):
    url = F"{base_url}/posts/{post_id}"
    res = requests.delete(url, auth=HTTPBasicAuth(
        username=uname, password=pwd))
    return res.text


print(delete_post(4))
