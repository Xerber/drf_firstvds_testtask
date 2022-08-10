from django.urls import path
from csv_worker.views import CreateTaskAPIView, QueueTaskAPIView, StatusTaskAPIView


urlpatterns = [
    path('v1/create_task', CreateTaskAPIView.as_view()),
    path('v1/queue_task', QueueTaskAPIView.as_view()),
    path('v1/status_task', StatusTaskAPIView.as_view()),
]
