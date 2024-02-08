from django.contrib import admin
from django.urls import path
from E_Comm_app import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('register',views.register),
    path('login',views.check_login),
    path('logout',views.logout),
    path('blog/',views.blog),
    path('blog_single/',views.blog_single),
    path('checkout/',views.checkout),
    path('contact/',views.contact),
    path('faqs/',views.faq),
    path('help/',views.help),
    path('index_2/',views.index_2),
    path('payment/',views.payment),
    path('privacy/',views.privacy),
    path('product/',views.product),
    path('product_2/',views.product_2),
    path('single/',views.single),
    path('single_2',views.single_2),
    path('terms/',views.terms)
]