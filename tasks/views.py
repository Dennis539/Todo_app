from django.shortcuts import render, redirect
from .models import Task, DeletedTask
from .forms import taskForm


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