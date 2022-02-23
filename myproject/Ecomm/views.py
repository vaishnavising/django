from distutils.command.upload import upload
from tabnanny import check
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
from .models import Category,product,order,register_data

# cart increase and decrease condition of if else.

def index(request):
 
    if request.method =="POST":
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id =request.session.get('cart')
        if cart_id:
            quantity= cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id]= quantity-1
                else:
                    cart_id[product_id]= quantity+1
            else:
                cart_id[product_id] =1     

        else:
            cart_id={}
            cart_id[product_id] = 1
        # print(cart_id)  
        request.session['cart']=cart_id
        print(request.session['cart'])


    path = product.objects.all()
    cat = Category.objects.all()
    cat_id =request.GET.get('category')
    if cat_id:
        path= product.objects.filter(category_id=cat_id)
    else:
        path = product.objects.all() 

    return render(request,'home.html',{'path':path,'cate':cat})
    
def aboutus(request):
    return render(request,'aboutus')   


    # fetch_info =register.objects.all()

#    for val in fetch_info:
#        print(val.firstname)

def contact(request):
    return render(request,'contact.html')

def save(request):    
    if request.method =='POST':
         firstname =request.POST.get('fname')
         lname =request.POST.get('lastname')
         mobile =request.POST.get('mobile')
         email = request.POST.get('email')
         password = request.POST.get('password')
         gender =request.POST.get('gender')
         print(firstname)
         save_info =register_data(firstname=firstname,lastname=lname,
                              mobile=mobile,password=password,
                              gender=gender,email=email)
         save_info.save()
         return redirect('home')
    else:
        
        return HttpResponse('login')

def handlelogin(request):

        if request.method =='POST':
         email = request.POST.get('email')
         password = request.POST.get('password')

         print(email)
        #  save_info =register (email=email,password=password)

        #  save_info.save()
         return redirect(request,'login.html')   

def register_info(request):
    if request.method == "POST":   
       firstname =request.POST.get('firstname')
       lastname =request.POST.get('lastname')
       mobile =request.POST.get('mobile')
       email = request.POST.get('email')
       password = request.POST.get('password')
       gender = request.POST.get('gender')
       
       store_data = register_data(firstname=firstname,lastname=lastname,
       mobile=mobile,gender=gender,email=email,password=make_password(password))

       store_data.save()

    return HttpResponse("success")
                                           
    
# def login_info(request):
#     error_msg = None
#     if request.method == "POST":   
#        email = request.POST.get('email')
#        password = request.POST.get('password')

#        try: 
#            fetch_email = register_data.objects.get(email=email)

#        except:
#            error_msg = "invalid Email"
#            return render(request,'home.html',{'error_msg': error_msg})

#        return HttpResponse(fetch_email)

#        return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        store_data = register_data(firstname=fname, lastname=lname,
                                   mobile=mobile, gender=gender, email=email, password=make_password(password))

        store_data.save()

        return redirect('home')


def login_info(request):
    error_msg = None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)
        try:
            fetch_email = register_data.objects.get(email=email)
            if (fetch_email.email == email):
                flag = check_password(password,fetch_email.password)
                print(flag)
                if flag:
                    request.session['email'] = fetch_email.email
                    print(fetch_email.email)
                    request.session['customer_id']= fetch_email.id
                    return redirect('home')
                else:
                    error_msg = "Please Enter valid password"
                    return render(request, 'home.html', {'error_msg': error_msg})
        except:
            error_msg = "Please Enter valid  Email"
            return render(request, 'home.html', {'error_msg': error_msg})

        return HttpResponse(fetch_email.email, fetch_email.password)


def logout(request):
    request.session.clear()
    return redirect('home')

def cart(request):

    ids = list(request.session.get('cart').keys())
    cart_pro =product.objects.filter(id__in =ids)
    print(cart_pro)
    return render(request,'cart.html',{'cart_pro':cart_pro})   

def checkout(request):
    if request.method =="POST":
        address =request.POST.get("address")
        mobile =request.POST.get("mobile")
        customer_id =request.session.get('customer_id')
        cart =request.session.get('cart')
        products =product.objects.filter(id__in=list(cart.keys()))

    for pro in products:
        save_order_dtls = order(
             customer =register_data(id=customer_id),
             product=pro,
             price=pro.price,
             quality = cart.get(str(pro.id)),
             address =  address,
             phone =mobile)

        # print(address,mobile,cart,customer_id,products)
        save_order_dtls.save()  
        request.session['cart']={}
    return redirect('cart')  

def order_dtls(request):
    customer =request.session.get('customer_id')
    ord_Dtls = order.objects.filter(customer=customer).order_by('-date')

    tp =0
    for i in ord_Dtls:

        tp =tp+(i.price*i.quality)

    return render(request,'order.html',{'order_dtls':ord_Dtls, 'tp': tp}) 