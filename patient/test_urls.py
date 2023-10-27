from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Exercise, Session


class PatientViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.exercise = Exercise.objects.create(
            name="Test Exercise", description="Test Description"
        )
        self.session = Session.objects.create(
            name="Test Session", description="Test Description"
        )

    def test_patient_exercises_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("patient-exercises"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Exercise")

    def test_patient_sessions_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("patient-sessions"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Session")

    def test_patient_login_view(self):
        response = self.client.get(reverse("patient-login"))
        self.assertEqual(response.status_code, 200)

    def test_patient_profile_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("patient-profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testuser")
