from django.shortcuts import render,redirect
from emastersystem.models import Employee
from django.views.generic import CreateView,FormView,TemplateView,UpdateView,View
from emastersystem.forms import UserProfileForm,UserCreationForm,LoginForm,UserRegistrationForm
from django .contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from emastersystem.models import Employee
from django.utils.decorators import method_decorator
# Create your views here.


def signin_required(fuctn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fuctn(request,*args,**kwargs)
        else:
            messages.error(request,'Sigin First')
            return  redirect('login')
    return wrapper

class SignUpView(CreateView):
    form_class=UserRegistrationForm
    template_name = 'signup.html'
    model=User
    success_url = reverse_lazy('login')

class LoginView(FormView):
    form_class = LoginForm
    template_name='login.html'
    model=User
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        admin=authenticate(request,username='admin',password='admin')
        if user:
            print('success')
            login(request,user)
            return redirect('viewprofile')
        
        else:
            return render(request,'login.html')

class ViewMyProfileView(TemplateView):
    template_name = 'viewprofile.html'
class IndexView(TemplateView):
    template_name = 'index.html'

@method_decorator(signin_required,name='dispatch')
class UserProfileAdd(CreateView):
    form_class=UserProfileForm
    template_name ='addprofile.html'
    model = Employee
    print('success')
    success_url=reverse_lazy('viewprofile')
    def form_valid(self,form):
        form.instance.user=self.request.user
        print(form.instance.user)
        self.object=form.save()
        messages.success(self.request, 'profile added')
        return super().form_valid(form)

@method_decorator(signin_required,name='dispatch')
class UserUpdateView(UpdateView):
    model=Employee
    form_class = UserProfileForm
    template_name ='editprofile.html'
    success_url = reverse_lazy('viewprofile')
    pk_url_kwarg ='user_id'
    def form_valid(self, form):
        messages.success(self.request,'your profile updated Successfully')
        self.object = form.save()
        return super().form_valid(form)

@method_decorator(signin_required,name='dispatch')
class EmployeeListView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'employelist.html'
    success_url = reverse_lazy('emp_list')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        employe=Employee.objects.all()
        context['employe']=employe
        return context




@signin_required
def SignOut(request,*args,**kwargs):
    logout(request)
    return redirect('login')