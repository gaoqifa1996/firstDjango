from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myApp.models import Grades, Students


def index(request):
    return HttpResponse('thin is a good project')

def returnNum(request,num):
    return HttpResponse('get from bower is %s'%num)


def gradesViews(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板 模板再渲染页面，再将渲染好的页面传递给浏览器
    return render(request,'myApp/grades.html',{'grades':gradesList})


def studentsView(request):
    studentsList = Students.stuObj.all()
    return render(request,'myApp/students.html',{'students':studentsList})

def studentsView2(request):
    # 限制查询集的条数
    studentsList = Students.stuObj.all()[0:4]
    return render(request,'myApp/students.html',{'students':studentsList})

def student_page(request,page):
    '''
    :param request:
    :return:
    0-4 5-8 9-12
    1   2   3
    '''
    page = int(page)
    studentsList = Students.stuObj.all()[(page-1)*4:page*4]
    return render(request, 'myApp/students.html', {'students': studentsList})


def gradesStudents(request,num):
    # 获取对应班级对象
    grade = Grades.objects.get(pk=num)
    # 获取班级对象的学生对象列表
    studentsList = grade.students_set.all()

    return render(request,'myApp/students.html',{'students':studentsList})


def createStudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent('刘德华',24,True,'我是华仔',grade)
    stu.save()
    return HttpResponse('create success')


def createStudent2(request):
    grade = Grades.objects.get(pk=3)
    stu = Students.stuObj1.createStudent('张学友',34,True,'我是学友',grade)
    stu.save()
    return HttpResponse('create2 success')


def showregist(request):
    print(request.POST)
    return render(request,'myApp/regist.html')

def regist(request):
    print(request.POST)
    return HttpResponse(request.POST)

# cookie
def cookietext(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write('<h1>'+cookie['cookieset']+'</h1>')
    # cookie = res.set_cookie('cookieset','success')
    return res



# 重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def regrict1(request):
    # return HttpResponseRedirect('/regrict2')

    return redirect('/regrict2')

def regrict2(request):
    return HttpResponse('hello')



# session
def main(request):
    name = request.session.get('name','游客')
    return render(request,'myApp/main.html',{'name':name})


def login(request):
    return render(request,'myApp/login.html')

def showmain(request):
    data = request.POST
    name = data.get('name')
    print(name)
    request.session['name'] = name
    request.session.set_expiry(10)  # 设置session的保存时间 单位秒
    return redirect('/main')

from django.contrib.auth import logout
def logout1(request):
    logout(request)
    # 或者
    # request.session.clear()
    # request.session.flush()
    return redirect('/main')


def index(request):
    return render(request,'myApp/index.html',{'num':10,'str':'hello'})


def good(request,id):
    return render(request,'myApp/good.html',{'num':id})


def frombase(request):
    return render(request,'myApp/form.html')



