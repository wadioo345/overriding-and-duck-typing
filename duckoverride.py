# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:35:41 2026

@author: Dell User
"""

class vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
        
    def engine(self):
        print(self.brand)
        
class car(vehicle):
    def __init__(self, brand, year , doors):
        super().__init__(brand, year)
        self.doors = doors
        
        
    def engine(self):
        print(f"{self.brand} car (Model {self.year} , {self.doors}-doors)")
        
        
Car = car("Toyota" , 2025 , 4)


Car.engine()



#duck typing

class KBZPay:
    def pay(self):
        print("Payment made using KBZPay Sucessfully:")
        
class WavePay:
    def pay(self):
        print("Payment made using WavePay Sucessfully:")
        
        
class AYAPay:
   def pay(self):
       print("Payment made using AYAPay Sucessfully:")
       
       
class CBPay:
   def pay(self):
       print("Payment made using CBPay Sucessfully:")
       
     
        
class Yomabank:
   def pay(self):
       print("Payment made using Yomabank Sucessfully:")
       
       
class UABPay:
   def pay(self):
       print("Payment made using UABPay Sucessfully:")
       
       
class CashOnDelivery:
   def pay(self):
       print("Payment made using Cash On Delivery:")
       
       
def chekout(Payment_syatem):
    Payment_syatem.pay()
    
    
k_pay = KBZPay()
w_pay = WavePay()
aya_pay = AYAPay()
cb_pay = CBPay()
yomabank = Yomabank()
uab_pay = UABPay()
Cash = CashOnDelivery()


chekout(k_pay)
chekout(w_pay)
chekout(aya_pay)
chekout(cb_pay)
chekout(yomabank)
chekout(uab_pay)
chekout(Cash)