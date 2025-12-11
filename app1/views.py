from django.shortcuts import render,redirect

from app1.models import student, teacher

from app1.forms import st_form, teach_form
# Create your views here.

def display_details(request):
    return render(request, 'display/display.html')


# student data
def st_details(request):
    st_data = student.objects.all()

    context = {
        'st_data' : st_data
    }

    return render(request, 'student/st_table.html', context)

def student_form(request):
    # form = st_form()
    if request.method == 'POST':
        form = st_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stu_d1')
    else:
        form = st_form()

    context = {
        'form' : form
    }

    return render(request, 'student/st_form.html', context)

def stu_update(request,id):
    data = student.objects.get(id=id)

    if request.method == 'POST':
        form = st_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('stu_d1')
    else:
        form = st_form(instance=data)

    context = {
        'form' : form
    }

    return render(request, 'student/st_form.html', context)

def st_del(request,id):
    data = student.objects.get(id=id)
    data.delete()
    return redirect('stu_d1')

# teacher data

def teach_details(request):
    data = teacher.objects.all()

    context = {
        'data' : data
    }

    return render(request, 'teacher/teach_table.html', context)

def tea_form(request):
    # form = teach_form()
    if request.method == 'POST':
        form = teach_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teach_de')
    else:
        form = teach_form()

    context = {
        'form' : form
    }

    return render(request, 'teacher/teach_form.html', context)

def teach_update(request,id):
    data = teacher.objects.get(id=id)

    if request.method == 'POST':
        form = teach_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('teach_de')
    else:
        form = teach_form(instance=data)

    context = {
        'form' : form
    }

    return render(request, 'teacher/teach_form.html', context)

def teach_del(request,id):
    data = teacher.objects.get(id=id)
    data.delete()
    return redirect('teach_de')

