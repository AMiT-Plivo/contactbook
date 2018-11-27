import requests
import json

token = 'f9ca5cbb5d1972e7343152ab27cbe5950a93c693'


class ContactApi(object):
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8000/contact/'
        self.page_url = 'http://127.0.0.1:8000/contact/?page={}'
        self.search_url = 'http://127.0.0.1:8000/contact/?name={name}&email={email}'
        self.delete_url = 'http://127.0.0.1:8000/contact/{}/'
        self.update_url = 'http://127.0.0.1:8000/contact/{}/'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': 'Token ' + token}

    def get(self):
        r = requests.get(url=self.base_url, headers=self.headers)
        return r.json()

    def search(self, name='', email=''):
        search_url = self.search_url.format(**{'name': name, 'email': email})
        r = requests.get(url=search_url, headers=self.headers)
        return r.json()

    def post(self, name, email, mobile):
        data = {"name": name, "email": email, "mobile": mobile}
        payload = json.dumps(data)
        r = requests.post(url=self.base_url, data=payload, headers=self.headers)
        return r.json()

    def update(self, id, name=None, email=None, mobile=None):
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email
        if mobile:
            data["mobile"] = mobile

        payload = json.dumps(data)
        r = requests.put(url=self.update_url.format(id), data=payload, headers=self.headers)
        return r.json()

    def delete(self, id):
        r = requests.delete(url=self.delete_url.format(id), headers=self.headers)
        if r.status_code == 202 or r.status_code == 204:
            return 'Deletion Successful'
        return r.json()

    def navigate_page(self,page):
        r = requests.get(self.page_url.format(page), headers=self.headers)
        return r.json()


contact = ContactApi()

print('Search : ', contact.search(name='amit', email='test@plivo.com'))

print('Update : ', contact.update(15, name='amit11', email='tes22@plivo.com', mobile=1234))

print('Delete : ', contact.delete(15))

print('Post : ', contact.post(name='new11', email='new11@gmail', mobile=123452123))

print('Get All : ', contact.get())

print('Jump to Page : ', contact.navigate_page(2))
