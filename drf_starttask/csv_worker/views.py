from rest_framework.views import APIView
from rest_framework.response import Response
from celery import current_app

from .tasks import csv_task



class CreateTaskAPIView(APIView):
  def post(self,request, *args, **kwargs):
    filename = request.data.get('filename')
    task = csv_task.delay(filename)
    return Response({"success": f"Task '{task.id}' created successfully"})


class QueueTaskAPIView(APIView):
  def get(self, request):
    active = current_app.control.inspect().active()
    all_tasks = []
    if active is not None:
      for node, tasks in active.items():
        all_tasks += tasks
    return Response({'Count:': len(all_tasks)})


class StatusTaskAPIView(APIView):
  def post(self,request, *args, **kwargs):
    task_id = request.data.get('task_id')
    task = current_app.AsyncResult(task_id)
    response_data = {'status_task': task.status, 'task_id': task.id}
    if task.status == 'SUCCESS':
      result = task.get()
      response_data['result'] = result
    return Response(response_data)