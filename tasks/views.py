from django.shortcuts import render, redirect
from .models import Task, DeletedTask
from .forms import taskForm

"""
This part of the app renders the homepage while it also takes care 
of the functionality of adding new tasks when a post is made. 
"""
def index(request):
    tasks = Task.objects.all()
    form = taskForm()
    deleteTask = DeletedTask.objects.all()

    if request.method == "POST":
        # Passing the response into the form class. 
        form = taskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task = Task(title=title)
            task.save()
        
        # At the end of this function, the idea is to return to the same url-path as before. 
        return redirect('/')

    context = {"tasks": tasks, "form": form, "deleteTask": deleteTask}
    return render(request, 'tasks/home.html', context)

"""
This function takes care of the update functionality of a task. If the update button is clicked,
this function will be activated, causing the user to redirect to another page where the updating
can be done. 

Improvement point: updated tasks now show up in both the todo part and the completed part. Have
not thought of a way on how solve this. 
"""
def update(request, pk):
    # This part uses the pk to grab the specific item which needs to be updated. 
    task = Task.objects.get(id=pk)
    form = taskForm(instance=task)
    if request.method == "POST":
        # This way, you can process the POST request but it will allow you to update
        # the specific task which has to be updated.
        form = taskForm(request.POST, instance=task) 

        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'tasks/update.html', context)

"""
Takes care of deleting a task. When the delete button is clicked, the task will 
immediately be removed and displayed in the list of deleted tasks. 
"""
def delete(request, pk):
    task = Task.objects.get(id=pk)
    form = taskForm(instance=task)

    #I want to have the deleted items inside of a separate database.
    deleteTask = DeletedTask.objects.all()

    if request.method == "POST":
        task_title = task.title
        task.delete()
        deleted_task = DeletedTask(title=task_title)
        deleted_task.save()

        return redirect('/')

    context = {'form': form, "deleteTask": deleteTask}
    return render(request, 'tasks/home.html', context)