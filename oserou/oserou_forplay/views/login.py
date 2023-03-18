from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from ..forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class signup_view(View):
    def get(self, request):
        form = SignupForm()
        param = {
                'form': form
        }
        #return HttpResponse("hello")
        return render(request, "oserou_forplay/signup.html", param)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
        else:
            print(form.cleaned_data)
            return HttpResponse("Oh no!")

        return HttpResponseRedirect("/play/login")

class login_view(View):
    def get(self, request):
        form = LoginForm()
        param = {
        'form': form,
        }

        return render(request, 'oserou_forplay/login.html', param)

    def post(self, request):
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return HttpResponseRedirect('/play/mypage')

        else:
            print(form.cleaned_data)
            return HttpResponse("Oh no!")
        

class logout_view(View):
     def get(self, request):
        logout(request)
        return HttpResponseRedirect("/play")

class user_view(View):
    @method_decorator(login_required)
    def get(self, request):
        user = self.request.user

        param = {
            "username" : user.get_username(), 
        }

        return render(request, 'oserou_forplay/user.html', param)

class other_view(View):
    def get(self, request):
         pass