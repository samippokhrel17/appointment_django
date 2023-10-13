from django.shortcuts import render, HttpResponse
from django.http import HttpResponse 
import io, csv
from mysite.appoint.models import Branch


# Create your views here.
# def index(request):
#     return render(request,'appoint/index.html',context={})

# def import_excel(request):
#     if request.method == 'POST':
#         data = request.POST
#         print(data,'----------')
#     return render(request,'appoint/excel.html').

posts =[
    {
        'Branch':'Kalanki',
        
    },
    {
        'Branch':'Baneshor',
        
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def files(request):
    return render(request,'blog/files.html')

def readCSV(request):
    file = io.TextIOWrapper(request.FILES['import_excel'].file)
    appointment = csv.DictReader(file)
    list_of_dict = list(appointment)
    branches = Branch.object.all()
    for branch in branches:
        x = appointment.object.filter(branch = branch)
        print(x)
    

    # objs = [
    #     Member(
    #         member_id=generateMemberId(),
    #         first_name=row['first_name'],
    #         middle_name=row['middle_name'],
    #         last_name=row['last_name'],
    #         gender='male',
    #         religion_id=(row['religion'] if row['religion'] != '' else 6),
    #         date_of_birth=(row['date_of_birth']
    #                     if row['date_of_birth'] != '' else None),
    #         blood_group_id=(row['blood_group']
    #                         if row['blood_group'] != '' else 9),
    #         email=(row['email'] if row['email'] != '' else None),
    #         phone=row['phone'],
    #         state_id=(row['state'] if row['state'] != '' else 3),
    #         city=(row['city'] if row['city'] != '' else "Kathmandu"),
    #         address=(row['address'] if row['address']
    #                                 != '' else "Kathmandu"),
    #         emergency_contact_name=row['emergency_contact_name'],
    #         emergency_contact_address=row['emergency_contact_address'],
    #         emergency_contact_phone=row['emergency_contact_phone'],
    #         status="3",
    #         created_by=request.user,
    #     )
    #     for row in list_of_dict
    # ]

    # Member.objects.bulk_create(objs)

