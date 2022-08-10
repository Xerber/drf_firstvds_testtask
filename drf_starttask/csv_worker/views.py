from rest_framework.views import APIView
from rest_framework.response import Response

from .tasks import csv_task



class CreateTaskAPIView(APIView):
  def post(self,request, *args, **kwargs):
    filename = request.data['filename']
    task = csv_task.delay(filename)
    return Response({"success": f"Task '{task.id}' created successfully"})
