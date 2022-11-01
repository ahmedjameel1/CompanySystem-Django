from django.shortcuts import render ,redirect
from .forms import RegistrationForm, LoginForm
from .models import Account
from django.contrib import messages, auth
from accounts.models import Account 
from django.contrib.auth import authenticate 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = RegistrationForm()
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            phone_number = request.POST['phone_number']
            username = email.split('@')[0]
            user = Account.objects.create(first_name=first_name,
            last_name=last_name,email=email,phone_number=phone_number,username=username)
            user.set_password(password)
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    ctx = {'form':form}
    return render(request, 'accounts/register.html',ctx)



def login(request):
    if request.user.is_authenticated:
        url = request.META.get('HTTP_REFERER')
        try:
            query = requests.utils.urlparse(url).query
            params = dict(x.split('=') for x in query.split('&'))
            if 'next' in params:
                nextpage = params['next']
                return redirect(nextpage)
        except:
           return redirect('home')
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome '+ user.first_name + '!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect email or password')
            return redirect('login')
    else:
        form = LoginForm()
    ctx = {'form':form}
    return render(request, 'accounts/login.html', ctx)



def logout(request):
    auth.logout(request)
    return redirect('login')











