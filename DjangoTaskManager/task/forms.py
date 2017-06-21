from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, Form

from DjangoTaskManager.task.models import Task


class AddTaskForm(Form):
    assignee = CharField(required=True)
    description = CharField(required=False)
    name = CharField(required=True)

    def clean_assignee(self):
        assignee = self.cleaned_data.get('assignee')
        try:
            return User.objects.get(username=assignee)
        except User.DoesNotExist:
            raise ValidationError('Assignee does not exist')


class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
        'assignee',
        'name',
        'description']
