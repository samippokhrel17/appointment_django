from django.db import models



# # Create your models here.

    
class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    limit = models.IntegerField()
    is_main_branch = models.BooleanField(default=False) 

    # appoinment_id = models.ForeignKey(Appoinment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mainbranch(models.Model):
    name = models.CharField(max_length=100)
    # branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    branch_id = models.ManyToManyField(Branch)

    def __str__(self):
        return self.name


class Appoinment(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_cancel = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name