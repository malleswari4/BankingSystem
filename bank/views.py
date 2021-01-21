from django.shortcuts import render,redirect
from django.http import HttpResponse
from bank.models import *
from bank.forms import *
from django.contrib import messages

def index(request):
    return render(request,'bank/index.html')
def customers(request):
    data=Customers.objects.all()
    return render(request,'bank/customers.html',{'data':data})
def user(request,pk):
    customer=Customers.objects.get(id=pk)
    form=CustomerForm(instance=customer)
    if request.method=='POST':
        form=CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/index")
    context={'form':form}
    return render(request,'bank/user.html',context)
def transfer(request):
    if request.method=='POST':
        sender=request.POST['sen']
        receiver=request.POST['rec']
        amount=request.POST['amount']
        sender1=Customers.objects.get(name=sender)
        balance1=sender1.balance
        form=CustomerForm(request.POST,instance=sender1)
        if balance1 < int(amount):
                return HttpResponse("insufficient amount")
        else:
            balance1=balance1-int(amount)
            sender1.balance=balance1
            sender1.save()
            rece=Customers.objects.get(name=receiver)
            balance2=rece.balance
            balance2=balance2+int(amount)
            rece.balance=balance2
            rece.save()
            return HttpResponse("<h3>"+sender +" Successfully Transfered To "+receiver+"</h3>"+"<br><h3> Your Transaction is Successful</h3>")
            # messages.success(request,"Successfully Transfered")
            
        
    return render(request,'bank/transfer.html')