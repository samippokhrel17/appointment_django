from django.db import models

# # Create your models here.

    
class Branch(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # appoinment_id = models.ForeignKey(Appoinment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mainbranch(models.Model):
    name = models.CharField(max_length=255)
    # branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    branch_id = models.ManyToManyField(Branch)

    def __str__(self):
        return self.name

class Appoinment(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
#     # time = models.DateTimeField()
    appoinment_cancel = models.BooleanField(default=False)
    appoinment_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


