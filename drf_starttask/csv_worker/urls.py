from django.urls import path
from csv_worker.views import CreateTaskAPIView


urlpatterns = [
    path('v1/create_task', CreateTaskAPIView.as_view()),
]
