from django.db import models

class third_party(models.Model):
    third_party_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45,blank=True)
    birth_date = models.DateField

    def __str__(self):
        return self.third_party_id

class accounts(models.Model):
    account_id = models.IntegerField(primary_key=True)
    third_party_id = models.ForeignKey(third_party, on_delete=models.CASCADE)
    account_number = models.IntegerField
    start_date = models.DateField
    end_date = models.DateField

    def __str__(self):
        return f"{self.account_id}"
