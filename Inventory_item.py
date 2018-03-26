'''
Created on Mar 23, 2018

@author: armando
'''

class Inventory_item:
    '''
    container class, can be put in list apparently...
    description
    cost
    remaining 
    '''


    def __init__(self, description, cost, remaining):
        
        self.description = description
        self.cost = cost
        self.remaining = remaining
    
    #getters and setters...
    def getDescrption(self):
        return self.description
    def getCost(self):
        return self.cost
    def getRemaining(self):
        return self.remaining
    def setDescrption(self, description):
        self.description = description
    def setCost(self, cost):
        self.cost=cost
    def setRemaining(self, remaining):
        self.remaining=remaining
        
    def printItem(self):
        print(self.getDescrption())
        print(self.getCost())
        print(self.getRemaining())