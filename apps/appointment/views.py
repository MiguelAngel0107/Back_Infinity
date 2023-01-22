from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from apps.appointment.models import Appointment
# Create your views here.

class Reserve(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        
        data = self.request.data
        
        user_name = str(data['user'])
        date_name = data['date']
        time_name = data['time']
        
        return Response({
            'user' : user_name,
            'date' : date_name,
            'time' : time_name
        }, status=status.HTTP_200_OK)
