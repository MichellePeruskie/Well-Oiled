from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import*
from django.core.files.storage import FileSystemStorage

# Create your views here.
def homepage (request):
    context= {
        # 'register-users':Register.objects.all()
        'user': Register.objects.all()
    }
    return render (request, "homepage.html", context)

def login (request):
    user=Register.objects.filter(email=request.POST['email']) #go over this section, not sure it's correct
    password=request.POST['pw']
    if user: 
        user=user[0]
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['user_id'] = user.id 
            request.session['username'] = f"{user.first_name} {user.last_name}" 
            return redirect('/success')
    return redirect('/')

def register (request):
    errors=Register.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['pw']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        new_user=Register.objects.create(first_name=request.POST['f_n'], last_name=request.POST['l_n'], email=request.POST['email'], password=pw_hash)
        request.session['user_id'] = new_user.id 
        request.session['username'] = f"{new_user.first_name} {new_user.last_name}" 
        return redirect('/success')

def success(request):
    context={
        'success_login':Login.objects.all(),
        'success_reg':Register.objects.all()
    }
    return render (request, "to-do.html", context)

#EMPLOYEE/TALENT FUNCTIONS
def renderemployeepage (request):
    if request.method=="GET":
        return render (request, "addtalent.html")   

# def createemployee(request, employee_id):
def createemployee(request):
    if request.method=="GET":
        return render (request, "addtalent.html")
    # else: 
    #     errors=Employee.objects.employee_validator(request.POST)
    #     if len(errors) > 0:
    #         for key, value in errors.items(): 
    #             messages.error(request, value)
    #         return redirect('/createemployee')
    else:
        password = request.POST['e_pw']
        e_pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()    

        photo = request.FILES['talentphoto']
        fs=FileSystemStorage()
        emp_photo=fs.save(photo.name, photo)
        url=fs.url(emp_photo)
        
        new_employee=Employee.objects.create(first_name=request.POST['e_f_n'], last_name=request.POST['e_l_n'], company_email=request.POST['e_c_email'], job_title=request.POST['e_job'], photo=url,comp_level=request.POST['comp_level'], zipcode= request.POST['e_zip'], initial_password=e_pw_hash) #smltap = request.POST['s_tap'], lrgtap = request.POST['l_tap'], smlcomp = request.POST['s_com'], lrgcomp = request.POST['l_com'], iso = request.POST['p_iso'], highp = request.POST['hp_a'], angle = request.POST['a-tap'])

        request.session['new_employee_id'] = new_employee.id 
        request.session['employee'] = f"{new_employee.first_name} {new_employee.last_name}"
        new_employee.save()
        # return redirect(f'/employeeprofile/{employee_id}')
        return redirect(f'/employeeprofile/{new_employee.id}')
    #this is the part your worked with Drew on specifically for the photo upload function
    # else:
    #     pic = request.FILES['talentphoto']
    #     fs=FileSystemStorage()
    #     userpic=fs.save(pic.name, pic)
    #     url=fs.url(userpic)
    #     print (url)
    #     return redirect ('/addtalent')
    # I just changed the naming conventions below, but save the above in case it doesn't work. 
# def employee_successful_create(request): #i'm losing the employee ID with this step. Do I need this step?
#     context={
#         'employee': Employee.objects.all()
#     }
#     # return render (request, "talent_profile.html", context)
#     return redirect ('/employeeprofile', context)

def employeeprofile(request, employee_id):
    # if 'employee_id' not in request.session:
    #     return redirect('/createemployee')
    context = {
        'employee': Employee.objects.get(id=employee_id)
    }
    return render (request, 'talent_profile.html', context)

def viewemployees(request):
    context= {
        'user': Login.objects.all(),
        'all_employees': Employee.objects.all()
    }
    return render (request, "all_talent.html", context)

