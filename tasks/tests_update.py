from django.test import TestCase
from .models import Task
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class UpdateTestCase(TestCase):
    def setUp(self):
        self.task_data = {'title': 'Do dishes'}
        Task.objects.create(title="Walking the dog", completed=False) 
        Task.objects.create(title="Work on plan for world domination")


    def test_update_get_method(self):
        world_domination = Task.objects.get(title="Work on plan for world domination")
        url = reverse('update', args=[world_domination.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Assert that the template used is 'tasks/update.html'
        self.assertTemplateUsed(response, 'tasks/update.html')

        # Check that the form in the context is bound to the existing task's data
        form = response.context['form']
        self.assertEqual(form.instance, world_domination)
    

    def test_update_post_method(self): # Test updating an existing task. 
        walk_dog = Task.objects.get(title="Walking the dog")
        update_data = {"title": "Walking the dog", "completed": True}
        update_url = reverse('update', args=[walk_dog.pk])
        response = self.client.post(update_url, data=update_data)

        self.assertEqual(response.status_code, 302) # Check whether redirect

        # Check whether update works. 
        walk_dog_updated = Task.objects.get(title="Walking the dog")
        self.assertEqual(walk_dog_updated.completed, True)