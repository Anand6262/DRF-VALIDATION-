from tracemalloc import start
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student
from django.db import models   

#3)Validators
def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('Name should be start with R')


class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=255, validators=[starts_with_r]) #We are writing this (validators=[starts_with_r]) for #3)Validators
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=255)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name= validate_data.get('name', instance.name)
        instance.roll= validate_data.get('roll', instance.roll)
        instance.city= validate_data.get('city', instance.city)
        instance.save()
        return instance


    #1)Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full!!')
        return value
    

    #2)Object Level Validation
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() == 'rahul' and ct.lower() !='mumbai':
            raise serializers.ValidationError('City of Rahul must be Mumbai!!')
        return data


    # def validate(self, data):
    #     ro=data.get('roll')
    #     for roll in range(ro):
    #         raise serializers.ValidationError('Roll must be unique!!')
    #     return data
    # def validate_roll(self, value):
    #     for roll in range(value):
    #         raise serializers.ValidationError('Roll must be unique!!')
    #     return value
