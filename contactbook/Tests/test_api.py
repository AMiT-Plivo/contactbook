import unittest
from contact_api import ContactApi


class ModelTestCase(unittest.TestCase):
    """Test suite for contact model."""
    id = -1

    def setUp(self):
        """Setup for test"""
        self.mobile = 123456789
        self.email = 'test@plivo.com'
        self.name = 'test'
        self.contact = ContactApi()

    def test_create_contact(self):
        """Testing if contact API can create an object"""

        response = self.contact.post(name=self.name, email=self.email, mobile=self.mobile)
        print('create => ', response.json())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], self.name)
        self.assertEqual(response.json()['email'], self.email)
        ModelTestCase.id = response.json()['id']

    def test_no_duplicate_email(self):
        """Testing No duplicate email"""
        # using same email id which is already created. this must fail.
        response = self.contact.post(name=self.name, email=self.email, mobile=self.mobile)
        print('check same email => ', response.json())
        self.assertEqual(response.json()['email'], ["contact with this email already exists."])

    def test_search_with_email_and_name(self):
        """Testing Search the same email and name. Must give 1 as count"""
        # using same email and name to search.
        response = self.contact.search(name=self.name, email=self.email)
        print('search => ', response.json())
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['email'], self.email)
        self.assertEqual(response.json()['results'][0]['name'], self.name)

    def test_update_contact(self):
        """Testing Update the contact"""
        # update contact name and email for same id.
        self.new_name = self.name + '_new'
        self.new_email = self.email.replace('@plivo', '_new@plivo')
        response = self.contact.update(id=ModelTestCase.id, name=self.new_name, email=self.new_email)
        print('update => ',response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][0]['email'], self.new_email)
        self.assertEqual(response.json()['results'][0]['name'], self.new_name)

    def test_delete_contact(self):
        """Testing delete the contact"""
        print('id==>', ModelTestCase.id)
        response = self.contact.delete(id=ModelTestCase.id)
        if response.status_code==204 or response.status_code==202:
            pass
        raise Exception('Deletion Unsuccessful.')


if __name__ == '__main__':
    unittest.main()