from django.shortcuts import render , redirect
from django.contrib .auth import authenticate , login , logout
from .models import CustomUser         #CodeConfirmation
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .decorators import authenticated
from django.contrib.auth.decorators import login_required

# from helpers import send_sms,random_code
# from helpers import send_sms, random_code



# def code_verify(request):
#     code = request.POST.get('code')
#     print(code)
#     return render(
#         request= request,
#         template_name='auth/codeconfirmation.html',
#     )

# @login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        print(request.POST)
        email =(request.POST.get('email'))
        first_name =request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ex_user =CustomUser.objects.filter(email=email).first()
        if ex_user:
            return HttpResponse('<h1>Bu email orqali oldin royhatdan otilgan</h1>')
        elif password1 != password2:
            return HttpResponse('<h1>Parolni togri kiriting</h1>')
        else:
            user = CustomUser.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password1,
            )

            # code = random_code.random_code()
            # send_sms.send_email(email, code )
            # CodeConfirmation.objects.create(
            #     user=user,
            #      code=code
            # )
            login(request = request, user=user)
            return redirect('world')
    return render(
        request=request ,
        template_name = 'auth/register.html'
    )


@authenticated
def log_in(request):   ## funksiya methodning nomi log_in bo'lganini sababi tepada standart login chaqirib qo'yilgan
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request=request , email=email, password=password)
        if user:
            login(request=request ,user=user)
            return redirect('world')   # redirectning vazifasi home page ga yo'naltirib yuboradi .
        else:
            return HttpResponse('<h1>Siz password yoki emailni xato kiritdingiz !</h1>')
            # return redirect('login')
    return render(
        request=request ,
        template_name='auth/login.html'
    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')  #videoda loginni o'rniga maqola qo'yilgan