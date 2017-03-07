from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render_to_response , render





def logout_view(request):
    logout(request)
    return render_to_response("html_templates/success.html")
    



def login_page(request):
    return render_to_response("html_templates/login.html")


def welcome_page(request):
    return render_to_response('html_templates/welcome.html')


def registration_page(request):
    return render_to_response('html_templates/registration.html')








def login(request):
    jsonobj=json.loads(request.body)
    print jsonobj

    user_name=jsonobj.get("user_name")
    password=jsonobj.get("password")

    if user_name == None:
        return HttpResponse(json.dumps({'validation':'Enter user name' , "status": False}), content_type="application/json")
    elif password == None:
        return HttpResponse(json.dumps({'validation':'Enter password first' , "status": False}), content_type="application/json")

    user = authenticate(username=user_name,password=password)

    if not user:
        return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")
    if not user.is_active:
        return HttpResponse(json.dumps({'validation':'The password is valid, but the account has been disabled!', "status":False}), content_type="application/json")

    login(request,user)
    return HttpResponse(json.dumps({'validation':'Login successfully', "status": True}), content_type="application/json")






def registration(request):
    reg=json.loads(request.body)
    print (reg)

    uname=reg.get("name")
    umobno=reg.get("mob_no")
    uemail=reg.get("email")

    user_name = reg.get('user_name')
    user_pswrd = reg.get('user_pswrd')
    cnfrm_pswrd = reg.get('cnfrm_pswrd')

    if len(user_pswrd) < 8:
        return HttpResponse(json.dumps({'validation':'please enter minimum 8 characters', "status":False}), content_type="application/json")

    if not user_pswrd == cnfrm_pswrd:
        return HttpResponse(json.dumps({'validation':'password not matched', "status":False}), content_type="application/json")

    if(user_name and uname) == None:
        return HttpResponse(json.dumps({'validation':'name is required', "status":False}), content_type="application/json")

    if User.objects.filter(username=user_name).exists():
        return HttpResponse(json.dumps({'validation':'username already exists', "status":False}), content_type="application/json")


    user = User.objects.create(username=user_name)
    user.set_password(user_pswrd)
    user.save()

    client=Client.objects.create(client_name=uname,mob_no=umobno,email=uemail,user=user)

    return  HttpResponse(json.dumps({'validation':'registraion succesfully', "status":True}), content_type="application")




