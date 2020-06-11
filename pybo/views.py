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
    project_construct = Project_Construct.objects.order_by('-pjt_idx_id')
    project_cost = Project_Cost.objects.order_by('-pjt_idx_id')
    project_schedule = Project_Schedule.objects.order_by('-pjt_idx_id')


    #페이지로 전달되는 데이터로써, 출력할 프로젝트정보를 딕셔너리 형태로 저장 (key는 pjt_id)
    project_data = {}

    for project in project_info :

        #Project_total 클래스 인스턴트 형성
        pjt = Project_total()

        #Jquery형으로 불러온 기본 프로젝트 데이터를 인스턴트 내 각 필드에 저장
        pjt.id = project.id
        pjt.date = project.date
        pjt.num = ("000" + str(project.num))[-3:]
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


    for project in project_construct :
        # Jquery형으로 불러온 프로젝트 관련 회사 데이터를 인스턴트 내 각 필드에 저장
        project_data[project.pjt_idx_id].scale_width = project.scale_width
        project_data[project.pjt_idx_id].scale_length = project.scale_length
        project_data[project.pjt_idx_id].scale_depth = project.scale_depth

        project_data[project.pjt_idx_id].tm = project.tm
        project_data[project.pjt_idx_id].steel = project.steel
        project_data[project.pjt_idx_id].earth = project.earth

        if project.scale_expect == False:
            project_data[project.pjt_idx_id].scale_width = '(' + str(project.tm) + ')'
            project_data[project.pjt_idx_id].scale_length = '(' + str(project.steel) + ')'
            project_data[project.pjt_idx_id].scale_depth = '(' + str(project.earth) + ')'

        if project.tm_expect == False :
            project_data[project.pjt_idx_id].tm = \
                '(' + str(project_data[project.pjt_idx_id].tm) + ')'

        if project.steel_expect == False :
            project_data[project.pjt_idx_id].steel = \
                '(' + str(project_data[project.pjt_idx_id].steel) + ')'

        if project.earth_expect == False :
            project_data[project.pjt_idx_id].earth = \
                '(' + str(project_data[project.pjt_idx_id].earth) + ')'



    for project in project_cost :
        # Jquery형으로 불러온 프로젝트 관련 회사 데이터를 인스턴트 내 각 필드에 저장
        project_data[project.pjt_idx_id].real = round(project.real,2)
        project_data[project.pjt_idx_id].total = round(project.total,2)

        # DB내 확정유무에 따라 미확정인 경우 회사이름 양옆에 괄호를 추가
        if project.real_expect == False :
            project_data[project.pjt_idx_id].real = \
                '(' + str(round(project_data[project.pjt_idx_id].real,2)) + ')'

        if project.total_expect == False :
            project_data[project.pjt_idx_id].total = \
                '(' + str(round(project_data[project.pjt_idx_id].total,2)) + ')'



    for project in project_schedule :
        # Jquery형으로 불러온 프로젝트 관련 회사 데이터를 인스턴트 내 각 필드에 저장
        project_data[project.pjt_idx_id].receive = project.receive
        project_data[project.pjt_idx_id].contract = project.contract
        project_data[project.pjt_idx_id].delivery = project.delivery



    #고유 id를 기준으로 내림차순 정렬하여 불러오기
    conference_info = Conference_Info.objects.order_by('-id')
    conference_content = Conference_Content.objects.order_by('-cfr_idx_id')


    #페이지로 전달되는 데이터로써, 출력할 프로젝트정보를 딕셔너리 형태로 저장 (key는 pjt_id)
    conference_data = {}

    for conference in conference_info :

        #Project_total 클래스 인스턴트 형성n
        cfr = Conference_total()

        #Jquery형으로 불러온 기본 프로젝트 데이터를 인스턴트 내 각 필드에 저장
        cfr.pjt_idx = conference.pjt_idx_id
        cfr.department = conference.department

        #project_data에 pjt.id를 키 값으로 하여 형성된 인스턴트 저장
        conference_data[conference.pjt_idx_id] = cfr

    for conference in conference_content:
        # Jquery형으로 불러온 프로젝트 관련 회사 데이터를 인스턴트 내 각 필드에 저장
        conference_data[project.pjt_idx_id].summary = conference.summary
        conference_data[project.pjt_idx_id].stage = conference.stage

    context = {'project_list' : project_data, 'conference_list' : conference_data }
    return render(request, 'pybo/tables.html', context)


