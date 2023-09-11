from django.urls import path
from .views import trigger_bash,list_view,main_page,new_buildings,new_sub_comms,buildings_add_raw,communities_add,view_comms,areas_add,sub_comms_add,projects_add_buildings,projects_add_comms

urlpatterns = [
    path('', trigger_bash, name='run_sh'),
    path('areas/', list_view, name='areas'),
    path('areas/add/', areas_add, name='areas_add'),
    path('communities/', view_comms, name='view_comms'),
    path('communities/add/', communities_add, name='communities_add'),

    path('new_buildings/', new_buildings, name='new_buildings'),
    path('add/raw/building/<str:name>/<int:areaid>', buildings_add_raw, name='building_add'),


    path('new_sub_comms/', new_sub_comms, name='new_sub_comms'),
    path('add/raw/subcomms/<str:name>/<int:areaid>/<str:areaname>', sub_comms_add, name='comm_add'),

    path('add/project/buildings/<str:name>', projects_add_buildings, name='projects_add_bldgs'),
    path('add/project/subcomms/<str:name>', projects_add_comms, name='projects_add_comms'),
]