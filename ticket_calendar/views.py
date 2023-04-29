from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CalendarSerializer
from .models import Calendar
# Create your views here.

import datetime



class CalendarViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class=CalendarSerializer

    current_date = datetime.date.today()

    def check_date(self):
        queryset=Calendar.get(day=consert_date)

        if current_date==queryset:
            return Calendar
        else:
            return

    


