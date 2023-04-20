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
    

#class >Digital_Product,household appliances,Educational

class Digital_Product(BaseItem):
    color_choise=(('black' , 'black') ,
                    ('white' , 'white') ,
                    ('silver' , 'silver') ,
                    ('blue' , 'blue') ,
                    ('red' , 'red') ,
                    ('green' , 'green') ,
                    ('yellow' , 'yellow'))
    
    color=models.CharField(max_length=120, choices=color_choise, null=True)
    volume=models.SmallIntegerField(null=True, default=0)
                    

class Household_appliances(BaseItem):
    color_choise=(('black' , 'black') ,
                    ('white' , 'white') ,
                    ('silver' , 'silver') ,
                    ('blue' , 'blue') ,
                    ('red' , 'red') ,
                    ('green' , 'green') ,
                    ('yellow' , 'yellow'))
    
    color=models.CharField(max_length=100, choices=color_choise)


class Educational(BaseItem):

    recommended_age=models.CharField(max_length=150)


class Computer(Digital_Product):
    




class Mobile(Digital_Product):




class Television(Household_appliances):
    decision=models.CharField(max_length=200)
    size=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name





    