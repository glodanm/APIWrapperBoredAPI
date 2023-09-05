from django.test import TestCase
from rest_framework.test import APIClient
from .models import Activity
from rest_framework import status
from .serializers import ActivitySerializer


class ActivityModelTest(TestCase):

    def setUp(self):
        self.activity1 = Activity.objects.create(
            activity="Test Activity 1",
            type="Test Type 1",
            participants=4,
            price="0.5",
            accessibility="0.75",
            link="https://example.com"
        )
        self.activity2 = Activity.objects.create(
            activity="Test Activity 2",
            type="Test Type 2",
            participants=2,
            price="0.8",
            accessibility="0.50",
            link="https://example.com",
        )
    
    def test_model_creation(self):
        saved_activity = Activity.objects.get(activity="Test Activity 1")
        self.assertEqual(saved_activity.type, "Test Type 1")
        self.assertEqual(saved_activity.participants, 4)
        self.assertEqual(saved_activity.price, 0.5)
        self.assertEqual(saved_activity.accessibility, 0.75)
        self.assertEqual(saved_activity.link, "https://example.com")
    
    def test_activity_str_representation(self):
        self.assertEqual(str(self.activity1), "Test Activity 1")

    def test_filter_by_activity_type(self):
        url = '/api/activities/'  
        response = self.client.get(url, {'type': 'Test Type 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['activity'], 'Test Activity 1')

    def test_filter_by_participants(self):
        url = '/api/activities/'
        response = self.client.get(url, {'participants': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['activity'], 'Test Activity 2')

    def test_filter_by_minprice(self):
        url = '/api/activities/'
        response = self.client.get(url, {'minprice': '0.8'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['activity'], 'Test Activity 2')

    def test_filter_by_maxprice(self):
        url = '/api/activities/'
        response = self.client.get(url, {'maxprice': '0.5'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['activity'], 'Test Activity 1')

    def test_filter_by_minaccessibility(self):
        url = '/api/activities/'
        response = self.client.get(url, {'minaccessibility': '0.75'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['activity'], 'Test Activity 1')

    def test_filter_by_maxaccessibility(self):
        url = '/api/activities/'
        response = self.client.get(url, {'maxaccessibility': '0.5'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['activity'], 'Test Activity 2')

    def test_empty_query(self):
        url = '/api/activities/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
