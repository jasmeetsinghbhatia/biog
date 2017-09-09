from django.conf.urls import url
from jasmeetsingh import views

urlpatterns = [
    # url(r'status/', views.status, name='status'),
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]