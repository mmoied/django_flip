from django import forms
from django.db.models import Max
from .models import Areas, Communities,Projects,RawBuildings,RawCommunities
from dal import autocomplete


class projects_add_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        name = kwargs.pop('name')
        project_number = kwargs.pop('project_number')
        super(projects_add_form, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(initial=name)
        self.fields['id'] = forms.IntegerField(initial=project_number['id__max']+1,widget=forms.HiddenInput())

    class Meta:
        model = Projects
        fields = "__all__"

# creating a form
class buildings_add_forms(forms.ModelForm):
    # project_id = forms.IntegerField(initial=Projects.objects.aggregate(Max('id'))["id__max"]+1)
    community_id = forms.ModelChoiceField(
        queryset=Communities.objects.all()
    )
    def __init__(self, *args, **kwargs):
        name = kwargs.pop('name')
        areaid = kwargs.pop('areaid')
        project_number = kwargs.pop('project_number')
        super(buildings_add_forms, self).__init__(*args, **kwargs)
        self.fields['building_name_en'] = forms.CharField(initial=name)
        self.fields['area_id'] = forms.ModelChoiceField(
            queryset=Areas.objects.all(),
            initial=areaid
        )
        self.fields['project_id'] = forms.IntegerField(initial=project_number['id__max']+1)

    class Meta:
        model = RawBuildings
        fields = "__all__"

class communities_add_form(forms.ModelForm):

    class Meta:
        model = Communities
        fields = "__all__"

class areas_add_form(forms.ModelForm):
    class Meta:
        model = Areas
        fields = "__all__"

class sub_comms_raw_forms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        name = kwargs.pop('name')
        areaid = kwargs.pop('areaid')
        super(sub_comms_raw_forms, self).__init__(*args, **kwargs)
        self.fields['community'] = forms.CharField(initial=name)
        self.fields['area_id'] = forms.IntegerField(initial=areaid)
        # self.fields['fixed_area'] = forms.CharField(initial=areaname)

    class Meta:
        model = RawCommunities
        fields = "__all__"
class building_raw_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        name = kwargs.pop('name')
        areaid = kwargs.pop('areaid')
        super(building_raw_form, self).__init__(*args, **kwargs)
        auto  = RawBuildings.objects.aggregate(Max('id'))
        self.fields['building_name_en'] = forms.CharField(initial=name)
        self.fields['area_id'] = forms.IntegerField(initial=areaid)
        self.fields['id'] = forms.IntegerField(initial=auto['id__max']+1)

    class Meta:
        model = RawBuildings
        ordering = ['Projects__name']
        fields = "__all__"
        # widgets = {
        #     'c': autocomplete.ModelSelect2(url='country-autocomplete')
        # }

class projects_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        project_number = kwargs.pop('project_number')
        name = kwargs.pop('name')
        super(projects_form, self).__init__(*args, **kwargs)
        # self.fields['building_name_en'] = forms.CharField(initial=name)
        self.fields['id'] = forms.IntegerField(initial=project_number['id__max']+1)
        self.fields['name'] = forms.CharField(initial=name)

    class Meta:
        model = Projects
        # ordering = ['Communities__name']
        fields = "__all__"
