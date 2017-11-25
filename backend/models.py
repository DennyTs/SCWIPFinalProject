from django.db import models

# Create your models here.
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
