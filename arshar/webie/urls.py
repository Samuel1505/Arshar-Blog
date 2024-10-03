from django.contrib import admin
from django.urls import path
from webie.views import homepageview, aboutpageview, contactpageview,  inner_pageview, portfolio_detailspageview, servicepageview

urlpatterns = [
    path("",homepageview.as_view(),name="home"),
    path("about",aboutpageview.as_view(),name="about"),
    path("contact",contactpageview.as_view(),name="contact"),
    path("inner_page",inner_pageview.as_view(),name="inner_page"),
    path("portfolio_details",portfolio_detailspageview.as_view(),name="portfolio_details"),
    path("service",servicepageview.as_view(),name="services"),
   
]