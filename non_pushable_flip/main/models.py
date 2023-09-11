
from django.db import models


class Areas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'areas'
        ordering = ["name"]

    def __str__(self):
        return self.name

class Communities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communities'
        ordering = ["name"]

    def __str__(self):
        return self.name
class NonPushableData(models.Model):
    transaction_id = models.CharField(primary_key=True, max_length=255)
    procedure_id = models.CharField(max_length=255, blank=True, null=True)
    trans_group_id = models.CharField(max_length=255, blank=True, null=True)
    trans_group_en = models.CharField(max_length=255, blank=True, null=True)
    procedure_name_en = models.CharField(max_length=255, blank=True, null=True)
    instance_date = models.CharField(max_length=255, blank=True, null=True)
    property_type_id = models.CharField(max_length=255, blank=True, null=True)
    property_type_en = models.CharField(max_length=255, blank=True, null=True)
    property_sub_type_id = models.CharField(max_length=255, blank=True, null=True)
    property_sub_type_en = models.CharField(max_length=255, blank=True, null=True)
    property_usage_en = models.BooleanField(blank=True, null=True)
    reg_type_id = models.CharField(max_length=255, blank=True, null=True)
    reg_type_en = models.CharField(max_length=255, blank=True, null=True)
    area_id = models.CharField(max_length=255, blank=True, null=True)
    area_name_en = models.CharField(max_length=255, blank=True, null=True)
    building_name_en = models.CharField(max_length=255, blank=True, null=True)
    project_number = models.CharField(max_length=255, blank=True, null=True)
    project_name_en = models.CharField(max_length=255, blank=True, null=True)
    master_project_en = models.CharField(max_length=255, blank=True, null=True)
    nearest_landmark_en = models.CharField(max_length=255, blank=True, null=True)
    nearest_metro_en = models.CharField(max_length=255, blank=True, null=True)
    nearest_mall_en = models.CharField(max_length=255, blank=True, null=True)
    rooms_en = models.CharField(max_length=255, blank=True, null=True)
    has_parking = models.CharField(max_length=255, blank=True, null=True)
    procedure_area = models.CharField(max_length=255, blank=True, null=True)
    actual_worth = models.CharField(max_length=255, blank=True, null=True)
    meter_sale_price = models.CharField(max_length=255, blank=True, null=True)
    rent_value = models.CharField(max_length=255, blank=True, null=True)
    meter_rent_price = models.CharField(max_length=255, blank=True, null=True)
    no_of_parties_role_1 = models.CharField(max_length=255, blank=True, null=True)
    no_of_parties_role_2 = models.CharField(max_length=255, blank=True, null=True)
    no_of_parties_role_3 = models.CharField(max_length=255, blank=True, null=True)
    community_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_pushable_data'


class Projects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    community = models.ForeignKey(Communities, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'
        ordering = ["name"]

    def __str__(self):
        return self.name

class RawBuildings(models.Model):
    id = models.IntegerField(primary_key=True)
    area_id = models.CharField(max_length=255, blank=True, null=True)
    building_name_en = models.CharField(max_length=255, blank=True, null=True)
    community = models.ForeignKey(Communities, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_buildings'



class RawCommunities(models.Model):
    area_id = models.CharField(max_length=255, blank=True, null=True)
    community = models.CharField(max_length=255, blank=True, null=True)
    community_0 = models.ForeignKey(Communities, models.DO_NOTHING, db_column='community_id', blank=True, null=True)  # Field renamed because of name conflict.
    project = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
    fixed_area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_communities'

