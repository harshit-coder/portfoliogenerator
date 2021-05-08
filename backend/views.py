from django.contrib import messages
from django.contrib.messages import *
from django.shortcuts import render, redirect
from backend.forms import *
from backend.models import *
from django.core.mail import send_mail


def home(request):
    int = Intro.objects.first()
    edu = education.objects.all()
    key_spec = key_specialization.objects.all()
    cer = certification.objects.all()
    key_ach = key_achievements.objects.all()
    sk = skill.objects.all()
    tr = trait.objects.all()
    pro = projects.objects.all().order_by('-start_date')[:4]
    soc = social_url.objects.all()
    intern = internships.objects.all().order_by('-start_date1')[:4]
    job = jobs.objects.all().order_by('-start_date2')[:4]
    qu = query_form()
    c_pro = projects.objects.count()
    context = {'int': int, 'edu': edu, 'key_spec': key_spec, 'cer': cer, 'key_ach': key_ach, 'sk': sk, 'tr': tr,
               'pro': pro, 'soc': soc, 'intern': intern, 'job': job, 'qu': qu, 'c_pro': c_pro}
    return render(request, "homepage.html", context)


def proj_part(request, proj):
    project = projects.objects.get(id=proj)
    context = {'project': project}
    return render(request, 'project.html', context)


def intern_part(request, intern):
    intern = internships.objects.get(id=intern)
    context = {'intern': intern}
    return render(request, 'intern.html', context)


def job_part(request, job):
    jo = jobs.objects.get(id=job)
    context = {'jo': jo}
    return render(request, 'jobs.html', context)


def certif(request, cert):
    ce = certification.objects.get(id=cert)
    context = {'ce': ce}
    return render(request, 'certification.html', context)


def all_works(request):
    intern = internships.objects.all().order_by('-start_date1')
    job = jobs.objects.all().order_by('-start_date2')
    pro = projects.objects.all().order_by('-start_date')
    cer = certification.objects.all()
    soc = social_url.objects.all()
    context = {'intern': intern, 'job': job, 'pro': pro, 'cer': cer, 'soc': soc}
    return render(request, 'all.html', context)


def query_request(request):
    qu = query_form()
    if request.method == "POST":
        qu = query_form(request.POST)
        print(qu.errors)
        print("hello")
        if qu.is_valid():
            qn = request.POST['query_name']
            qe = request.POST['query_email']
            qc = request.POST['query_contact']
            qd = request.POST['query_desc']
            qu.save()
            print('Query send by' + qn, qd + 'contact No.' + qc, qe, 'gulfam.query33@gmail.com')
            send_mail('Query send by' + qn, qd + '  contact No.' + qc, qe, ['gulfam.query33@gmail.com'],
                      fail_silently=False)
            messages.success(request, 'Sent')
            return redirect('/')
        else:
            messages.error(request, 'Oops !  A error occurred')
            return redirect('/')
    else:
        return redirect('/')