def updateemployee(request, employee_id):
    if request.method=="GET":
        context = {
            'employee': Employee.objects.get(id=employee_id)
        # 'employee': Employee.object.all()
    }
        return render (request, "talent_profile.html", context)
    context = {
        'employee': Employee.objects.get(id=employee_id)
    }
    if request.method=="POST":
        update_employee = Employee.objects.get(id=employee_id)
        update_employee.first_name = request.POST['e_f_n']
        update_employee.last_name = request.POST['e_l_n']
        update_employee.company_email= request.POST['e_c_email']
        update_employee.job_title = request.POST['e_job']
        update_employee.comp_level = request.POST['comp_level']
        update_employee.zipcode= request.POST['e_zip']
        update_employee.photo=request.POST['talentphoto']
        update_employee.save()
        

        # new_e_pw= Employee.objects.get(id=employee_id)
        # new_e_pw.initial_password=request.POST['e_pw']
        # new_e_pw.save()

        # new_smltap=Employee.objects.get(id=employee_id)
        # new_smltap.smltap= request.POST['s_tap']
        # new_smltap.save()

        # new_lrgtap=Employee.objects.get(id=employee_id)
        # new_lrgtap.lrgtap= request.POST['l_tap']
        # new_lrgtap.save()

        # new_smlcomp=Employee.objects.get(id=employee_id)
        # new_smlcomp.smlcomp= request.POST['s_com']
        # new_smlcomp.save()

        # new_lrgcomp=Employee.objects.get(id=employee_id)
        # new_lrgcomp.lrgcomp= request.POST['l_com']
        # new_lrgcomp.save()

        # new_iso=Employee.objects.get(id=employee_id)
        # new_iso.iso= request.POST['p_iso']
        # new_iso.save()

        # new_highp=Employee.objects.get(id=employee_id)
        # new_highp.highp= request.POST['hp_a']
        # new_highp.save()

        # new_angle=Employee.objects.get(id=employee_id)
        # new_angle.angle= request.POST['a_tap']
        # new_angle.save()

        return redirect(f'/employeeprofile/{employee_id}') #adding the employee.id here was Michael's suggestion. Not currently working.
    context = {
        'employee': Employee.objects.get(id=employee_id),
        # 'user': Register.objects.get(id=user_id),
    }
    return render (request, "talent_profile.html", context)

def deleteemployee(request, employee_id):
    # context = {
    #     'employee': Employee.objects.get(id=employee_id),
    # }
    Employee.objects.get(id=employee_id).delete()
    return redirect ('/viewemployees')

# def qualification(request):
#     return redirect('/addtalent') 

# def viewprofile(request, user_id):
#     context = {
#         'user': Register.objects.get(id=user_id)
#     }  
#     return render (request, "user_profile.html", context)

def updateprofile(request):
    if request.method=="GET":
        context = {
        'user': Register.objects.get(id=request.session['user_id'])
    }
        return render (request, "user_profile.html", context)
    context = {
        'user': Register.objects.get(id=request.session['user_id'])
    }
    user_id=request.session['user_id']
    if request.method=="POST":
        new_first_name = Register.objects.get(id=user_id)
        new_first_name.first = request.POST['f_n']
        new_first_name.save()

        new_last_name = Register.objects.get(id=user_id)
        new_last_name.last = request.POST['l_n']
        new_last_name.save()

        new_email = Register.objects.get(id=user_id)
        new_email.email = request.POST['email']
        new_email.save()

        new_job_title = Register.objects.get(id=user_id)
        new_job_title.job_title = request.POST['title']
        new_job_title.save()

        new_password = Register.objects.get(id=user_id)
        new_password.password = request.POST['pw']
        new_password.save()

        return redirect("/updateprofile")
    return render (request, "user_profile.html", context)

def schedulejob(request):
    context= {
        'new_job': Employee.objects.all(),
        'job_parameters': JobParameters.objects.all()
    }
    return render (request, "schedule_job.html", context)

def job_parameters_data (request):
    if request.method=="POST":
        job=JobParameters.objects.create(tap=request.POST['p_tap'], plug=request.POST['p_plug'], isolate=request.POST['p_iso'], psi=request.POST['p_psi'], size=request.POST['p_size'], angle=request.POST['p_angle'], company=request.POST['p_co'], jobstart=request.POST['p_start'], jobend=request.POST['p_end'], location=request.POST['p_location'])

        request.session['job_id'] = job.id 
        request.session['job_name'] = f"{job.company} {job.start_date}"
    
    return redirect('/schedulejob')


def logout(request):
    request.session.clear()
    return redirect('/')

def pricing(request):
    return render (request, "pricing.html")

def viewdocs(request):
    return render (request, "docs.html")

def drop_pin (request):
    request.session['address'] = request.POST['p_location']
    return redirect ('/schedulejob')