from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User  

# Member = settings.AUTH_USER_MODEL
# class Member(models.Model):
#     mem_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20, null=False)
#     email = models.EmailField()
#     password = models.CharField(max_length=20, null=False)
#     enabled = models.BooleanField(default=False)

#     def __unicode__(self):
#         return self.name

    

class Institution(models.Model):
    ins_id = models.IntegerField(primary_key=True)
    ins_type = models.CharField(max_length=10)
    ins_name = models.CharField(max_length=51)
    agent = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    city = models.ForeignKey(
        'City', related_name='city', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.Ins_id)

    class Meta:
        db_table = 'institution'


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=10)
    area_name = models.CharField(max_length=10)
    aqi = models.ForeignKey(
        'AQI', related_name='aqi', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.city_id)

    class Meta:
        db_table = 'city'


class Capacity(models.Model):
    cap_id = models.AutoField(primary_key=True)
    cap_name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.cap_id)

    class Meta:
        db_table = 'capacity'


class Institutions_Unit(models.Model):
    Ins_id = models.ForeignKey(
        'Institution', related_name='institution', on_delete=models.CASCADE)
    cap_id = models.ForeignKey(
        'Capacity', related_name='capacity', on_delete=models.CASCADE)
    num_bed = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Ins_id + cap_id)

    class Meta:
        db_table = 'institution_unit'
        unique_together = ("Ins_id", "cap_id")

class Aqi(models.Model):
    aqi_id = models.IntegerField(primary_key=True)
    aqi_area = models.CharField(max_length=10)
    aqi_index = models.IntegerField()
    aqi_pubdate = models.DateTimeField()
       
    def __str__(self):
        return str(self.aqi_id)

    class Meta:
        db_table = 'AQI'
        # ordering = ('aqi_id')

class Comment(models.Model):
    com_id = models.IntegerField(primary_key=True)
    com_con = models.TextField(max_length=500, blank=False)
    com_created = models.DateTimeField(auto_now_add=True)
    mem = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.com_id)

    class Meta:
        db_table = 'comment'
        # ordering = ('Com_created')


class Favorite(models.Model):
    fav_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    fav_intitu = models.ForeignKey(
        'Institutions_Unit', related_name='institution_unit', on_delete=models.CASCADE)
    mem = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fav_id)

    class Meta:
        db_table = 'favorite'
        # ordering = ('created')

