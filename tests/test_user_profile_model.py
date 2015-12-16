# from django.test import TestCase
import unittest
from faker import Factory
from django.db import IntegrityError

from app.models.user import User, UserAuthentication

fake = Factory.create()


class TestUserProfileModel(unittest.TestCase):

    def setUp(self):
        self.email = fake.email()
        self.username = fake.user_name()
        self.password = fake.password()
        self.user_type = 1
        self.user = User.create_userprofile(username=self.username, user_type=self.user_type, email=self.email, password=self.password)


    def tearDown(self):
        del self.user

    def test_get_email_method(self):
        self.assertTrue(isinstance(self.user, UserAuthentication))
        self.assertEqual(self.user.get_email(), '{}'.format(self.email))

    def test_user_creation_fails_when_username_is_the_same(self):
        email = fake.email()
        with self.assertRaises(IntegrityError):
            user = User.create_userprofile(username=self.username, user_type=self.user_type, email=email, password=self.password)
            del user

    def test_user_creation_fails_when_username_is_the_same_diff_case(self):
        """
        Testing for case insensitivity.
        Checks for IntegrityErrors when username of same value (but different alphabet case)
        is used.
        """
        email = fake.email()
        with self.assertRaises(IntegrityError):
            user = User.create_userprofile(username=self.username.upper(), user_type=self.user_type, email=email, password=self.password)
            del user

    def test_user_creation_fails_when_email_is_the_same(self):
        username = fake.user_name()
        with self.assertRaises(IntegrityError):
            user = User.create_userprofile(username=username,  user_type=self.user_type, email=self.email, password=self.password)
            del user

    def test_user_creation_fails_when_email_is_the_same_diff_case(self):
        """
        Testing for case insensitivity.
        Checks for IntegrityErrors when email of same value (but different alphabet case)
        is used.
        """
        username = fake.user_name()
        with self.assertRaises(IntegrityError):
            user = User.create_userprofile(username=username,  user_type=self.user_type, email=self.email.upper(), password=self.password)
            del user

    def test_user_creation_fails_when_email_and_username_is_the_same(self):
        with self.assertRaises(IntegrityError):
            user_profile = User.create_userprofile(username=self.username,  user_type=self.user_type, email=self.email, password=self.password)
            del user_profile

    def test_user_creation_fails_when_email_and_username_is_the_same_diff_case(self):
        """
        Testing for case insensitivity.
        Checks for IntegrityErrors when email and username of same value (but different alphabet case)
        is used.
        """
        with self.assertRaises(IntegrityError):
            user_profile = User.create_userprofile(username=self.username.upper(),  user_type=self.user_type, email=self.email.upper(), password=self.password)
            del user_profile

    def test_user_creation_succeeds_when_correct_data_is_passed(self):
        email = fake.email()
        password = fake.password()
        username = fake.user_name()
        user = User.create_userprofile(username=username,  user_type=self.user_type, email=email, password=password)
        self.assertTrue(isinstance(user, UserAuthentication))
        self.assertEqual(isinstance(user, UserAuthentication), isinstance(self.user, UserAuthentication))
        del user
