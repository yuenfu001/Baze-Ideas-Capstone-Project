from django.urls import path
from . import views
app_name="lead_management_serializer"
urlpatterns = [
    path('enter-details/',views.create_client_form, name='createform'),
]
