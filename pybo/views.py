from django.shortcuts import render, get_object_or_404
from .models import *
from .classs import *

def index(request) :
    return render(request, 'pybo/index.html')

def buttons(request) :
    return render(request, 'pybo/buttons.html')

def cards(request) :
    return render(request, 'pybo/cards.html')

def utilities_colors(request) :
    return render(request, 'pybo/utilities-color.html')

def utilities_borders(request) :
    return render(request, 'pybo/utilities-border.html')

def utilities_animations(request) :
    return render(request, 'pybo/utilities-animation.html')

def utilities_other(request) :
    return render(request, 'pybo/utilities-other.html')

def login(request):
    return render(request, 'pybo/login.html')

def register(request):
    return render(request, 'pybo/register.html')

def forgot_password(request):
    return render(request, 'pybo/forgot-password.html')

def page404(request):
    return render(request, 'pybo/404.html')

def blank(request):
    return render(request, 'pybo/blank.html')

def charts(request) :
    return render(request, 'pybo/charts.html')



#tables.html 관련 함수
def tables(request) :

    #고유 id를 기준으로 내림차순 정렬하여 불러오기
    project_info = Project_Info.objects.order_by('-id')
    project_company = Project_Company.objects.order_by('-pjt_idx_id')

    #페이지로 전달되는 데이터로써, 출력할 프로젝트정보를 딕셔너리 형태로 저장 (key는 pjt_id)
    project_data = {}

    for project in project_info :

        #Project_total 클래스 인스턴트 형성
        pjt = Project_total()

        #Jquery형으로 불러온 기본 프로젝트 데이터를 인스턴트 내 각 필드에 저장
        pjt.id = project.id
        pjt.date = project.date
        pjt.num = project.num
        pjt.address = project.address
        pjt.name = project.name

        #project_data에 pjt.id를 키 값으로 하여 형성된 인스턴트 저장
        project_data[pjt.id] = pjt


    for project in project_company :
        # Jquery형으로 불러온 프로젝트 관련 회사 데이터를 인스턴트 내 각 필드에 저장
        project_data[project.pjt_idx_id].execute = project.execute
        project_data[project.pjt_idx_id].construct = project.construct
        project_data[project.pjt_idx_id].subcontract = project.subcontract
        project_data[project.pjt_idx_id].plan = project.plan

        # DB내 확정유무에 따라 미확정인 경우 회사이름 양옆에 괄호를 추가
        if project.execute_expect == False :
            project_data[project.pjt_idx_id].execute = \
                '(' + project_data[project.pjt_idx_id].execute[:] + ')'

        if project.construct_expect == False :
            project_data[project.pjt_idx_id].construct = \
                '(' + project_data[project.pjt_idx_id].construct[:] + ')'

        if project.subcontract_expect == False :
            project_data[project.pjt_idx_id].subcontract = \
                '(' + project_data[project.pjt_idx_id].subcontract[:] + ')'

        if project.plan_expect == False :
            project_data[project.pjt_idx_id].plan = \
                '(' + project_data[project.pjt_idx_id].plan[:] + ')'


    context = {'project_list' : project_data}
    return render(request, 'pybo/tables.html', context)


# url 'tables/게시글번호' 관련 함수
def detail(request, pjt_id):

    try :
        project_info = get_object_or_404(Project_Info, pk=pjt_id)
    except :
        return render(request, 'pybo/404.html')

    try :
        project_construct = Project_Construct.objects.get(pjt_idx_id=pjt_id)
    except :
        project_construct = Project_total()

    try :
        project_company = Project_Company.objects.get(pjt_idx_id=pjt_id)
    except :
        project_company = Project_total()


    try :
        project_cost = Project_Cost.objects.get(pjt_idx_id=pjt_id)
    except :
        project_cost = Project_total()

    try :
        project_schedule = Project_Schedule.objects.get(pjt_idx_id=pjt_id)
    except :
        project_schedule = Project_total()


    pjt = Project_total()

    pjt.id = project_info.id
    pjt.date = project_info.date
    pjt.num = project_info.num
    pjt.address = project_info.address
    pjt.name = project_info.name

    pjt.shape = project_construct.shape
    pjt.scale_width = project_construct.scale_width
    pjt.scale_length = project_construct.scale_length
    pjt.scale_depth = project_construct.scale_depth
    pjt.tm = project_construct.tm
    pjt.steel = project_construct.steel
    pjt.earth = project_construct.earth

    pjt.real = project_cost.real
    pjt.total = project_cost.total

    pjt.execute = project_company.execute
    pjt.construct = project_company.construct
    pjt.subcontract = project_company.subcontract
    pjt.plan = project_company.plan

    pjt.receive = project_schedule.receive
    pjt.contract = project_schedule.contract
    pjt.delivery = project_schedule.delivery


    cfr_list = []


    conference_info = Conference_Info.objects.filter(pjt_idx_id=pjt_id).order_by('-num')

    for conference in conference_info:
        cfr = Conference_total()

        cfr.id = conference.id
        cfr.pjt_idx = conference.pjt_idx_id
        cfr.num = conference.num
        cfr.date = conference.date
        cfr.place = conference.place
        cfr.cf_start = conference.cf_start
        cfr.cf_end = conference.cf_end
        cfr.reference = conference.reference

        try :
            conference_content = Conference_Content.objects.get(cfr_idx_id=cfr.id)
        except :
            conference_content = Conference_total()

        try:
            conference_attender = Conference_Attender.objects.filter(cfr_idx_id=cfr.id).order_by('responsibility')
        except :
            conference_attender = Attender()

        try:
            conference_visitor = Conference_Visitor.objects.filter(cfr_idx_id=cfr.id).order_by('position')
        except:
            conference_visitor = Visitor()

        try:
            conference_approve = Conference_Approve.objects.filter(cfr_idx_id=cfr.id).order_by('position')
        except:
            conference_approve = Approve()

        cfr.summary = conference_content.summary
        cfr.detail = conference_content.detail
        cfr.writer = conference_content.writer

        cfr.attender.append(conference_attender)
        cfr.visitor.append(conference_visitor)

        for approve in conference_approve :
            cfr.approve[approve.id] = approve


        try :
            conference_point = Conference_Point.objects.filter(cfr_idx_id=cfr.id).order_by('-num')
        except:
            conference_point = Point_out()

        for point in conference_point :
            cfr.point[point.id] = point

            try :
                conference_action = Conference_Action.objects.filter(point_idx_id=point.id).order_by('-num')
            except :
                conference_action = Action()

            for action in conference_action :
                cfr.action[point.id] = action

        cfr_list.append(cfr)


    context = {'project': pjt, 'conference_list' : cfr_list}

    return render(request, 'pybo/question_detail.html', context)


