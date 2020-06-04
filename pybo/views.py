from django.shortcuts import render, get_object_or_404
from .models import Question



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

def tables(request) :
    return render(request, 'pybo/tables.html')

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)




# Create your views here.
