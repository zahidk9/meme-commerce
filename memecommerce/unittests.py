import os
import re 
import inspect 
import tempfile 
import memecommerce.models
import uuid
from memecommerce.models import Meme
from memecommerce.models import UserProfile 
from django.contrib.auth.models import User
from memecommerce import forms
from populate_memecommerce import populate 
from django.db import models 
from django.test import TestCase
from django.conf import settings 
from django.urls import reverse, resolve
from django.forms import fields as django_fields 

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}==================={os.linesep}MEMECOMMERCE TEST FAILURE =({os.linesep}===================={os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"

def create_user_object():

    #helper function to create a user object

    user = User.objects.get_or_create(username='testuser',
                                        first_name = 'Test',
                                        last_name = 'User',
                                        email = 'test@test.com')[0]
    user.set_password('test123456')
    user.save()

    return user 

def create_meme_object():

    #helper function to create a meme object

    meme = Meme.objects.get_or_create(title='testmeme',
                                        price = 1.00,
                                        image= tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                        description='test description')
                                    
    return meme 

def create_super_user_object():
    
    #helper function to create a super user account

    return User.objects.create_superuser('admin', 'admin@test.com', 'testpassword')

def get_template(path_to_template):

    #helper function to get string representation of template files.

    f = open(path_to_template, 'r')
    template_str = ""

    for line in f:
        template_str = f"{template_str}{line}"
    
    f.close()
    return template_str

class SetUpTests(TestCase):

    #check if auth app has been specified

    def test_installed_apps(self):
        self.assertTrue('django.contrib.auth' in settings.INSTALLED_APPS)

class ModelTests(TestCase):

    def test_purchased_memes(self):
        user_profile = UserProfile.object.all()
        meme1 = Meme.objects.create(title="Meme1")
        meme2 = Meme.objects.create(title="Meme2")
        user_profile.purchased_memes.set([meme1.pk, meme2.pk])
        self.assertEqual(user.purchased_memes.count(), 2)
    #check if UserProfile model has been created correctly
    
    def test_userprofile_class(self):

        #does it exist in memecommerce.models? Are all required attributes present?

        self.assertTrue('UserProfile' in dir(memecommerce.models))

        user_profile = memecommerce.models.UserProfile()

        expected_attributes = {
            
            'user': create_user_object(),
        }

        expected_types = {
            'purchased_memes': models.fields.related.ManyToManyField,
            'user': models.fields.related.OneToOneField,
        }

        found_count = 0

        for attr in user_profile._meta.fields:
            attr_name = attr.name 

            for expected_attr_name in expected_attributes.keys():
                if expected_attr_name == attr_name:
                    found_count += 1

                    self.assertEqual(type(attr), expected_types[attr_name], f"{FAILURE_HEADER}The type of attribute for '{attr_name}' was '{type(attr)}'; we expected '{expected_types[attr_name]}'. Check your definition of the UserProfile model.{FAILURE_FOOTER}")
                    setattr(user_profile, attr_name, expected_attributes[attr_name])
            
        self.assertEqual(found_count, len(expected_attributes.keys()), f"{FAILURE_HEADER}In the UserProfile model, we found {found_count} attributes name is {attr_name}, but were expected {len(expected_attributes.keys())}. {FAILURE_FOOTER}")
        user_profile.save()

    def test_memeclass(self):

        #does it exist in memecommerce.models? Are all required attributes present?

        self.assertTrue('Meme' in dir(memecommerce.models))

        meme = memecommerce.models.Meme()

        expected_attributes = {
            'meme_id': uuid.uuid4(),
            'author': create_user_object(),
            'title' : 'testMeme',
            'price' : 1.00,
            'image' : tempfile.NamedTemporaryFile(suffix=".jpg").name,
            'description' : 'testDescription',
        }

        expected_types = {
            'meme_id': models.fields.UUIDField,
            'author': models.fields.related.ForeignKey,
            'title': models.fields.CharField,
            'price': models.fields.DecimalField,
            'image': models.fields.files.ImageField,
            'description': models.fields.TextField,
        }

        found_count = 0

        for attr in meme._meta.fields:
            attr_name = attr.name 

            for expected_attr_name in expected_attributes.keys():
                if expected_attr_name == attr_name:
                    found_count += 1

                    self.assertEqual(type(attr), expected_types[attr_name], f"{FAILURE_HEADER}The type of attribute for '{attr_name}' was '{type(attr)}'; we expected '{expected_types[attr_name]}{FAILURE_FOOTER}")
                    setattr(meme, attr_name, expected_attributes[attr_name])

        self.assertEqual(found_count, len(expected_attributes.keys()), f"{FAILURE_HEADER}In the Meme model, we found {found_count} attributes, but were expected {len(expected_attributes.keys())}.{FAILURE_FOOTER}")
        meme.save()


class LoginTests(TestCase):
    def test_login_url_exists(self):
        #check if new login view exists in the correct place, with correct name
        url = ''
        try:
            url = reverse('memecommerce:login')
        except:
            pass

        self.assertEqual(url, '/memecommerce/login/', f"{FAILURE_HEADER}Have you created the memecommerce:login URL mapping correctly?{FAILURE_FOOTER}")

    def test_login_functionality(self):
        #tests that a user can login and is then redirected to homepage
        user_object = create_user_object()

        response = self.client.post(reverse('memecommerce:login'), {'username': 'testuser', 'password': 'test123456'})

        try:
            self.assertEqual(user_object.id, int(self.client.session['_auth_user_id']), f"{FAILURE_HEADER}We attempted to log a user with an ID of {user_object.id}, but instead logged a user in with an ID of {self.client.session['_auth_user_id']}. Check login() view.{FAILURE_FOOTER}")
        except KeyError:
            self.assertTrue(False, f"{FAILURE_HEADER}When attempting to log in with your login() view, it didn't seem to log the user in. Please check your login() view implementation, and try again.{FAILURE_FOOTER}")

        self.assertEqual(response.status_code, 302, f"{FAILURE_HEADER}Testing your login functionality, logging in was successful. However, we expected a redirect; we got a status code of {response.status_code} instead. Check your login() view implementation.{FAILURE_FOOTER}")
        self.assertEqual(response.url, reverse('memecommerce:home'), f"{FAILURE_HEADER}We were not redirected to the MemeCommerce homepage after logging in. Please check your login() view implementation, and try again.{FAILURE_FOOTER}")

    def test_login_template(self):
        #does login.html exist in the right place, and does it use inheritance.
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'memecommerce')
        template_path = os.path.join(template_base_path, 'login.html')
        self.assertTrue(os.path.exists(template_path), f"{FAILURE_HEADER}We couldn't find the 'login.html' template in the 'templates/memecommerce/' directory.{FAILURE_FOOTER}")

        request = self.client.get(reverse('memecommerce:login'))
        content = request.content.decode('utf-8')


class HomeViewTests(TestCase):
    #examine behaviour of the home view and its corresponding templates
    
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('memecommerce:home'))
        self.content = self.response.content.decode()

    def test_template_filename(self):
        self.assertTemplateUsed(self.response, 'memecommerce/home.html', f"{FAILURE_HEADER}Are you using home.html for your home() view?{FAILURE_FOOTER}")

class AboutViewTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('memecommerce:about'))
        self.content = self.response.content.decode()
    
    def test_mapping_exists(self):
        #checks view has correct URL mapping
        self.assertEquals(reverse('memecommerce:about'), '/memecommerce/about/', f"{FAILURE_HEADER}URL mapping either missing or mistyped.{FAILURE_FOOTER}")

    def test_template_filename(self):
        self.assertTemplateUsed(self.response, 'memecommerce/about.html', f"{FAILURE_HEADER}Are you using about.html for your about() view?{FAILURE_FOOTER}")  