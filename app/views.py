from django.shortcuts import render

# Create your views here.
def down(request):
    return render(request,'down.html')


def btsrp(request):
    return render(request,'btsrp.html')