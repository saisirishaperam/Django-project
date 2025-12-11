"""
URL configuration for database_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import display_details,st_details, student_form, stu_update, st_del
from app1.views import teach_details, tea_form, teach_update, teach_del

urlpatterns = [
    path('admin/', admin.site.urls),
    # student urls
    path('',display_details, name='display1'),
    path('stu_d1', st_details, name='stu_d1'),
    path('stu_fom1', student_form, name='stu_fom1'),
    path('st_up/<int:id>/', stu_update, name='st_up'),
    path('stu_del/<int:id>/',st_del, name='stu_del'),

    # staff urls
    path('teach_de',teach_details, name='teach_de'),
    path('teach_form1',tea_form, name='teach_form1'),
    path('teach_up1/<int:id>/',teach_update, name='teach_up1'),
    path('teach_del1/<int:id>/',teach_del, name='teach_del1')

]
