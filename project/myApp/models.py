from django.db import models

# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self):
        # 将父级返回的查询集过滤掉已经删除的数据isDelete=True
        return super(StudentManager,self).get_queryset().filter(isDelete=False)

    def createStudent(self,name,age,gender,contend,grade):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgrade = grade
        stu.sgender = gender
        stu.scontend = contend
        return stu


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    # class Meta:
    #     db_table = 'students'
    #     ordering = ['id']

    def __str__(self):
        return self.gname

class Students(models.Model):
    stuObj = models.Manager()
    stuObj1 = StudentManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey('Grades')

    def __str__(self):
        return self.sname

    # 定义类方法
    @classmethod
    def createStudent(cls,name,age,gender,contend,grade):
        stu = cls(sname=name,sage=age,sgender=gender,scontend=contend,sgrade=grade)
        return stu
