from django.urls import path

from inmakesapp import views

#urlpatterns = [
 #   path('',views.home,name='home'),
 #   path('about/',views.about,name='about'),
#  path('contact/',views.contact,name='contact'),
#    path('detail/',views.details,name='detail'),
 #   path('thank/',views.thanks,name='thank'),
#]

#
# urlpatterns=[
#    path('',views.home,name='home'),
#    path('opr/',views.opr,name='operations'),
# ]

urlpatterns=[
   path('',views.home1,name='home1'),

]