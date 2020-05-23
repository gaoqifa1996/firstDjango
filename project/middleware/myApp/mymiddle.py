#!-- encoding=utf8 --#
# date {2020/5/23}

from django.utils.deprecation import MiddlewareMixin

class MyMiddle(MiddlewareMixin):
    def process_request(self,request):
        print('我的中间件，获取参数a=',request.GET.get('a'))
