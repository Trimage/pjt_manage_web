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

    #날짜, 프로젝트번호, 진행주소, 프로젝트명

    date = models.DateField(unique=True, blank=False)
    num = models.IntegerField(unique=True, blank=False)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


#프로젝트 공사정보 테이블
class Project_construct(models.Model):

    # 형태, 규모(가로,세로,깊이), t/m, 토량(M3), 강재(t), 각 예측여부(규모, t/m, 토량, 강재)

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    shape = models.CharField(max_length=10)
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

    # 실(억), 총(억), 각 예측여부( 실(억), 총(억) )

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    real = models.DecimalField(max_digits=6, decimal_places=3)
    total = models.DecimalField(max_digits=6, decimal_places=3)
    real_expect = models.BooleanField(blank=False)
    total_expect = models.BooleanField(blank=False)


#프로젝트 업무일정보 테이블
class Project_schedule(models.Model):

    # 접수일, 계약일, 납품일

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    receive = models.DateField()
    contract = models.DateField()
    delivery = models.DateField()




#프로젝트 관련사정보 테이블
class Project_company(models.Model):

    # 시행사, 시공사, 하도급사, 설계사, 각 예측여부 (시행사, 시공사, 하도급사, 설계사)

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    execute = models.CharField(max_length=30)
    construct = models.CharField(max_length=30)
    subcontract = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
    execute_expect = models.BooleanField(blank=False)
    construct_expect = models.BooleanField(blank=False)
    subcontract_expect = models.BooleanField(blank=False)
    plan_expect = models.BooleanField(blank=False)




#프로젝트 회의 테이블
class Conference_Info(models.Model):

    #회의자료, 장소, 회의일, 회의시작시간, 회의종료시간

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    reference = models.BinaryField()
    place = models.CharField(max_length=30)
    date = models.DateField()
    cf_start = models.TimeField()
    cf_end = models.TimeField()



#프로젝트 회의내용 테이블
class Conference_content(models.Model):

    #작성자, 요약, 상세내용

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    writer = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    detail = models.TextField()



#프로젝트 회의 결재사항 테이블
class Conference_approve(models.Model):

    #직책, 성명

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    name = models.CharField(max_length=30)




#프로젝트 회의 방문자 테이블
class Conference_visitor(models.Model):

    #직책, 성명

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    name = models.CharField(max_length=30)



# 프로젝트 회의 참석자 테이블
class Conference_attender(models.Model):
    # 담당업무, 소속사, 직책, 성명, 연락처, 이메일주소

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    responsibility = models.CharField(max_length=20)
    agency = models.CharField(max_length=20)
    position = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=40)



# 프로젝트 회의 지적사항 테이블
class Conference_point(models.Model) :

    # 작성자, 지적사항
    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    writer = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)



# 프로젝트 회의 조치사항 테이블
class Conference_action(models.Model) :

    # 작성자, 조치사항
    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    writer = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
