import os.path
import unittest

import requests_mock

import tpm


api_url = 'https://tpm.example.com/index.php/api/v6/'


class ClientV6TestCase(unittest.TestCase):
    def setUp(self):
        self.client = tpm.TpmApiv6('https://tpm.example.com', username='USER', password='PASS')

    def test_function_list_projects_all(self):
        request_url = api_url + 'projects/all.json'
        return_data = [{'id': 1, 'name': 'all-project'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_projects_all()
        self.assertEqual(response, return_data)

    def test_function_list_passwords_all(self):
        request_url = api_url + 'passwords/all.json'
        return_data = [{'id': 1, 'name': 'all-password'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_passwords_all()
        self.assertEqual(response, return_data)

    def test_function_copy_password(self):
        request_url = api_url + 'passwords/14/copy.json'
        with requests_mock.Mocker() as m:
            m.post(request_url, json={'id': 140})
            response = self.client.copy_password('14', '5')
        self.assertEqual(response, 140)

    def test_function_duplicate_password(self):
        request_url = api_url + 'passwords/14/duplicate.json'
        with requests_mock.Mocker() as m:
            m.post(request_url, json={'id': 141})
            response = self.client.duplicate_password('14', 'copy of password')
        self.assertEqual(response, 141)

    def test_function_list_users_search(self):
        request_url = api_url + 'users/search/Alan.json'
        return_data = [{'id': 6, 'name': 'Alan Hall'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_users_search('Alan')
        self.assertEqual(response, return_data)

    def test_function_list_passwords_of_user(self):
        request_url = api_url + 'users/1/passwords.json'
        return_data = [{'id': 15, 'name': 'wordpress'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_passwords_of_user('1')
        self.assertEqual(response, return_data)

    def test_function_list_projects_of_user(self):
        request_url = api_url + 'users/1/projects.json'
        return_data = [{'id': 5, 'name': 'Company projects'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_projects_of_user('1')
        self.assertEqual(response, return_data)

    def test_function_list_mypasswords_archived(self):
        request_url = api_url + 'my_passwords/archived.json'
        return_data = [{'id': 4, 'archived': True}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_mypasswords_archived()
        self.assertEqual(response, return_data)

    def test_function_list_mypasswords_favorite(self):
        request_url = api_url + 'my_passwords/favorite.json'
        return_data = [{'id': 2, 'favorite': True}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_mypasswords_favorite()
        self.assertEqual(response, return_data)

    def test_function_update_custom_fields_of_mypassword(self):
        request_url = api_url + 'my_passwords/4/custom_fields.json'
        with requests_mock.Mocker() as m:
            m.put(request_url, status_code=204)
            response = self.client.update_custom_fields_of_mypassword('4', {'custom_type1': 'text'})
        self.assertEqual(response, None)

    def test_function_archive_mypassword(self):
        request_url = api_url + 'my_passwords/4/archive.json'
        with requests_mock.Mocker() as m:
            m.put(request_url, status_code=204)
            response = self.client.archive_mypassword('4')
        self.assertEqual(response, None)

    def test_function_unarchive_mypassword(self):
        request_url = api_url + 'my_passwords/4/unarchive.json'
        with requests_mock.Mocker() as m:
            m.put(request_url, status_code=204)
            response = self.client.unarchive_mypassword('4')
        self.assertEqual(response, None)

    def test_function_list_mypassword_files(self):
        request_url = api_url + 'my_passwords/4/files.json'
        return_data = [{'id': 10, 'filename': 'evidence.txt'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_mypassword_files('4')
        self.assertEqual(response, return_data)

    def test_function_upload_mypassword_file(self):
        request_url = api_url + 'my_passwords/4/upload.json'
        file_path = os.path.normpath('tests/resources/projects/4/upload.json')
        with requests_mock.Mocker() as m:
            m.post(request_url, json={'id': 11})
            response = self.client.upload_mypassword_file('4', file_path, notes='doc')
        self.assertEqual(response, 11)

    def test_function_copy_mypassword(self):
        request_url = api_url + 'my_passwords/4/copy.json'
        with requests_mock.Mocker() as m:
            m.post(request_url, json={'id': 120})
            response = self.client.copy_mypassword('4', '5')
        self.assertEqual(response, 120)

    def test_function_duplicate_mypassword(self):
        request_url = api_url + 'my_passwords/4/duplicate.json'
        with requests_mock.Mocker() as m:
            m.post(request_url, json={'id': 121})
            response = self.client.duplicate_mypassword('4', 'copy of my password')
        self.assertEqual(response, 121)

    def test_function_set_favorite_mypassword(self):
        request_url = api_url + 'favorite_my_passwords/4.json'
        with requests_mock.Mocker() as m:
            m.post(request_url, status_code=204)
            response = self.client.set_favorite_mypassword('4')
        self.assertEqual(response, None)

    def test_function_unset_favorite_mypassword(self):
        request_url = api_url + 'favorite_my_passwords/4.json'
        with requests_mock.Mocker() as m:
            m.delete(request_url, status_code=204)
            response = self.client.unset_favorite_mypassword('4')
        self.assertEqual(response, None)

    def test_function_set_favorite_project(self):
        request_url = api_url + 'favorite_projects/4.json'
        with requests_mock.Mocker() as m:
            m.post(request_url, status_code=204)
            response = self.client.set_favorite_project('4')
        self.assertEqual(response, None)

    def test_function_unset_favorite_project(self):
        request_url = api_url + 'favorite_projects/4.json'
        with requests_mock.Mocker() as m:
            m.delete(request_url, status_code=204)
            response = self.client.unset_favorite_project('4')
        self.assertEqual(response, None)

    def test_function_list_log(self):
        request_url = api_url + 'log.json'
        return_data = [{'id': 510396, 'origin': 'web'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_log()
        self.assertEqual(response, return_data)

    def test_function_search_log(self):
        request_url = api_url + 'log/search/action_id%3Aview_password.json'
        return_data = [{'id': 510392, 'origin': 'api'}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.search_log('action_id:view_password')
        self.assertEqual(response, return_data)

    def test_v6_metadata_header(self):
        request_url = api_url + 'passwords.json'
        return_data = [{'id': 68}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_passwords(metadata_only=True)
            history = m.request_history
        self.assertEqual(response, return_data)
        self.assertEqual(history[0].headers.get('X-Metadata-Only'), 'true')

    def test_v6_permissions_header(self):
        request_url = api_url + 'projects.json'
        return_data = [{'id': 18}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_projects(permissions=True)
            history = m.request_history
        self.assertEqual(response, return_data)
        self.assertEqual(history[0].headers.get('X-Permissions'), 'true')

    def test_v6_page_size_header(self):
        request_url = api_url + 'log.json'
        return_data = [{'id': 1}]
        with requests_mock.Mocker() as m:
            m.get(request_url, json=return_data)
            response = self.client.list_log(page_size=10)
            history = m.request_history
        self.assertEqual(response, return_data)
        self.assertEqual(history[0].headers.get('X-Page-Size'), '10')


if __name__ == '__main__':
    unittest.main()
