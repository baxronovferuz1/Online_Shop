# target for model.py

# 1)BaseItem
#     category_choise(household appliances,Educational)

# -name 
# -brand
# -image
# -category
# -description
# -quantity
# -created_data


from django.db import models


class BaseItem(models.Model):

    category_choise=(("Digital_Product","Digital_Product"),
                     ("Household_appliances","Household_appliances"),
                     ("Educational","Educational"))


    