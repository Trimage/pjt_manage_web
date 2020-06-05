from django.db import models

class Question(models.Model) :
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return [self.subject]

class Answer(models.Model) :
    subject = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


#프로젝트 기본정보 테이블
class Project_Info(models.Model):
    date = models.DateField(unique=True, blank=False)
    num = models.IntegerField(unique=True, blank=False)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


#프로젝트 공사정보 테이블
class Project_construct(models.Model):
    idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    scale_width = models.IntegerField(blank=False)
    scale_length = models.IntegerField(blank=False)
    scale_depth = models.IntegerField(blank=False)
    tm = models.IntegerField()
    steel = models.IntegerField()
    earth = models.IntegerField()
    scale_expect = models.BooleanField(blank=False)
    tm_expect = models.BooleanField(blank=False)
    steel_expect = models.BooleanField(blank=False)
    earth_expect = models.BooleanField(blank=False)


#프로젝트 비용정보 테이블
class Project_cost(models.Model):
    idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    real = models.DecimalField(max_digits=6, decimal_places=3)
    total = models.DecimalField(max_digits=6, decimal_places=3)
    real_expect = models.BooleanField(blank=False)
    total_expect = models.BooleanField(blank=False)


#프로젝트 업무일정보 테이블
class Project_schedule(models.Model):
    idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    receive = models.DateField()
    contract = models.DateField()
    delivery = models.DateField()


#프로젝트 관련사정보 테이블
class Project_company(models.Model):
    idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    execute = models.CharField(max_length=30)
    construct = models.CharField(max_length=30)
    subcontract = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
    execute_expect = models.BooleanField(blank=False)
    construct_expect = models.BooleanField(blank=False)
    subcontract_expect = models.BooleanField(blank=False)
    plan_expect = models.BooleanField(blank=False)


# Create your models here.
