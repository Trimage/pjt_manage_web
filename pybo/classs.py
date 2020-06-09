#사용되는 객체를 정리해놓은 py파일

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


class Conference_total :
    # 프로젝트 회의관련 객체

    def __init__(self):
        self.id = 0
        self.pjt_idx = 0
        self.num = 0
        self.date = ''
        self.place = ''
        self.cf_start = ''
        self.cf_end = ''
        self.reference = ''

        self.summary = ''
        self.detail = ''
        self.writer = ''

        self.point = []
        self.action = {}
        self.approve = {}
        self.visitor = []
        self.attender = []



class Attender :
    # 참석자 객체

    def __init__(self):
        self.id = 0
        self.pjt_idx = 0
        self.num = 0
        self.date = ''

        self.responsibility = ''
        self.agency = ''
        self.position = ''
        self.name = ''
        self.phone = ''
        self.email = ''


class Visitor :
    # 방문자 객체

    def __init__(self):
        self.id = 0
        self.pjt_idx = 0
        self.num = 0
        self.date = ''

        self.position = ''
        self.name = ''



class Approve :
    # 결제관련 객체

    def __init__(self):
        self.id = 0
        self.pjt_idx = 0
        self.cfr_idx_id = 0
        self.num = 0

        self.date = ''
        self.position = ''
        self.name = ''


class Point_out :
    # 지적사항 객체

    def __init__(self):
        self.id = 0
        self.pjt_idx = 0
        self.cfr_idx_id = 0
        self.num = 0

        self.date = ''
        self.position = ''
        self.name = ''


class Action:
    # 조치사항 객체

    def __init__(self):
        self.id = 0
        self.pjt_idx = 0
        self.cfr_idx_id = 0
        self.num = 0

        self.date = ''
        self.position = ''
        self.name = ''