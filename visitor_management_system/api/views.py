from rest_framework import generics
from .models import Employee, VisitorLog
from .serializers import EmployeeSerializer, VisitorLogSerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class VisitorLogListCreateAPIView(generics.ListCreateAPIView):
    queryset = VisitorLog.objects.all()
    serializer_class = VisitorLogSerializer

class VisitorLogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisitorLog.objects.all()
    serializer_class = VisitorLogSerializer


# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Employee, VisitorLog
# from .serializers import EmployeeSerializer, VisitorLogSerializer

# class UserRegistrationAPIView(APIView):
#     def post(self, request):
#         # Your user registration logic goes here
#         return Response("User registration logic goes here", status=status.HTTP_200_OK)

# class EmployeeListAPIView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data)

# class EmployeeCreateAPIView(APIView):
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmployeeDetailAPIView(APIView):
#     def get(self, request, pk):
#         employee = Employee.objects.get(pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         employee = Employee.objects.get(pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = Employee.objects.get(pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class VisitorLogListAPIView(APIView):
#     def get(self, request):
#         visitor_logs = VisitorLog.objects.all()
#         serializer = VisitorLogSerializer(visitor_logs, many=True)
#         return Response(serializer.data)

# class VisitorLogCreateAPIView(APIView):
#     def post(self, request):
#         serializer = VisitorLogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class VisitorLogDetailAPIView(APIView):
#     def get(self, request, pk):
#         visitor_log = VisitorLog.objects.get(pk=pk)
#         serializer = VisitorLogSerializer(visitor_log)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         visitor_log = VisitorLog.objects.get(pk=pk)
#         serializer = VisitorLogSerializer(visitor_log, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         visitor_log = VisitorLog.objects.get(pk=pk)
#         visitor_log.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 