from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user(
            'Joel', 'nyambok97@gmail.com', 'password@123')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'nyambok97@gmail.com')
        self.assertFalse(user.is_staff)

    def test_raise_error_when_no_username_is_applied(self):
        self.assertRaises(ValueError, User.objects.     create_user, username='',
                          email='nyambok97@gmail.com', password='password@123')
        
    def test_raises_error_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set' ):
            User.objects.create_user(
            username='', email='nyambok97@gmail.com', password='password@123')   

    def test_raise_error_when_no_email_is_applied(self):
        self.assertRaises(ValueError, User.objects.     create_user, username='Joel',
                          email='', password='password@123')
        
    def test_raises_error_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set' ):
            User.objects.create_user(
            username='Joel', email='', password='password@123')

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            username='username', email='nyambok97@gmail.com', password='password@123', 
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'nyambok97@gmail.com')
        self.assertTrue(user.is_staff)


    def test_cant_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
         User.objects.create_superuser(
            username='username', email='nyambok97@gmail.com', password='password@123', is_staff=False
        )
         
    def test_cant_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
         User.objects.create_superuser(
            username='username', email='nyambok97@gmail.com', password='password@123', is_superuser=False
        )
