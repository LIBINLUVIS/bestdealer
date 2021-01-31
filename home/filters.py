import django_filters
from .models import image
from django import forms
from django_filters import CharFilter



class HomeFilter(django_filters.FilterSet):

	temp=CharFilter(field_name='name',lookup_expr='icontains',label='')