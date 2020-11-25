from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'polls'

urlpatterns = [

    path('', views.index, name='index'),

    path('<int:poll_id>/', views.detail, name='detail'),

    path('<int:id>/vote/', login_required(views.vote), name='vote'),

]



