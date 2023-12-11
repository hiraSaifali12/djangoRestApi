from django.shortcuts import render
from rest_framework import viewsets
from apis.models import Company,Employee
from apis.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer


    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
          
          company=Company.objects.get(pk=pk)
          employee= Employee.objects.filter(company= company)
          employee_serializer= EmployeeSerializer(employee, many=True,context={'request':'request'})
        except Exception as e :
            print(e)
            return Response({
                'message':'company not exist'
            })
        return Response(employee_serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


