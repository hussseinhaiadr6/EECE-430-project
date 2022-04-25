from urllib import request
from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from datetime import *
from django.db.models import Q

from gymApp.forms import CreateClientForm,CreateClassForm
from .models import Client,Class,Membership,Reservation,Instructor
today=date.today()
print(today)
S=Client.objects.all()

ClientNameList=[]
for user in S:
    ClientNameList.append(user.Client_name)
def index(request):
    if "uname" in request.session:
        return userhome(request)
    else:
        return render(request, 'index.html')
def signup(request):
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            clientform = form.cleaned_data

            name = clientform['Client_name']
            password = clientform['Client_pass']
            email = clientform['Client_email']
            phone = clientform['Client_phone']
            address = clientform['Client_address']
            gender = clientform['Client_gender']
            age=clientform['Client_age']
            print(phone)
            print(address)
            listOfEmails=[]
            S=Client.objects.all()
            for client in S:
                listOfEmails.append(client.Client_email)
            if ( email in listOfEmails):
                return HttpResponse("email is already registered")
            
            else:
                try:
                    Client.objects.create(Client_name=name,Client_pass=password,Client_email=email,Client_phone=phone,Client_address=address,Client_gender=gender,Client_age=age)
                    #user = Client.objects.get(Client_email=email)
                    request.session['uname'] = name
                    request.session['umail'] = email
                    return userhome(request)
                except:
                    return("something went wrong")
    else:
        form = CreateClientForm()
   
    return render(request, 'Signup.html', {'form': form})
def userhome(request):
    print("calling user home")
    if 'uname' in request.session:
        name=request.session.get('uname')
        mail=request.session.get('umail')
        print("the name is "+name)
    try:
        user = Client.objects.get(Client_email=mail)
        print(user.Client_address)
        membership = Membership.objects.get(client=user)
        final=membership.expired
        print(" memebrship finish time is : "+str(final))
        now=date.today()
        days=(final-today).days
        return render(request,'clienthome.html',{'client':name,"status":"you have "+str(days)+"days left"})
    except:
        return render(request,'clienthome.html',{'client':name,"status":"no membership yet"})  
def createClass(request):
    if request.method == 'POST':
        form = CreateClassForm(request.POST)
        if form.is_valid():
            Classform = form.cleaned_data
            id = Classform['Class_id']
            name = Classform['Class_name']
            instructor = Classform['Class_instructor']
           
            Class.objects.create(Class_id=id,Class_name=name,Class_instructor=instructor)
            S=Client.objects.all()
            print(S)
            return render(request, 'addclass.html',{'form':CreateClassForm()})
    else:
        form = CreateClassForm()
   
    return render(request, 'addclass.html', {'form': form})
def clientlogin(request):

    print("hello")
    if request.method=='POST':
        email=request.POST.get("email")
        psw=request.POST.get("psw")
        print(email)
        print(psw)
        
        try:
            user = Client.objects.get(Client_email=email)

            if user.Client_pass == psw:
                request.session['uname'] = user.Client_name
                request.session['umail'] = user.Client_email
                return userhome(request)
            else:
                data = {'status':"Incorrect  Password!!!"}
                return render(request,'Signin.html',{'error':"password is incorrect"})
        except:
            return render(request,'Signin.html',{'error':"Email is not  is incorrect"})
            
       
    else:
        print("get method")
        return render(request,'Signin.html') 
