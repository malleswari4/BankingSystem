from django.db import models

# Create your models here.
users=(('1','bhuvana'),('2','teja'),('3','siva'),('4','kalyani'),('5','pooji')
    ,('6','prani'),('7','vyshu'),('8','nandu'),('9','mouni'),('10','nikki'))

class Customers(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    balance=models.IntegerField()
    def __str__(self):
        return self.name+" "+self.email+" "+str(self.balance)

class TransferTable(models.Model):
    selectuser=models.CharField(max_length=20,choices=users,default='1')
    money=models.IntegerField()
    def __str__(self):
        return self.selectuser+" "+str(self.money)