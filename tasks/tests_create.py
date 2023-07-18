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


    def test_objects_filled_in_correctly(self):
        walk_dog = Task.objects.get(title="Walking the dog")
        self.assertEqual(walk_dog.completed, False)


    def test_index_get_method(self):
        world_domination = Task.objects.get(title="Work on plan for world domination")

        # The next part tests whether the url sent sends the right information (which is in the database). 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200) #Just asserts whether the get method was successful. 

        response_elements = response.context['tasks']
        self.assertQuerysetEqual(response_elements.get(title="Work on plan for world domination").title, world_domination.title)


    def test_index_view_post(self):
        response = self.client.post(self.url, data=self.task_data)
        tasks = Task.objects.filter(title=self.task_data['title'])

        # Like with the previous request, it checks whether the post method was successful. 302 means redirect. 
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.url)

        # There should only be 1 task with this specific title inside of the database. 
        self.assertEqual(tasks.count(), 1)


    