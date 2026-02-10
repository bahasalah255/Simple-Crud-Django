from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_list,name='student_list'),
    path('student_form/',views.student_form,name='student_from'),
    path('edit/<int:pk>/',views.editform,name='editform'),
    path('delete/<int:pk>/',views.delete,name='delete')
]