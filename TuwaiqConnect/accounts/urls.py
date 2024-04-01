from django.urls import path
from . import views


app_name="accounts"

urlpatterns = [
    
    path('student/register',views.student_register,name="student_register"),
    path ("staff/register",views.staff_register,name="staff_register"),
    path("orgnaization/register",views.orgnaization_register,name="orgnaization_register")
]