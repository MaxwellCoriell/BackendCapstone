from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from DjangoTaskManager.task.forms import EditTaskForm
from DjangoTaskManager.task.forms import AddTaskForm
from DjangoTaskManager.task.models import Task


@login_required
def all_tasks(request):
    """
    Purpose: this displays all tasks created by users

    Author: Max Baldridge

    Arguments: Request -- the full HTTP request object

    Returns: all tasks created by all registered users
    """
    hide_completed = request.GET.get('hide_completed', False)
    tasks = Task.objects.all()
    if hide_completed:
        tasks = tasks.filter(completed=False)

    return TemplateResponse(request, 'tasks.html', {
        'tasks': tasks
    })


@login_required
def add(request):
    """
    Purpose: to present the user with a form to upload information about a task to complete

    Author: Max Baldridge

    Arguments: Request -- the full HTTP request object

    Returns: (TemplateResponse): A form that lets the user upload a a task to complete
    """
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            Task(
                assignee=form.cleaned_data.get('assignee'),
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                created_by=request.user
            ).save()
            return HttpResponseRedirect(reverse('all_tasks'))
        else:
            return TemplateResponse(request, 'edit_task.html', {'errors': form.errors})
    else:
        return TemplateResponse(request, 'edit_task.html', {})


@login_required
def mark_done(request, task_id):
    """
     Purpose: Allows user to mark a task as completed, whether editing it,
     or viewing it in the complete list of tasks.
     Checks to see if a specific task id appears, 
     and if it does to complete the task.
     If no id is found for the task, the raises a 404 [not found] error

     Author: Max Baldridge

     Arguments: Request -- the full HTTP request object
                task_id: (integer): id of task we are marking as complete

     Returns: (HttpResponseRedirect):
        the view of all tasks, with the current task as all
     """
    try:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save(update_fields=['completed'])
    except Task.DoesNotExist:
        raise Http404

    return HttpResponseRedirect(reverse('all_tasks'))


@login_required
def edit(request, task_id):
    """
     Purpose: Allows user to view the edit view, 
     which contains a very specific view
     for editing a singular task
     For an example, visit /edit/1/ to see a view on the first task created
     displaying title, description, assignee, and whether or not it's been completed. 

     Author: Max Baldridge 

     Arguments: Request -- the full HTTP request object
                task_id: (integer): id of task we are editing

     Returns: (render): a view of the request, template to use, and product obj
     """
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404

    form = EditTaskForm(instance=task)
    return TemplateResponse(
        request,
        'edit_task.html',
        {'form': form, 'edit': True})


@login_required
def delete(request, task_id):
    """
     Purpose: Allows user to delete a single task,
     thus removing it from the list of all user tasks.

     Author: Max Baldridge

     Arguments: Request -- the full HTTP request object
                task_id: (integer): id of task we are removing

     Returns: (render): a view of the request, template to use, and product obj
     """
    try:
        Task.objects.get(id=task_id).delete()
    except Task.DoesNotExist:
        raise Http404

    return HttpResponseRedirect(reverse('all_tasks'))
