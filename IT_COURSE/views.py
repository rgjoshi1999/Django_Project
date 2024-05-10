from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .models import Feedback, ContactUs
from .forms import Signupform,ContactForm ,Feedbackform #,PaymentForm
#from django.conf import settings
#import stripe


#stripe.api_key = settings.STRIPE_SECRET_KEY

#Create your views here.

def home(request):
    return render(request,'home.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

def Msg(request):
    return render(request,'Msg.html')

def ContactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Msg')  # You can define a 'thank_you_page' in your urls.py
    else:
        form = ContactForm()

    return render(request, 'ContactUs.html', {'form': form})

'''def your_view(request):
    options = ['AWS', 'DevOps', 'Data Analytics', 'Full Stack Java', 'Full Stack Python', 'MERN Stack']

    return render(request, 'ContactUs.html', {'options': options})'''

'''def your_view(request):
    courses = Course.objects.all()
    return render(request, 'ContactUs.html', {'courses': courses})'''


def Models(request):
    return render(request,'Models.html')

def CoursesOffered(request):
    return render(request,'CoursesOffered.html')

def SignUp(request):
    if request.method == "POST":
        fm = Signupform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'you have register successfully')
            return redirect("SignIn")
    else:
        fm = Signupform()
    return render(request,'SignUp.html',{'reg_fm':fm})

def SignIn(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return render(request,'home.html',{'user':user, })

    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'user_data': fm})

def SignOut(request):
    logout(request)
    return redirect("Home")

def feedback(request):
    if request.method == "POST":
        fd = Feedbackform(request.POST)
        if fd.is_valid():
            if not request.user.is_authenticated:
                return redirect('SignIn')
            fd.save()
            return redirect("feedback")
    else:
        fd = Feedbackform()
    show = Feedback.objects.all()
    return render(request, 'feedback.html',{'feedback': fd,'show': show})

def showfeedback(request):
    show = Feedback.objects.all()
    return render(request,'reviews.html',{'show':show})

def RI(request):
    return render(request,'RI.html')

def Freshers(request):
    return render(request,'Freshers.html')

def fullstackpython(request):
    return render(request,'fullstackpython.html')

def fullstackjava(request):
    return render(request,'fullstackjava.html')

def aws(request):
    return render(request,'aws.html')

def dataanalytics(request):
    return render(request,'dataanalytics.html')

def devops(request):
    return render(request,'devops.html')

def mernstack(request):
    return render(request,'mernstack.html')


def aws(request):
    return render(request,'aws.html')

def your_view(request):
    user = request.user
    return render(request,'home.html',{'user':user})


'''def success(request):
    return render(request,'home.html')

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Create a customer and charge the card
            token = stripe.Token.create(
                card={
                    'number': form.cleaned_data['card_number'],
                    'exp_month': form.cleaned_data['exp_month'],
                    'exp_year': form.cleaned_data['exp_year'],
                    'cvc': form.cleaned_data['cvc'],
                },
            )

            charge = stripe.Charge.create(
                amount=1000,  # amount in cents
                currency='usd',
                source=token.id,
                description='Example Charge',
            )

            # Handle successful payment (e.g., update database, send confirmation email)
            return render(request, 'success.html')

    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})
'''