# this methos is for viewing the schedule of the classes no login needed 
def ClassSchedule(request):
    print("route of class chedule")
    S=Class.objects.all()
    M1=["no","class",""]
    M2=["no","class",""]
    M3=["no","class",""]
    M4=["no","class",""]
   
    T1=["no","class",""]
    T2=["no","class",""]
    T3=["no","class",""]
    T4=["no","class",""]
   
    W1=["no","class",""]
    W2=["no","class",""]
    W3=["no","class",""]
    W4=["no","class",""]
    
    R1=["no","class",""]
    R2=["no","class",""]
    R3=["no","class",""]
    R4=["no","class",""]
   
    F1=["no","class",""]
    F2=["no","class",""]
    F3=["no","class",""]
    F4=["no","class",""]
    
    Classes=Class.objects.all()
    timeslot=[]
    classname=[]
    instructor=[]
    capacity=[]
    for Clas in Classes:
        timeslot.append(Clas.Class_id)
        classname.append(Clas.Class_name)
        instructor.append(Clas.Class_instructor.Instructor_name)
        capacity.append(Clas.Class_capacity)
    index=0
    print(timeslot)
    print(classname)
    print(instructor)
    for x in timeslot:
        if x=='11':
            M1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="12":
            M2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="13":
            M3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="14":
            M4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=='21':
            T1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="22":
            T2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="23":
            T3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="24":
            T4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=='31':
            W1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="32":
            W2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="33":
            W3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="34":
            W4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=='41':
            R1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="42":
            R2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="43":
            R3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="44":
            R4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=="51":
            F1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="52":
            F2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="53":
            F3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="54":
            F4=[str(classname[index]),str(instructor[index]),str(capacity[index])]  
        index=index+1 
    
    data={'M10':M1[0],'M11':M1[1],'M12':M1[2],
        'M20':M2[0],'M21':M2[1],'M22':M2[2],
        'M30':M3[0],'M31':M3[1],'M32':M3[2],
        'M40':M4[0],'M41':M4[1],'M42':M4[2],

        'T10':T1[0],'T11':T1[1],'T12':T1[2],
        'T20':T2[0],'T21':T2[1],'T22':T2[2],
        'T30':T3[0],'T31':T3[1],'T32':T3[2],
        'T40':T4[0],'T41':T4[1],'T42':T4[2],
        
        'W10':W1[0],'W11':W1[1],'W12':W1[2],
        'W20':W2[0],'W21':W2[1],'W22':W2[2],
        'W30':W3[0],'W31':W3[1],'W32':W3[2],
        'W40':W4[0],'W41':W4[1],'W42':W4[2],

        'R10':R1[0],'R11':R1[1],"R12":R1[2],
        'R20':R2[0],'R21':R2[1],"R22":R2[2],
        'R30':R3[0],'R31':R3[1],"R32":R3[2],
        'R40':R4[0],'R41':R4[1],"R42":R4[2],
        

        'F10':F1[0],'F11':F1[1],"F12":F1[2],
        'F20':F2[0],'F21':F2[1],"F22":F2[2],
        'F30':F3[0],'F31':F3[1],"F32":F3[2],
        'F40':F4[0],'F41':F4[1],"F42":F4[2]}
    if "uname" in request.session:
        return render(request,'reserveclass.html',context=data)
    else:
        return render(request,'schedule.html',context=data)
# this method is accesed after a susccesful login from the client
# render the page for amdin to delete a class  and update(not yet implmented the update 
def viewclasses(request):
    S=Class.objects.all()
    return render(request,'viewclasses.html', {'Classes':S})   
def db_delete_class(request,id):
    if request.method == 'GET': 
        clas = Class.objects.get(Class_id=id)
        clas.delete()

        return HttpResponse("Deleted succesfully")
    else:
        return HttpResponse("Something went wrong!!!!!")
def manageclient(request):
    Clients=Client.objects.all() 
    return render(request,'adminClients.html', {'Clients':Clients}) 
def update_client(request,mail):
    
    if request.method == 'POST':
        print ("this is a post request")
        print("prirnitng mail" +mail)
        mail=mail[5:]
        name = request.POST.get('name') 
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address') 
        print(name)
        print(email)
        print(phone)
        print(address)
        client1 = Client.objects.get(Client_email=mail)
        print("helo mF")
        client1.Client_name = name
        client1.Client_email = email
        client1.Client_phone = phone
        client1.Client_address = address
        client1.save()

       
    else :
        print ("this is a get request")    
        print(mail)   
        Client1 = Client.objects.get(Client_email=mail)

        return render(request,'updateclient.html', {'client':Client1}) 
def delete_client(request,mail):
    clas = Client.objects.get(Client_email=mail)
    clas.delete()
def signout(request):
    print('sign out called')
    print(request.session.get("uname"))
    del request.session['uname']
    del request.session['umail'] 
    return render(request,'index.html')
