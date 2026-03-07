from django.shortcuts import render
from django.views import View

# Create your views here.
class SignupView(View):
    def get(self, request):
        return render(request, 'account/signup.html')
    
    def post(self, request):
        return render(request, 'account/signup.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')
    
    def post(self, request):
        return render(request, 'account/login.html')

