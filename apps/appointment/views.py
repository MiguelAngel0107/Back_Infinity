from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from apps.appointment.models import Appointment
from apps.appointment.serializers import AppointmentSerializer
from datetime import date


class Get_Reserve(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):

        user = self.request.user

        if not Appointment.objects.filter(user=user).exists():
            return Response(
                {'error': 'Invalid Appointment option, no exists'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            appointment = Appointment.objects.order_by(
                'date').filter(user=user)
            appointment = AppointmentSerializer(appointment, many=True)

            return Response(
                {'bookings': appointment.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Invalid Appointment option'},
                status=status.HTTP_404_NOT_FOUND
            )


class Reserve_Save(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):

        data = self.request.data
        user = self.request.user

        date_name = data['date']
        date_name = date(date_name['year'],
                         date_name['mounth'], date_name['day'])

        time = data['time']['hour']

        try:
            Appointment.objects.create(user=user, date=date_name, time=time)
        except:
            return Response(
                {'error': 'Error al crear la Cita'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response({
            'status': 'Se guardo Correctamente su Cita'
        }, status=status.HTTP_200_OK)
