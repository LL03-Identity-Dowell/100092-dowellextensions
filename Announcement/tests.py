import json
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from .views import AnnouncementDetail


class AnnouncementListTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_announcements(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/announcements/')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.content)
        self.assertIsInstance(response_json, dict)

    def test_create_announcement(self):
        data = {
            "description": "test hello",
            "product": "test workflow",
            "created_by": "booz",
            "member_type": "Public",
            "company_id": "jhgy67",
            "created_at_position": "admin"
        }
        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/announcements/', data)
        self.assertEqual(response.status_code, 201)
        response_json = json.loads(response.content)

    def test_create_invalid_announcement(self):
        invalid_data = {
            "description": "Hello World3",
            "product": "WorkFlow3",
            "created_by": "fazzie3",
            "company_id": "sdf2334",
            "created_at_position": "admin"
        }
        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/announcements/', invalid_data)
        self.assertEqual(response.status_code, 400)
        response_json = json.loads(response.content)


class AnnouncementDetailTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_announcement(self):
        request = self.factory.get(
            'http://127.0.0.1:8000/api/v1/announcements/648bff82e7a9fca150a72618')

        response = AnnouncementDetail.as_view()(request, id="648bff82e7a9fca150a72618")
        self.assertEqual(response.status_code, 200)

        expected_data = {'isSuccess': True, 'data': [{'_id': '648bff82e7a9fca150a72618', 'eventId': {'is_success': True, 'event_id': 'FB1010000000000000000000003004', 'inserted_id': '648bff7f2a2b476e2c3b78fe'}, 'announcement': {
            'member_type': 'Public', 'description': 'New description', 'product': 'test workflow', 'created_by': 'booz', 'is_active': False, 'company_id': 'jhgy67', 'created_at_position': 'admin', 'created_at': '2023-06-16T06:21:50.023537', 'is_Active': False}}]}
        self.assertEqual(response.data, expected_data)

    def test_get_announcement_fail(self):
        request = self.factory.get(
            'http://127.0.0.1:8000/api/v1/announcements/648bff82e7a9fca150a72622')

        response = AnnouncementDetail.as_view()(request, id="648bff82e7a9fca150a72622")
        self.assertEqual(response.status_code, 200)

        expected_data = {'isSuccess': True, 'data': []}
        self.assertEqual(response.data, expected_data)

    def test_put_announcement(self):
        request = self.factory.put(
            'http://127.0.0.1:8000/api/v1/announcements/648bff82e7a9fca150a72618')

        response = AnnouncementDetail.as_view()(request, id="648bff82e7a9fca150a72618")

        self.assertEqual(response.status_code, 200)

        expected_data = {
            "isSuccess": True
        }
        self.assertEqual(response.data, expected_data)

    def test_patch_announcement(self):

        request_data = {
            'description': 'New description',
        }
        request = self.factory.patch(
            'http://127.0.0.1:8000/api/v1/announcements/648bff82e7a9fca150a72618', data=request_data, format='json')

        response = AnnouncementDetail.as_view()(request, id="648bff82e7a9fca150a72618")

        self.assertEqual(response.status_code, 200)

        expected_data = {
            "isSuccess": True
        }
        self.assertEqual(response.data, expected_data)
