from django.test import TestCase
from rest_framework.test import APIRequestFactory
# Create your tests here.

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.get('/api/invoice/')
request = factory.get('/api/invoice/<pk>/')
request = factory.post('/api/invoice/', {
    "customer_name": "latika",
    "desc": "I want momos, spring rolls",
    "quantity": 5,
    "unit_price": 60
})
request = factory.put('/api/invoice/', {'title': 'new idea'})
request = factory.patch('/api/invoice/', {'title': 'new idea'})

request = factory.delete('/api/invoice/<pk>/', {'title': 'new idea'})