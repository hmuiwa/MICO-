
from django.shortcuts import render,redirect
from careproapp.models import Appointment, member
from careproapp.models import Message


# Create your views here.
def index(request):
    if request.method == "POST":
        myappointment=Appointment(
            patient_name=request.POST['patient_name'],
            doctors_name=request.POST['doctors_name'],
            department_name=request.POST['department'],
            phone_number=request.POST['phone_number'],
            symptoms=request.POST['symptoms'],
            date=request.POST['date'],
        )
        myappointment.save()
        return redirect('/index.html')


    else:
        return render(request,'index.html')




def about(request):
    return render(request, 'about.html' )

def contact(request):
    if request.method == "POST":
        mymessage=Message(
            name=request.POST['name'],
            email=request.POST['email'],
            number=request.POST['number'],
            message=request.POST['message'],

        )
        mymessage.save()
        return redirect('/contact.html')

    else:
        return render(request, 'contact.html')



def doctor(request):
    return render(request, 'doctor.html' )

def testimonial(request):
    return render(request, 'testimonial.html' )

def treatment(request):
    return render(request, 'treatment.html' )

def login(request):
    if request.method == "POST":
        if member.objects.filter(
            username=request.POST['username'],
            password=request.POST['password'],
        ).exists():
            members = member.objects.get(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            return render(request,'index.html',{'members':members})

        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        members = member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login.html')
    else:
        return render(request, 'register.html')

