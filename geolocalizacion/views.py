from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.distance import geodesic
from .models import Location



#distance = geodesic(loc1, loc2).km
# Create your views here.
class geolocalizacion_view:
    def post(self, request):
        serializer = LocationSerializer(data= request.data)
        if serializer.is_valid():
            Location= serializer.save()
            #loc1 = (cliente.latitud, cliente.longitud)
            #loc2 = (repartidor.latitud, repartidor.longitud)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def seguimiento_view(request, repartidor_id):
    context = {
        'repartidor_id': repartidor_id
    }
    return render(request, 'geolocalizacion/seguimiento.html', context)
