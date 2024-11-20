from django.urls import path
from . import views

app_name = 'forms_app'
urlpatterns = [
    path("lead-creation/", views.lead_creation,name='lead_creation'),
]
