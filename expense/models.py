from django.db import models

# Create your models here.
class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class Expense(Basemodel):
    name = models.CharField(max_length=55)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f'{self.name}-{self.category}'