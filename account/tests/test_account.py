from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from string import printable
from random import choice

class AccountLogicTest(TestCase):
    def test_create_user(self):
        client = Client()

        # Check if account create exists
        response = client.get(reverse('account_create'))
        self.assertEquals(response.status_code, 200)

        # Complete login form and we should be redirected (302) 
        password = "".join([choice(printable[:94]) for i in range(24)])
        response = client.post(
            reverse('account_create'), 
            {
                'username' : 'admin', 
                'email' : 'email@email.com', 
                'password1' : password, 
                'password2' : password
            })
        self.assertEquals(response.status_code, 302)

        # We should have a new user
        num_users = User.objects.filter(username='admin').count()
        self.assertEquals(num_users, 1)

        # User should exist but not be authenticated
        user = User.objects.get(username='admin')
        self.assertEquals(user.is_two_factor_authenticated, False)

        # If we log in we should be redirected to the account_inactive page
        response = client.post(
            reverse('account_login'),
            {
                'username' : 'admin',
                'password' : password
            }
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('account_inactive'))

        # Authenticate
        token = user.create_new_two_factor_token()
        response = client.get(reverse('account_two_factor_authenticate'), 
        {
            'username':'admin',
            'token': token.token
        })
        
        self.assertEquals(response.context['authenticated'], True)

        # Now if we log in we should be redirected to the profile page
        response = client.post(
            reverse('account_login'),
            {
                'username' : 'admin',
                'password' : password
            }
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('profile_detail'))


        #client.login(username='admin', password=password)
        #self.assertEquals(client.request.user.is_authenticated, True)