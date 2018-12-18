import requests
import json

local_token = 'f9ca5cbb5d1972e7343152ab27cbe5950a93c693'
token_aws = '9ec887751893e44f37e06e151c8f6042d2dcdd09'
token = token_aws

aws_url = 'http://13.232.5.70:8000'
local_url = 'http://127.0.0.1:8000'
base_url = aws_url


class ContactApi(object):
    def __init__(self):
        self.base_url = base_url + '/contact/'
        self.page_url = base_url + '/contact/?page={}'
        self.search_url = base_url + '/contact/?name={name}&email={email}'
        self.delete_url = base_url + '/contact/{}/'
        self.update_url = base_url + '/contact/{}/'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': 'Token ' + token}

    def get(self):
        response = requests.get(url=self.base_url, headers=self.headers)
        return response

    def search(self, name='', email=''):
        search_url = self.search_url.format(**{'name': name, 'email': email})
        response = requests.get(url=search_url, headers=self.headers)
        return response

    def post(self, name, email, mobile):
        data = {"name": name, "email": email, "mobile": mobile}
        payload = json.dumps(data)
        response = requests.post(url=self.base_url, data=payload, headers=self.headers)
        return response

    def update(self, id, name=None, email=None, mobile=None):
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email
        if mobile:
            data["mobile"] = mobile

        payload = json.dumps(data)
        response = requests.put(url=self.update_url.format(id), data=payload, headers=self.headers)
        return response

    def delete(self, id):
        response = requests.delete(url=self.delete_url.format(id), headers=self.headers)
        return response

    def navigate_page(self, page):
        response = requests.get(self.page_url.format(page), headers=self.headers)
        return response


