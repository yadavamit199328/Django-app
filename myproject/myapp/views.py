from django.shortcuts import render
from myapp.models import Start, Phoneno
from django_pandas.io import read_frame
from django.http import HttpResponse

# Create your views here.


def home(request):
    a = Start.objects.all()
    if request.method=="GET":
        
        b = read_frame(a)
        
        return render(request,'myapp/home.html',{'b':b})
    c = request.POST['resname']
    print(c)
    q = Start.objects.values("coupon").filter(name=c)
    qq = read_frame(q)
    print(q)
    # qqq = qq.coupon
    # return HttpResponse(q)
    return render(request,'myapp/coupon.html',{'cou':qq})

def phoneno(request):
    aa = Phoneno.objects.all()
    if request.method=="GET":
        
        bb = read_frame(aa)
        
        return render(request,'myapp/phoneno.html',{'bb':bb})
        
    
    