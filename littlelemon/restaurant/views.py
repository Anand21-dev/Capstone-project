from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .models import Booking,Menu
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class menuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(
            {"success": "Dish added to the menu!"},
            status=status.HTTP_201_CREATED
        )

class singleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        # 🔥 Return a success message so form resets
        return Response(
            {"success": "Menu updated successfully!",
             
             "data":serializer.data},
            status=status.HTTP_200_OK
        )
    

class BookingViewSet(ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer

   def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(
            {"success": "Booking successful!"},
            status=status.HTTP_201_CREATED
        )
#    def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         # 🔥 Return a success message so form resets
#         return Response(
#             {"success": "Booking updated successfully!",
             
#              "data":serializer.data},
#             status=status.HTTP_200_OK
#         )

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 