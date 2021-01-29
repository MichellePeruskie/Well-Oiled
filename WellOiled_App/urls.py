from django.urls import path
from . import views
from django.conf import settings		
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('pricing', views.pricing),
    #Log/Reg
    path('register', views.register), 
    path('login', views.login),
    path('success', views.success),
    path ('logout', views.logout),
    #add/edit employee and qualifications
    path('renderemployeepage', views.renderemployeepage),
    # path('createemployee/<int:employee_id>', views.createemployee),
    path('createemployee', views.createemployee),
    # path('employee_successful_create', views.employee_successful_create),
    # path('employeeprofile', views.employeeprofile),
    path('employeeprofile/<int:employee_id>', views.employeeprofile),
    #edit profile 
    # path('viewprofile/<int:user_id>', views.viewprofile),
    path('updateprofile', views.updateprofile),
    path('viewemployees', views.viewemployees),
    path('updateemployee/<int:employee_id>', views.updateemployee),
    path('deleteemployee/<int:employee_id>', views.deleteemployee),
    #schedule job
    path('schedulejob', views.schedulejob),
    path('process', views.drop_pin),
    #docuementation
    path('viewdocs', views.viewdocs)
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
