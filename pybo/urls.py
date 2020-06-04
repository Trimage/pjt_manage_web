from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('utilities-color/', views.utilities_colors, name='utilities-colors'),
    path('utilities-border/', views.utilities_borders, name='utilities-borders'),
    path('utilities-animation/', views.utilities_animations, name='utilities-animations'),
    path('utilities-other/', views.utilities_other, name='utilities-other'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('page404/', views.page404, name='page404'),
    path('blank/', views.blank, name='blank'),

]