from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeAdminView(View):
    def get(self,request):
        return render(request,'administracion/adm_home.html',{})

class PreciosView(View):
    def get(self, request):
        return render(request,'administracion/adm_precios.html',{})