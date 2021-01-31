from django.shortcuts import render,redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage
from . models import *
from .forms import *
from django.forms import ModelForm
from .filters import  HomeFilter
from django.contrib.auth.models import User,auth
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages


# Create your views here.

def home(request):

    from .models import image
    users = image.objects.all()
    lists = image.objects.all()
    myfilter=HomeFilter(request.GET,queryset=lists)
    context={'filter':myfilter,'users':users} 
    return render(request,'upload1_pic.html',context)
@login_required(login_url="login")
def accounts(request):
    from .models import image
    users = image.objects.all()
    pics=userprofile.objects.all()
    customer = request.user.userprofile
    form = customerForm(instance=customer)
    phoneform=PhoneForm()
    
    form =customerForm(request.POST,request.FILES,instance=customer)
    
    if request.is_ajax():
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success'})
            
    context={'users':users,'form':form,'pics':pics,'phoneform':phoneform} 
    return render(request,'account.html',context)


def upload(request):

    if request.method=='POST':

        p = request.FILES['image']
        temp = request.POST['pro_type']
        sam = request.POST['pro_des']
        c=request.POST['pro_con']
        L=request.POST['pro_Loc']
        pr=request.POST['pro_price']
        lat=request.POST['user_lat']
        log=request.POST['user_log']


        if (not request.POST['user_lat']):

            user=image(img=p,name=temp,pro_type=sam,pro_con=c,pro_Loc=L,pro_price=pr)
            user.auther=request.user
            print(user.auther)
            user.save();
            return redirect("/")
        else:

         
            user=image(img=p,name=temp,pro_type=sam,pro_con=c,pro_Loc=L,pro_price=pr,latitude=lat,logitude=log)
            user.auther=request.user
            print(user.auther)
            user.save();
            return redirect("/")
        


    return render(request,'upload1_pic.html')

@login_required(login_url="login")
def cart(request,pk):

  
    if request.POST:

        message=request.POST['message']
        user_id=request.POST['user_id']
        replay=request.POST.get('com_id')
        
        product = pk
        comment_qs=None
        if replay:

            comment_qs=comment.objects.all().get(id=replay)

        query=comment(message=message)
        query.replay=comment_qs
        query.product_id=product
        query.user_id_id=user_id
        query.save()
       
    var = image.objects.get(id=pk)
    is_liked=False  
    if var.likes.filter(id=request.user.id).exists():
        is_liked=True
    comments=comment.objects.all().filter(product=pk,replay=None) 
    var_id=var.auther.id
 
    temp={'var':var,'comments':comments,'likes_count':var.likes.count(),'is_liked':is_liked,'var_id':var_id}
    if request.is_ajax():
    
        html=render_to_string('comment.html',temp,request=request)
       
        return JsonResponse({'form':html})

    return render(request,"cart.html",temp)

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request,"Username taken")
                
                
                return redirect('register')
            elif User.objects.filter(email=email).exists():

                # messages.error(request,"Email already taken")
            
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')


        else:
            
            messages.error(request,'password not matching..')    
        return redirect('register')
        
        
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            
            # messages.error(request,"Invalid account")
            return redirect('login')

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="login")
def like_post(request):
  
    temp=get_object_or_404(image,id=(request.POST.get('id')))
   
    is_liked=False
 
    if temp.likes.filter(id=request.user.id).exists():
        temp.likes.remove(request.user) 
        is_liked=False

    else:
        temp.likes.add(request.user)
        is_liked=True
    context={
        'var':temp,
        'is_liked':is_liked,
        'likes_count':temp.likes.count()
    }
    if request.is_ajax():
    
        html=render_to_string('like-section.html',context,request=request)
        print(html)
        return JsonResponse({'form':html})
   
def remove(request,pk):
    pro=image.objects.get(id=pk)
    pro.delete()
    return redirect('accounts')


def edit(request,pk):
    var=image.objects.get(id=pk)
    form=TaskForm(instance=var)
    if request.method=='POST':
        form = TaskForm(request.POST,instance=var)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    context={'form':form}

    return render(request,'profile-edit.html',context)


@login_required(login_url="login")
def sellproduct(request):
    
    return render(request,'sellproduct.html')


def messages(request,pk):

    
    comments=comment.objects.all().filter(product=pk)
    pro_id=pk
    var=[]
    for com in comments:
        if request.user.id!=com.user_id.id:
            var.append(com)
            
    phone_no=userphone.objects.all()


    context={'comments':comments,'phone_no':phone_no,'var':var,'pro_id':pro_id}

    
    return render(request,'chat.html',context)


  
def accountphone(request):

    if request.method=='POST':

        form=PhoneForm(request.POST)
        if form.is_valid():

            profile=form.save(commit=False)
            profile.user=request.user

            profile.save();

            return redirect('/')
    

    return render(request,'account.html')
