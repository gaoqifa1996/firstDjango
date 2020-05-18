from django.contrib import admin

# Register your models here.

# 先引入
from .models import Grades,Students

# 创建班级时，同时创建学生
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    # 关联上上上面类
    inlines = [StudentsInfo]

    # 列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # 添加修改页属性
    # fields = ['gname','gdate','ggirlnum','gboynum','isDelete']
    fieldsets = [('nums',{'fields':['ggirlnum','gboynum']}),
                 ('base',{'fields':['gname','gdate','isDelete']}),
                 ]
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'
    # 列表页属性
    list_display = ['pk', 'sname', gender, 'sage', 'sgrade', 'scontend','isDelete']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 5

    # 执行动作位置
    actions_on_top = False
    actions_on_bottom = True

    # 添加修改页属性
    fields = ['sname', 'sgender', 'sage', 'sgrade', 'scontend','isDelete']
    # fieldsets = [('nums', {'fields': ['ggirlnum', 'gboynum']}),
    #              ('base', {'fields': ['gname', 'gdate', 'isDelete']}),
    #              ]




# 再注册，注册完成即可展示
admin.site.register(Grades,GradesAdmin) # 使用自定义管理页面类时 需要将类名作为参数引入
# admin.site.register(Students,StudentsAdmin)
