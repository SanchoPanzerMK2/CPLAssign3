'''
Created on Mar 23, 2018

@author: armando
'''
import Inventory_item

class main:
    items = []
    num=int(input("how many items do you want?"))
    for x in range(0,num):
        description=input("Enter description")
        cost=input("enter cost")
        remaining=input("Enter Remaining")
        items.append(Inventory_item.Inventory_item(description,cost,remaining))
    #item1= Inventory_item.Inventory_item("Makes toast", 50,1000)
    #item2=Inventory_item.Inventory_item("Vaccuums", 100, 44)
    #item3=Inventory_item.Inventory_item("Filters tap water", 30, 464)
    
    for i in range(0,x):
        print(items[i].printItem())
        