from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactUs(request):
    return render(request, 'contactUs.html')

def adminLogin(request):
    error = ""
    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"

    dict = {'error':error}

    return render(request, 'adminLogin.html', dict)

def userLogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "Student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    dic = {'error': error}
    #d variable used in below
    return render(request, 'userLogin.html', dic)

def recruiterLogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = RecruiterReg.objects.get(user=user)
                if user1.type == "Recruiter" and user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "nott"
            except:
                error = "yes"
        else:
            error = "yes"
    dic2 = {'error': error}
    return render(request, 'recruiterLogin.html', dic2)

def recruiterSignup(request):

    error = ""
    if request.method == 'POST':
        fn = request.POST['firstName']
        ln = request.POST['lastName']
        cn = request.POST['contNum']
        em = request.POST['email']
        pwd = request.POST['pwd']
        gdr = request.POST['gender']
        img = request.FILES['img']
        com = request.POST['companyName']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            RecruiterReg.objects.create(user=user, mobileNo=cn, profileImage=img, gender=gdr, company=com, type="Recruiter", status="pending")
            error = "no"
        except:
            error = "yes"

    d = {'error': error}

    return render(request, 'recruiterSignup.html', d)

def userHome(request):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    return render(request, 'userHome.html')


# user logut function
def logoutUser(request):
    logout(request)
    return redirect('index')

def userSignup(request):
    error = ""
    if request.method=='POST':
        fn = request.POST['firstName']
        ln = request.POST['lastName']
        cn = request.POST['contNum']
        em = request.POST['email']
        pwd = request.POST['pwd']
        gdr = request.POST['gender']
        img = request.FILES['img']
        try:
           user = User.objects.create_user(first_name=fn, last_name=ln, username=em ,password=pwd)
           StudentUser.objects.create(user=user, mobileNo=cn, profileImage=img, gender=gdr, type="Student")
           error="no"
        except:
            error="yes"

    d={'error':error}

    return render(request, 'userSignup.html',d)

def recruiterHome(request):
    if not request.user.is_authenticated:
        return redirect('recruiterLogin')
    scount = StudentUser.objects.all().count()
    d = {'scount': scount}
    return render(request, 'recruiterHome.html',d)

def adminHome(request):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    rcount = RecruiterReg.objects.all().count()
    scount = StudentUser.objects.all().count()
    d = {'rcount':rcount, 'scount':scount}
    return render(request, 'adminHome.html',d)

def viewUsers(request):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request, 'viewUsers.html',d)

def recruiterPending(request):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    data = RecruiterReg.objects.filter(status='pending')
    d = {'data':data}
    return render(request, 'recruiterPending.html',d)


def deleteUser(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('viewUsers')

def changeStatus(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    error = ""
    recruiter = RecruiterReg.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
    d = {'recruiter':recruiter,'error':error}
    return render(request,'changeStatus.html',d)

def viewRecruiters(request):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    data = RecruiterReg.objects.all()
    d = {'data':data}
    return render(request, 'viewRecruiters.html',d)

def deleteRecruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    recruiterdel = User.objects.get(id=pid)
    recruiterdel.delete()
    return redirect('viewRecruiters')

def changePwdAdmin(request):
    if not request.user.is_authenticated:
        return redirect('adminLogin')
    error = ""

    if request.method=="POST":
        c = request.POST['currentPwd']
        n = request.POST['newPwd']

        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'changePwdAdmin.html',d)

def logoutAdmin(request):
    logout(request)
    return redirect('adminLogin')

def changePwdUser(request):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    error = ""

    if request.method=="POST":
        c = request.POST['currentPwd']
        n = request.POST['newPwd']

        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"

    d = {'error':error}
    return render(request,'changePwdUser.html',d)

def logoutUser(request):
    logout(request)
    return redirect('userLogin')


def changePwdRecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiterLogin')
    error = ""

    if request.method=="POST":
        c = request.POST['currentPwd']
        n = request.POST['newPwd']

        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'changePwdRecruiter.html',d)



def logoutRecruiter(request):
    logout(request)
    return redirect('recruiterLogin')


def jobPosting(request):
    if not request.user.is_authenticated:
        return redirect('recruiterLogin')

    error = ""
    if request.method == 'POST':
        jt = request.POST['jobTitle']
        logo = request.FILES['img']
        com = request.POST['companyName']
        s = request.POST['salary']
        loc = request.POST['location']
        dec = request.POST['description']
        url = request.POST['jobURL']
        # cd = request.POST['creationDate']

        user = request.user
        recruiter = RecruiterReg.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, title=jt, image=logo, company=com, salary=s, location=loc,
                               description=dec, joburl=url, creationdate=date.today() )

            error = "no"
        except:
            error = "yes"

    d = {'error': error}

    return render(request, 'jobPosting.html',d)

def jobList(request):
    if not request.user.is_authenticated:
        return redirect('recruiterLogin')
    user = request.user
    recruiter = RecruiterReg.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job':job}
    return render(request, 'jobList.html',d)

def editJob(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiterLogin')

    error = ""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['jobTitle']
        # logo = request.FILES['img']
        com = request.POST['companyName']
        s = request.POST['salary']
        loc = request.POST['location']
        dec = request.POST['description']
        # cd = request.POST['creationDate']

        job.title = jt
        job.company = com
        job.salary = s
        job.location = loc
        job.description = dec

        try:
            job.save()
            error = "no"
        except:
            error = "yes"

    d = {'error': error, 'job':job}

    return render(request, 'editJob.html',d)

def jobsList(request):
    data = Job.objects.all().order_by('-creationdate')
    d = {'data':data}
    return render(request, 'jobsList.html',d)

def userJobList(request):
    data = Job.objects.all().order_by('-creationdate')
    d = {'data':data}
    return render(request, 'userJobList.html',d)

# def description(request, pid):
#     if not request.user.is_authenticated:
#         return redirect('userLogin')
#
#     job = Job.objects.get(id=pid)
#     if request.method == 'POST':
#         dec = request.POST['description']
#         # cd = request.POST['creationDate']
#
#         job.description = dec
#
#         d = {'job': job}
#     return render(request, 'description.html', d)

def description(request, pid):
    if not request.user.is_authenticated:
        return redirect('userLogin')

    error = ""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['jobTitle']
        # logo = request.FILES['img']
        com = request.POST['companyName']
        s = request.POST['salary']
        loc = request.POST['location']
        dec = request.POST['description']
        # cd = request.POST['creationDate']


        job.title = jt
        job.company = com
        job.salary = s
        job.location = loc
        job.description = dec

        try:
            job.save()
            error = "no"
        except:
            error = "yes"

    d = {'error': error, 'job':job}

    return render(request, 'description.html',d)

def deleteJob(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiterLogin')
    jobdel = Job.objects.get(id=pid)
    jobdel.delete()
    return redirect('jobList')