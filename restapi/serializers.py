from django.contrib.auth.models import User, Group
from rest_framework import serializers
from empapp.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('empName', 'empEmail', 'empPan')

class EmployeeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class EmployeeGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')