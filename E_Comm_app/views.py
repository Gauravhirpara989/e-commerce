from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.


def home(request):
    # slider = Slider.objects.all()

    # context = {"slider": slider}
    # print(slider)

    main_category = Main_Category.objects.all()
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()

    context = {"m_category": main_category, 
               "cat": category, "s_category": sub_category
               }
    return render(request, "index.html", context)


def register(request):
    if request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        name = request.POST.get("Name")
        role = request.POST.get("role")
        user_info = User(Email_id=email, Password=password, Name=name, Role=role)
        user_info.save()
        messages.success(request, "Registration Successfully")
        return redirect(home)
    else:
        messages.error(request, "Unable Registration")
        return render(home)


def check_login(request):
    email = request.POST["Email"]
    password = request.POST["Password"]
    try:
        query = User.objects.get(Email_id=email, Password=password)
        request.session["u_email"] = query.Email_id
        request.session["u_id"] = query.id
    except User.DoesNotExist:
        query = None

    if query is not None:
        messages.success(request, "Login Successfully")
        return render(request, "index.html")
    else:
        messages.info(request, "Account does not exist!! Please sign in")


def logout(request):
    try:
        del request.session["u_email"]
        del request.session["u_id"]

        messages.success(request,"Logout Successfully")
    except:
        pass
    return redirect(home)

def Add_product(request):
    return render(request,"Add_product.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def blog_single(request):
    return render(request, "blog-single.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faqs.html")


def help(request):
    return render(request, "help.html")


def index_2(request):
    return render(request, "index-2.html")


def payment(request):
    return render(request, "payment.html")


def privacy(request):
    return render(request, "privacy.html")


def product(request):
    return render(request, "product.html")


def product_2(request):
    return render(request, "product2.html")


def single(request):
    return render(request, "single.html")


def single_2(request):
    return render(request, "single2.html")


def terms(request):
    return render(request, "terms.html")
