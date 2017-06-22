from django.conf.urls import url

from DjangoTaskManager.task import views

urlpatterns = [
    url(r'^$', views.all_tasks, name='all_tasks'),
    url(r'^add/$', views.add, name='task_add'),
    url(r'^mark-done/(?P<task_id>[\w+:-]+)/$',
        views.mark_done, name='task_mark_done'),
    url(r'^edit/(?P<task_id>[\w+:-]+)/$',
        views.edit, name='task_edit'),
    url(r'^delete/(?P<task_id>[\w+:-]+)/$',
        views.delete, name='task_delete'),
    url(r'^single/(?P<task_id>[\w+:-]+)/$',
        views.single, name='single_task'),
]