def membership(request,type):
    print("calling membership function")
    if("umail" in request.session):
        mail=request.session.get("umail")
        user=Client.objects.get(Client_email=mail)
        try:
            Membership.objects.get(client=user)
            return render(request,"clienthome.html",{"error":"already have a memebrship"})
        except:
            if "uname" in request.session:
                mail=request.session.get("umail")
                print ("mail to send: "+ mail)
                client1 = Client.objects.get(Client_email=mail)
                print(type)
                if type=="B":
                    send_mail('Area_140 gym : payment invoice',
                    'Hello there, This is an automated message you are requested to pay an amount of 11$ in any OMT center to this phone number: 79185649',
                    'area140@gmail.com', #FROM 
                    [str(mail)], #TO
                    fail_silently=False)
                    today=date.today()
                    date_time = today.strftime("%d/%m/%Y")
                    print("printing the date: "+str(date_time))
                    date_format = '%d/%m/%Y'
                    dtObj = datetime.strptime(date_time, date_format)
                    future_date = dtObj + relativedelta(months=1)
                    Membership.objects.create(client=client1,initial=today,expired=future_date.date(),membershipType='B')

                elif type=="S":
                    send_mail('Area_140 gym : payment invoice',
                    'Hello there, This is an automated message you are requested to pay an amount of 21$ in any OMT center to this phone number: 79185649',
                    'area140@gmail.com', #FROM 
                    [str(mail)], #TO
                    fail_silently=False)
                    today=date.today()
                    date_time = today.strftime("%d/%m/%Y")
                    print("printing the date: "+str(date_time))
                    date_format = '%d/%m/%Y'
                    dtObj = datetime.strptime(date_time, date_format)
                    future_date = dtObj + relativedelta(months=3)
                    Membership.objects.create(client=client1,initial=today,expired=future_date.date(),membershipType='S')
                else:
                    send_mail('Area_140 gym : payment invoice',
                    'Hello there, This is an automated message you are requested to pay an amount of 31$ in any OMT center to this phone number: 79185649',
                    'area140@gmail.com', #FROM 
                    [str(mail)], #TO
                    fail_silently=False)
                    today=date.today()
                    date_time = today.strftime("%d/%m/%Y")
                    print("printing the date: "+str(date_time))
                    date_format = '%d/%m/%Y'
                    dtObj = datetime.strptime(date_time, date_format)
                    future_date = dtObj + relativedelta(months=6)
                    Membership.objects.create(client=client1,initial=today,expired=future_date.date(),membershipType='P')
                    
                name=request.session.get("uname")
                print(name)
                return userhome(request)
    else:

        return render(request,'Signin.html')
def reserveclass(request,id):
    print("calling reserve function")
    classid=id[-2:]
    mail=request.session.get("umail")
    print("amil is : "+mail+" class if is : "+classid)
    
    user=Client.objects.get(Client_email=mail)
    try:
        memebrship=Membership.objects.get(client=user)
        targetclass = Class.objects.get(Class_id=classid)
        checked=Reservation.objects.all()
        for x in checked:
            if ( x.client==user and x.class_id==targetclass.Class_id):
                return ClassScheduleerror(request, "this class is already resevred")
        
        print("not checking if already registered")
        capacity=targetclass.Class_capacity
        if (targetclass.Class_capacity>0):
            Reservation.objects.create(client=user,class_id=targetclass.Class_id)
            targetclass.Class_capacity=capacity-1
            targetclass.save()
            return ClassScheduleerror(request, "resevartion was succesful")
        else:
            return  ClassScheduleerror(request, "class is fully boooked")
    except:
        return  ClassScheduleerror(request, "you need to have a membership first")
