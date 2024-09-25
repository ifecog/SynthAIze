from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class UserModelTesT(TestCase):
    
    def test_create_synthesist_without_bio(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='synthesist@test.com',
                password='pAssw0rd',
                role='Synthesist'
            )
            
            
    def test_create_synthesist_with_bio(self):
        user = User.objects.create_user(
            email='synthesist@test.com',
            password='pAssw0rd',
            role='Synthesist',
            bio='I am a Synthesist.'
        )
        
        self.assertEqual(user.email, 'synthesist@test.com')
        self.assertEqual(user.role, 'Synthesist')
        self.assertEqual(user.bio, 'I am a Synthesist.')
        
        
    def test_create_observer(self):
        user = User.objects.create_user(
            email="observer@test.com",
            password="password123",
            role="Observer",
        )
        self.assertEqual(user.email, "observer@test.com")
        self.assertEqual(user.role, "Observer")
        self.assertIsNone(user.bio)  # bio should be None since it's optional for Observer

    def test_create_admin(self):
        user = User.objects.create_user(
            email="admin@test.com",
            password="password123",
            role="Admin",
        )
        self.assertEqual(user.email, "admin@test.com")
        self.assertEqual(user.role, "Admin")
        self.assertIsNone(user.bio)