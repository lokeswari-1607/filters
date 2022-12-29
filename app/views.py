from django.shortcuts import render

# Create your views here.
def Builtinfilters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'LokESwARi aNd YeshWaNtH','c':'a','dt':dt,'c':1}
    return render(request,'Builtinfilters.html',d)

def usdf(request):
    d={'data':'AmmA aNd AppA'}
    return render(request,'usdf.html',d)