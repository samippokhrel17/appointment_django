from django.urls import path, include
# from .views import index, import_excel
from . import views

urlpatterns = [
    # path('',index),
    # path('import/excel/',import_excel)
    path('', views.home, name='appoint-home'),
    path('about/', views.about, name='appoint-about'),
    path('contact/',views.contact,name='appoint-contact'),
    path('files/',views.files,name='appoint-files'),
    path('readCSV',views.readCSV,name='appoint-readCSV'),
    

]
 