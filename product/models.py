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
    slug = models.SlugField(unique = True , null = True)
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
    screen_size = models.CharField(max_length = 100)
    graphics_card = models.BooleanField()

    def __str__(self):
        return self.name

    


class Mobile(Digital_Product):

    model_choice=(
        ("redmi","Redmi"),
        ("samsung","Samsung"),
        ("apple","Apple"),
        ("nokia","Nokia"),
        ("vivo","Vivo"))
    



    type_choice=models.CharField(max_length=50, choices=model_choice)


    def __str__(self) -> str:
        return self.name



class Television(Household_appliances):
    size=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    


class Book(Educational):
    language_choice=(
        ("russian","Russian"),
        ("english","English"))
    
    language=models.CharField(max_length=40, choices=language_choice)
    author=models.CharField(max_length=250)
    publisher=models.CharField(max_length=250) #qaysi nashriyotdan ekanligi


    def __str__(self) -> str:
        return self.name



class Stationery(Educational): #konstavardagi mahsulotlar


    product_choice=(
        ("pen","Pen"),
        ("pencil","Pencil"),
        ("notebook","Notebook"))
        
    


    