from django.shortcuts import render




def base(request):
    return render(request, 'home/base.html', {'title':'Beeflux'})