from django.shortcuts import render, HttpResponse
from django.http import HttpResponse 
import io, csv
from .models import Appoinment,Branch
# from mysite.appoint.models import Branchpy

posts =[
    {
        'Branch':'Branch 1',
        
    },
    {
        'Branch':'Branch 2',
        
    }
]


def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def files(request):
    return render(request,'blog/files.html')

def readCSV(request):
    try:
        file = io.TextIOWrapper(request.FILES['import_excel'].file)
        appointment = csv.DictReader(file)
        appointment_list = list(appointment)

        branches = Branch.objects.exclude(is_main_branch=True).all()
        for branch in branches:
            appointment_count = Appoinment.objects.filter(branch=branch, is_cancel=False, is_complete=False).count()
            remaining_appoinment = branch.limit - appointment_count
            print(appointment_count,f"branch={branch}")

            branch_app = appointment_list[:remaining_appoinment]
            appointment_list = appointment_list[remaining_appoinment:]

            objs = [
                Appoinment(
                    name=row['name'],
                    location=row['location'],
                    branch=branch,
                    is_cancel=False,
                    is_complete=False
                )
                for row in branch_app
            ]
            try:
                Appoinment.objects.bulk_create(objs)
            except Exception as e:
                print(e)

        if appointment_list:
            branch=Branch.objects.get(is_main_branch=True)
            objs = [
                Appoinment(
                    name=row['name'],
                    location=row['location'],
                    branch=branch,
                    is_cancel=False,
                    is_complete=False
                )
                for row in branch_app
            ]
            try:
                Appoinment.objects.bulk_create(objs)
            except Exception as e:
                print(e)

        context = {
            "msg": "Success"
        }
    except Exception as e:
        print(e)
        context = {
            "msg": e
        }
    return render(request, 'blog/files.html', context=context)
    