def ClassScheduleerror(request,error):
    print("route of class chedule")
    S=Class.objects.all()
    M1=["no","class",""]
    M2=["no","class",""]
    M3=["no","class",""]
    M4=["no","class",""]
   
    T1=["no","class",""]
    T2=["no","class",""]
    T3=["no","class",""]
    T4=["no","class",""]
   
    W1=["no","class",""]
    W2=["no","class",""]
    W3=["no","class",""]
    W4=["no","class",""]
    
    R1=["no","class",""]
    R2=["no","class",""]
    R3=["no","class",""]
    R4=["no","class",""]
   
    F1=["no","class",""]
    F2=["no","class",""]
    F3=["no","class",""]
    F4=["no","class",""]
    
    Classes=Class.objects.all()
    timeslot=[]
    classname=[]
    instructor=[]
    capacity=[]
    for Clas in Classes:
        timeslot.append(Clas.Class_id)
        classname.append(Clas.Class_name)
        instructor.append(Clas.Class_instructor.Instructor_name)
        capacity.append(Clas.Class_capacity)
    index=0
    print(timeslot)
    print(classname)
    print(instructor)
    for x in timeslot:
        if x=='11':
            M1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="12":
            M2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="13":
            M3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="14":
            M4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=='21':
            T1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="22":
            T2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="23":
            T3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="24":
            T4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=='31':
            W1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="32":
            W2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="33":
            W3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="34":
            W4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=='41':
            R1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="42":
            R2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="43":
            R3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="44":
            R4=[str(classname[index]),str(instructor[index]),str(capacity[index])]

        elif x=="51":
            F1=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="52":
            F2=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="53":
            F3=[str(classname[index]),str(instructor[index]),str(capacity[index])]
        elif x=="54":
            F4=[str(classname[index]),str(instructor[index]),str(capacity[index])]  
        index=index+1 
    
    data={'M10':M1[0],'M11':M1[1],'M12':M1[2],
        'M20':M2[0],'M21':M2[1],'M22':M2[2],
        'M30':M3[0],'M31':M3[1],'M32':M3[2],
        'M40':M4[0],'M41':M4[1],'M42':M4[2],

        'T10':T1[0],'T11':T1[1],'T12':T1[2],
        'T20':T2[0],'T21':T2[1],'T22':T2[2],
        'T30':T3[0],'T31':T3[1],'T32':T3[2],
        'T40':T4[0],'T41':T4[1],'T42':T4[2],
        
        'W10':W1[0],'W11':W1[1],'W12':W1[2],
        'W20':W2[0],'W21':W2[1],'W22':W2[2],
        'W30':W3[0],'W31':W3[1],'W32':W3[2],
        'W40':W4[0],'W41':W4[1],'W42':W4[2],

        'R10':R1[0],'R11':R1[1],"R12":R1[2],
        'R20':R2[0],'R21':R2[1],"R22":R2[2],
        'R30':R3[0],'R31':R3[1],"R32":R3[2],
        'R40':R4[0],'R41':R4[1],"R42":R4[2],
        

        'F10':F1[0],'F11':F1[1],"F12":F1[2],
        'F20':F2[0],'F21':F2[1],"F22":F2[2],
        'F30':F3[0],'F31':F3[1],"F32":F3[2],
        'F40':F4[0],'F41':F4[1],"F42":F4[2],"error":error}
    if "uname" in request.session:
        return render(request,'reserveclass.html',context=data)
    else:
        return render(request,'schedule.html',context=data)
def viewreservedclasses(request):
    if "uname" in request.session:
        mail=request.session.get("umail")
        user=Client.objects.get(Client_email=mail)
        classes=Reservation.objects.all().filter(client=user)
        l1=[]
        for x in classes:
            item=Class.objects.get(Class_id=x.class_id)
            l1.append(item)
        print(l1)
        return render(request,'reservedclasses.html',{"l1":l1})
def deletereservation(request,id):
    classid=id[-2:]
    print("calling deletereservation")
    mail=request.session.get("umail")
    user=Client.objects.get(Client_email=mail)
    print("calling deletereservation")
    print(id)
    class1=Class.objects.get(Class_id=classid)
    temp=class1.Class_capacity
    class1.Class_capacity=temp+1
    class1.save()
    res=Reservation.objects.get(client=user,class_id=classid)
    res.delete()
    return viewreservedclasses(request)
def viewinstructors(request):
    instructors=Instructor.objects.all()
    return render(request,"viewinstructors.html",{'l1':instructors})
def gymreport(request):
    finichedmemeberhsip=[]
    currentmembership=[] ##valid memebsrhip
    B=[]   #basic membership
    S=[]   # standard memberhsip
    P=[]   #prmium menrship
    membership1=Membership.objects.all()
    for item in membership1 :
        print(item.expired)
        now=date.today()
        remaining=(item.expired-now).days
        if remaining>0:
            currentmembership.append(item)
        else:
            finichedmemeberhsip.append(item)
        type1=item.membershipType
        if type1=="B":
            B.append(item)
        elif type1=="S":
            S.append(item)
        else:
            P.append(time)
    return render(request,"gymreport.html",{"l1":finichedmemeberhsip,"l2":currentmembership})
def deletemembership(request,id):
    print("delete memebrship")
    print(id)
    mail=id[3:]
    print(mail)
    user=Client.objects.get(Client_email=mail)
    membership1=Membership.objects.get(client=user)
    membership1.delete()
    return gymreport(request)