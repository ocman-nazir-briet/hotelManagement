from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class branch(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural= "Branch List"

class staff(models.Model):
    categoryChoice=(
        ("W","Waiter"),
        ("S", "cleaning"),
        ("D", "Delivery"),
        ("M", "Management"),
        ("M", "Manager")
    )
    branchName = models.ForeignKey(branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    category =models.CharField(max_length=1, choices=categoryChoice) 
    genderType = models.TextChoices('gender', 'M F Other')
    gender = models.CharField(choices=genderType.choices,max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Staff & Management"


class food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Food Items'

class clients(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models .CharField(max_length=25)
    identity = models.CharField(blank=True ,max_length=50)
    genderType = models.TextChoices('gender', 'M F Other')
    gender = models.CharField(blank=True, choices=genderType.choices, max_length=50)
    BranchName = models.OneToOneField(branch, on_delete=models.CASCADE, primary_key=True) 
    foodItems = models.ManyToManyField(food, blank=True)
    roomNo = models.CharField(max_length=10)
    billStatus= models.TextChoices('Bill Status', 'Paid Pending Cancelled')
    bill = models.CharField(default="Pending", choices=billStatus.choices, max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Active Clients"

    def order(self):
        return ", ".join([str(p)for p in self.foodItems.all()])

class orders(models.Model):
    name = models.CharField(max_length=50)
    orderedItems = models.ManyToManyField(food)

    class Meta:
        verbose_name_plural = "Orders"

    def items(self):
        return ", ".join([str(p)for p in self.orderedItems.all()])