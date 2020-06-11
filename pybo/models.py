from django.db import models

#프로젝트 기본정보 테이블
class Project_Info(models.Model):

    #날짜, 프로젝트번호, 진행주소, 프로젝트명

    date = models.DateField(blank=False)
    num = models.IntegerField(blank=False)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


#프로젝트 공사정보 테이블
class Project_Construct(models.Model):

    # 형태, 규모(가로,세로,깊이), t/m, 토량(M3), 강재(t), 각 예측여부(규모, t/m, 토량, 강재)

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    shape = models.CharField(max_length=10, null=True)
    scale_width = models.IntegerField(null=True)
    scale_length = models.IntegerField(null=True)
    scale_depth = models.IntegerField(null=True)
    tm = models.IntegerField(null=True)
    earth = models.IntegerField(null=True)
    steel = models.IntegerField(null=True)
    scale_expect = models.BooleanField(blank=False)
    tm_expect = models.BooleanField(blank=False)
    steel_expect = models.BooleanField(blank=False)
    earth_expect = models.BooleanField(blank=False)


#프로젝트 비용정보 테이블
class Project_Cost(models.Model):

    # 실(억), 총(억), 각 예측여부( 실(억), 총(억) )

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    real = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    real_expect = models.BooleanField(blank=False)
    total_expect = models.BooleanField(blank=False)


#프로젝트 업무일정보 테이블
class Project_Schedule(models.Model):

    # 접수일, 계약일, 납품일

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    receive = models.DateField()
    contract = models.DateField(null=True)
    delivery = models.DateField(null=True)




#프로젝트 관련사정보 테이블
class Project_Company(models.Model):

    # 시행사, 시공사, 하도급사, 설계사, 각 예측여부 (시행사, 시공사, 하도급사, 설계사)

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    execute = models.CharField(max_length=30, null=True)
    construct = models.CharField(max_length=30, null=True)
    subcontract = models.CharField(max_length=30, null=True)
    plan = models.CharField(max_length=30, null=True)
    execute_expect = models.BooleanField(blank=False)
    construct_expect = models.BooleanField(blank=False)
    subcontract_expect = models.BooleanField(blank=False)
    plan_expect = models.BooleanField(blank=False)




#프로젝트 회의 테이블
class Conference_Info(models.Model):

    #회의자료, 장소, 회의일, 회의시작시간, 회의종료시간

    pjt_idx = models.ForeignKey(Project_Info, on_delete=models.CASCADE)
    num = models.IntegerField(blank=False)
    reference = models.BinaryField(null=True)
    place = models.CharField(max_length=30)
    date = models.DateField()
    cf_start = models.TimeField()
    cf_end = models.TimeField()



#프로젝트 회의내용 테이블
class Conference_Content(models.Model):

    #작성자, 요약, 상세내용

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    writer = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    detail = models.TextField(null=True)



#프로젝트 회의 결재사항 테이블
class Conference_Approve(models.Model):

    #직책, 성명

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date = models.DateField()




#프로젝트 회의 방문자 테이블
class Conference_Visitor(models.Model):

    #직책, 성명

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    name = models.CharField(max_length=30)



# 프로젝트 회의 참석자 테이블
class Conference_Attender(models.Model):
    # 담당업무, 소속사, 직책, 성명, 연락처, 이메일주소

    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    responsibility = models.CharField(max_length=20)
    agency = models.CharField(max_length=20)
    position = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=40, null=True)



# 프로젝트 회의 지적사항 테이블
class Conference_Point(models.Model) :

    # 작성자, 지적사항
    cfr_idx = models.ForeignKey(Conference_Info, on_delete=models.CASCADE)
    num = models.IntegerField(blank=False)
    writer = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    date = models.DateTimeField()



# 프로젝트 회의 조치사항 테이블
class Conference_Action(models.Model) :

    # 작성자, 조치사항
    point_idx = models.ForeignKey(Conference_Point, on_delete=models.CASCADE)
    num = models.IntegerField(blank=False)
    writer = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    date = models.DateTimeField()
