from typing import Any
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import CreateView,UpdateView
from .forms import EmployeeReport
from .models import DailyReport
from django.views.generic.base import TemplateView,RedirectView
from django import forms


def add_show(request):
    if request.method == "POST":
        fm =  EmployeeReport(request.POST)
        if fm.is_valid():
            # fm.save() #1st way ,2nd can use cleaned data
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            work = fm.cleaned_data['assigned_work']
            complete = fm.cleaned_data['completed']
            p_work = fm.cleaned_data['pending']
            data =  DailyReport(name = name, email = email, assigned_work = work,completed = complete,pending = p_work)
            data.save()
            fm = EmployeeReport()
    else:
        fm = EmployeeReport()
    emp = DailyReport.objects.all()
    return render(request, 'report.html',{"form":fm, "employees":emp})

def update_report(request,id):
    if request.method == "POST":
        stud = DailyReport.objects.get(pk = id)
        fm =  EmployeeReport(request.POST, instance = stud)
        if fm.is_valid():
            fm.save()
    else:
        stud = DailyReport.objects.get(pk = id)
        fm =  EmployeeReport(instance = stud)

    return render(request, 'updatereport.html',{'form':fm})


def delete_data(request,id):
    if request.method == "POST":
        stud = DailyReport.objects.get(pk = id)
        stud.delete()
        return HttpResponseRedirect("/")
