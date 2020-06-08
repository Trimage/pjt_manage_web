from django.shortcuts import render, get_object_or_404
from .models import *

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



class Project_total :
    # 프로젝트 객체

    def __init__(self):
        self.id = 0
        self.date = ''
        self.num = 0
        self.address = ''
        self.name = ''

        self.shape = ''
        self.scale_width = 0
        self.scale_length = 0
        self.scale_depth = 0
        self.tm = 0
        self.steel = 0
        self.earth = 0

        self.real = 0
        self.total = 0

        self.receive = ''
        self.contract = ''
        self.delivery = ''

        self.execute = ''
        self.construct = ''
        self.subcontract = ''
        self.plan = ''


def tables(request) :

    #고유 id를 기준으로 내림차순 정렬하여 불러오기
    project_info = Project_Info.objects.order_by('-id')
    project_company = Project_company.objects.order_by('-pjt_idx_id')

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


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    try :
        question = get_object_or_404(Question, pk=question_id)
    except :
        return render(request, 'pybo/404.html')

    context = {'question': question}

    return render(request, 'pybo/question_detail.html', context)




# Create your views here.
