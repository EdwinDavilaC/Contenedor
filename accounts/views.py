from django.shortcuts import render, redirect
from django import views
from django.contrib.auth.models import User
from .forms import UserForm
from accounts.models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.

def GetUsers(request):
    users = Usuario.objects.all()
    template_name = 'accounts/list.html'
    context = {
        'users' : users
    }
    
    return render(request, template_name, context)
       
def GetUser(request, id):
    user = Usuario.objects.get(pk=id)
    template_name = 'accounts/detail.html'
    context = {
        'user' : user 

    }
    return render(request, template_name, context)

class CreateUser(views.View):
    def get(self, request):
        form = UserForm()
        template_name = 'accounts/form-create.html'
        context = {
            'form' : form
        }

        return render(request, template_name, context)
    
    def post(self, request):
        new_form = UserForm(request.POST)
        if new_form.is_valid():
            new_user = new_form.save(commit=False)
            new_user.set_password(request.POST['password'])
            new_user.save()            
            return redirect('users:detail', new_user.id)
        else:
            template_name = 'accounts/form-create.html'
            context = { 
                'user' : new_form

            }
            return render(request, template_name, context)

class UpdateUser(views.View):
    def get(self, request, id):
        user = Usuario.objects.get(pk=id)
        form = UserForm(instance=user)
        template_name = 'accounts/form.html'
        context = {
        'form' : form,
        'user' : user,
        }

        return render(request, template_name, context)

    def post(self, request, id):
        user = Usuario.objects.get(pk=id)
        update_form = UserForm(request.POST, instance=user)

        if update_form.is_valid():
            user_updated = update_form.save(commit=False)
            user_updated.set_password(request.POST['password'])  
            user_updated.save()
            return redirect('users:detail', id)  
        else: 
            template_name = 'accounts/form.html'
            context = {
            'form' : update_form,
            'user' : user,
            }
            return render(request, template_name, context)

def DeleteUser(request, id):
    user = Usuario.objects.get(pk=id)
    user.delete()
    return redirect('users:list')


class Login (views.View):
    def get(self, request):
        auth_form = AuthenticationForm()
        template_name = 'authentication/login.html'
        context = {
            'form' : auth_form 
            }
        return render(request, template_name, context)    


    def post(self, request):
        try:
            auth_form = AuthenticationForm(data=request.POST)
            if auth_form.is_valid():
                username = auth_form.cleaned_data['username']
                password = auth_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('users:detail', user.id)
                else:
                    template_name = 'authentication/login.html'
                    context = {
                        'form' : auth_form 
                    }
                    return render(request, template_name, context)
                    
            else:
                template_name = 'authentication/login.html'
                context = {
                    'form' : auth_form 
                }
                return render(request, template_name, context)

        except Exception as e:
            template_name = 'authentication/login.html'
            context = {
                'form' : auth_form 
            }
            return render(request, template_name, context)

def Logout(request):
    logout(request)
    return redirect('login')


