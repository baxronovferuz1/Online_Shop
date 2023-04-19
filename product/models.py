# target for model.py

# 1)BaseItem
#     category_choise(household appliances,Educational)

# -name 
# -brand
# -image
# -category
# -description
#-price
# -quantity
# -created_data


from django.db import models


class BaseItem(models.Model):

    category_choise=(("Digital_Product","Digital_Product"),
                     ("Household_appliances","Household_appliances"),
                     ("Educational","Educational"))
    
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=40)
    image=models.ImageField(upload_to="Pictutes", null=True, blank=True)
    category=models.CharField(max_length=100, choices=category_choise)
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    created_data=models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


    