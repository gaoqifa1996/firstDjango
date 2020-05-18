#!-- encoding=utf8 --#
# date {2020/5/13}

from django.conf.urls import url
from myApp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/$',views.returnNum),
    url(r'^grades/$',views.gradesViews),
    url(r'^students/$',views.studentsView),
    url(r'^students2/$',views.studentsView2),
    url(r'^students3/(\d+)$',views.student_page),
    url(r'grades/(\d+)/$',views.gradesStudents),
    url(r'createstudent/$',views.createStudent),
    url(r'createstudent2/$',views.createStudent2),
    url(r'^showregist/$',views.showregist),
    url(r'^showregist/regist/$',views.regist),
    url(r'^cookietext/$',views.cookietext),
    url(r'^regrict1/$',views.regrict1),
    url(r'^regrict2/$', views.regrict2),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^logout1',views.logout1),
    url(r'^index/$',views.index),
]

