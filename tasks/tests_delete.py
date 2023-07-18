from django.test import TestCase
from .models import Task
from django.urls import reverse

# Create your tests here.
class IndexTestCase(TestCase):
    def setUp(self): # the naming is like this because the code otherwise does not work. 
        self.url = reverse('index')
        self.task_data = {'title': 'Do dishes'}
        Task.objects.create(title="Walking the dog", completed=False) 
        Task.objects.create(title="Work on plan for world domination")


    def test_delete_get_method(self):
        world_domination = Task.objects.get(title="Work on plan for world domination")
        url = reverse('delete', args=[world_domination.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Assert that the template used is 'tasks/home.html'
        self.assertTemplateUsed(response, 'tasks/home.html')

        # Check that the form in the context is bound to the existing task's data
        form = response.context['form']
        self.assertEqual(form.instance, world_domination)


    def test_delete_post_method(self):
        walk_dog = Task.objects.get(title="Walking the dog")

        url = reverse('delete', args=[walk_dog.pk])
        response = self.client.post(url)

        # Assert whether the deleted object doesn't exist in the database. 
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=walk_dog.pk)