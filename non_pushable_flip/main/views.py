from django.shortcuts import render
from django.db.models import Max
from .forms import buildings_add_forms,communities_add_form,areas_add_form,projects_add_form,building_raw_form,projects_form,sub_comms_raw_forms
# Create your views here.

from .models import Areas,NonPushableData,Communities,Projects
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import subprocess
from django.shortcuts import redirect
@login_required
def trigger_bash(request):
    if request.POST:
        # give the absolute path to your `text4midiAllMilisecs.py`
        # and for `tiger.mid`
        # subprocess.call(['python', '/path/to/text4midiALLMilisecs.py', '/path/to/tiger.mid'])

        subprocess.call('C:/Users/Moied/Desktop/script.bat')
        return redirect('areas')

    return render(request, 'main_page.html', {})

@login_required
def main_page(request):
    context = {}
    return render(request, "main_page.html", context)

@login_required
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    context["dataset"] = Areas.objects.all()
    context['max_area'] =  Areas.objects.aggregate(Max('id'))
    return render(request, "areas.html", context)
@login_required
def areas_add(request):
    context ={}
    form =areas_add_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "areas_add.html", context)



@login_required
def view_comms(request):
    context = {}
    context["dataset"] = Communities.objects.all()
    return render(request, "all_comms.html", context)
@login_required
def communities_add(request):
    context ={}
    form =communities_add_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "communities_add.html", context)


@login_required
def new_buildings(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    context["dataset"] = NonPushableData.objects.filter(property_type_en='Unit').distinct('building_name_en')
    context['max_area'] =  Areas.objects.aggregate(Max('id'))
    return render(request, "new_buildings.html", context)


@login_required
def buildings_add_raw(request,name,areaid):
    context ={}
    # project_number = Projects.objects.aggregate(Max('id'))
    form_projects = building_raw_form(request.POST or None, request.FILES or None, name = name, areaid= areaid)
    context['form_projects'] = form_projects
    if form_projects.is_valid():
        form_projects.save()
        return redirect('new_buildings')
    return render(request, "building_add.html", context)


@login_required
def projects_add_buildings(request,name):
    context ={}
    project_number = Projects.objects.aggregate(Max('id'))
    form_projects = projects_form(request.POST or None, request.FILES or None, name = name, project_number= project_number)
    context['form_projects'] = form_projects
    if form_projects.is_valid():
        form_projects.save()
        return redirect('new_buildings')
    return render(request, "building_add.html", context)


@login_required
def projects_add_comms(request,name):
    context ={}
    project_number = Projects.objects.aggregate(Max('id'))
    form_projects = projects_form(request.POST or None, request.FILES or None, name = name, project_number= project_number)
    context['form_projects'] = form_projects
    if form_projects.is_valid():
        form_projects.save()
        return redirect('new_sub_comms')
    return render(request, "building_add.html", context)

@login_required
def new_sub_comms(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    context["dataset"] = NonPushableData.objects.exclude(property_type_en ='Unit').distinct('building_name_en')
    return render(request, "new_projects.html", context)

@login_required
def sub_comms_add(request,name,areaid,areaname):
    context ={}
    # project_number = Projects.objects.aggregate(Max('id'))
    form_projects = sub_comms_raw_forms(request.POST or None, request.FILES or None, name = name, areaid= areaid,initial={'fixed_area': areaid})
    context['form_projects'] = form_projects
    if form_projects.is_valid():
        form_projects.save()
        return redirect('new_sub_comms')
    return render(request, "building_add.html", context)



@login_required
def non_pushable(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    context["dataset"] = NonPushableData.objects.distinct('building_name_en')
    context['max_area'] =  Areas.objects.aggregate(Max('id'))
    return render(request, "non_pushable.html", context)



