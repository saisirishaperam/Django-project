from django.db import models

# Create your models here.
class student(models.Model):
    st_id = models.IntegerField()
    st_name = models.CharField(max_length=50)
    st_email = models.EmailField(unique=True)
    st_age = models.IntegerField()
    st_gender = models.CharField(max_length=20)
    st_mobile = models.BigIntegerField()
    st_address = models.CharField(max_length=100)

    def __str__(self):
        return self.st_name

class teacher(models.Model):
    teach_id = models.IntegerField()
    teach_name = models.CharField(max_length=50)
    teach_email = models.EmailField(unique=True)
    teach_age = models.IntegerField()
    teach_gender = models.CharField(max_length=20)
    teach_mobile = models.BigIntegerField()
    teach_address = models.CharField(max_length=100)

    def __str__(self):
        return self.teach_name