# url 'tables/게시글번호' 관련 함수
def detail(request, pjt_id):

    pjt = Project_total()

    try :
        project_info = get_object_or_404(Project_Info, pk=pjt_id)

        pjt.id = project_info.id
        pjt.date = project_info.date
        pjt.num = ("000" + str(project_info.num))[-3:]
        pjt.address = project_info.address
        pjt.name = project_info.name

    except :
        return render(request, 'pybo/404.html')


    try :
        project_construct = Project_Construct.objects.get(pjt_idx_id=pjt_id)


        pjt.shape = project_construct.shape
        pjt.scale_width = project_construct.scale_width
        pjt.scale_length = project_construct.scale_length
        pjt.scale_depth = project_construct.scale_depth
        pjt.tm = project_construct.tm
        pjt.steel = project_construct.steel
        pjt.earth = project_construct.earth

        # DB내 확정유무에 따라 미확정인 경우 공사관련 정보 양옆에 괄호를 추가
        if project_construct.scale_expect == False:
            pjt.scale_width = '(' + str(project_construct.scale_width) + ')'
            pjt.scale_length = '(' + str(project_construct.scale_length) + ')'
            pjt.scale_depth = '(' + str(project_construct.scale_depth) + ')'

        if project_construct.tm_expect == False:
            pjt.tm = '(' + str(project_construct.tm) + ')'

        if project_construct.steel_expect == False:
            pjt.steel = '(' + str(project_construct.steel) + ')'

        if project_construct.earth_expect == False:
            pjt.earth = '(' + str(project_construct.earth) + ')'

    except :
        print("project_construct가 없습니다.")


    try :
        project_company = Project_Company.objects.get(pjt_idx_id=pjt_id)

        pjt.execute = project_company.execute
        pjt.construct = project_company.construct
        pjt.subcontract = project_company.subcontract
        pjt.plan = project_company.plan

        # DB내 확정유무에 따라 미확정인 경우 회사이름 양옆에 괄호를 추가
        if project_company.execute_expect == False :
            pjt.execute = '(' + project_company.execute[:] + ')'

        if project_company.construct_expect == False :
            pjt.construct = '(' + project_company.construct[:] + ')'

        if project_company.subcontract_expect == False :
            pjt.subcontract = '(' + project_company.subcontract[:] + ')'

        if project_company.plan_expect == False :
            pjt.plan = '(' + project_company.plan[:] + ')'

    except :
        print("project_company가 없습니다.")


    try :
        project_cost = Project_Cost.objects.get(pjt_idx_id=pjt_id)

        if project_cost.real_expect :
            pjt.real = round(project_cost.real,2)
        else :
            pjt.real = '(' + str(round(project_cost.real,2)) + ')'

        if project_cost.total_expect :
            pjt.total = round(project_cost.total,2)
        else :
            pjt.total = '(' + str(round(project_cost.total,2)) + ')'

    except :
        print("project_cost가 없습니다.")


    try :
        project_schedule = Project_Schedule.objects.get(pjt_idx_id=pjt_id)

        pjt.receive = project_schedule.receive
        pjt.contract = project_schedule.contract
        pjt.delivery = project_schedule.delivery

    except :
        print("project_schedule이 없습니다.")






    cfr_list = []


    try :
        conference_info = Conference_Info.objects.filter(pjt_idx_id=pjt_id).order_by('-date')
    except :
        print("conference_info가 없습니다.")


    for conference in conference_info:
        cfr = Conference_total()

        cfr.id = conference.id
        cfr.pjt_idx = conference.pjt_idx_id
        cfr.num = conference.num
        cfr.department = conference.department
        cfr.date = conference.date
        cfr.place = conference.place
        cfr.cf_start = conference.cf_start
        cfr.cf_end = conference.cf_end
        cfr.reference = conference.reference


        try :
            conference_content = Conference_Content.objects.get(cfr_idx_id=conference.id)
            cfr.stage = conference_content.stage
            cfr.summary = conference_content.summary
            cfr.detail = conference_content.detail
            cfr.writer = conference_content.writer

        except :
            print("conference_content가 없습니다.")


        try:
            conference_attender = Conference_Attender.objects.filter(cfr_idx_id=conference.id).order_by('responsibility')

            for attender in conference_attender :
                atd = Attender()

                atd.responsibility = attender.responsibility
                atd.agency = attender.agency
                atd.position = attender.position
                atd.name = attender.name
                atd.phone = attender.phone
                atd.email = attender.email

                cfr.attender.append(atd)

        except :
            print("conference_attender가 없습니다.")


        try:
            conference_visitor = Conference_Visitor.objects.filter(cfr_idx_id=conference.id).order_by('position')

            for visit in conference_visitor :
                vs = Visitor()

                vs.position = visit.position
                vs.name = visit.name

                cfr.visitor.append(vs)

        except:
            print("conference_visitor가 없습니다.")


        try:
            conference_approve = Conference_Approve.objects.filter(cfr_idx_id=conference.id).order_by('position')

            for approve in conference_approve :
                aprv = Approve()

                aprv.position = approve.position
                aprv.name = approve.name
                aprv.date = approve.date

                cfr.approve[approve.position] = aprv

        except:
            print("conference_approve가 없습니다.")




        try :
            conference_point = Conference_Point.objects.filter(cfr_idx_id=conference.id).order_by('-date')

            for point in conference_point:
                pt = Point_out()

                pt.id = point.id
                pt.writer = point.writer
                pt.summary = point.summary
                pt.date = point.date

                cfr.point.append(pt)

                try:
                    conference_action = Conference_Action.objects.filter(point_idx_id=point.id).order_by('-date')

                    action_list = []

                    for action in conference_action :
                        act = Action()

                        act.id = action.id
                        act.point_idx_id = action.point_idx_id
                        act.writer = action.writer
                        act.summary = action.summary
                        act.date = action.date

                        action_list.append(act)


                    cfr.action[point.id] = action_list

                except:
                    print("conference_action이 없습니다.")

        except:
            print("conference_point가 없습니다.")


        cfr_list.append(cfr)


    context = {'project': pjt, 'conference_list' : cfr_list}

    return render(request, 'pybo/project_detail.html', context)


