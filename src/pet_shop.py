# WRITE YOUR FUNCTIONS HERE


from re import M
from typing import Optional


def get_pet_shop_name(shop):
    return shop["name"]


def get_total_cash(shop):
    return shop["admin"]["total_cash"]


def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, amount):
    shop["admin"]["pets_sold"] += amount


def get_stock_count(shop):
    count = len(shop["pets"])
    return count


def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets


def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(shop, name):
    pets = shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            del pets[pets.index(pet)]
            del pets[4]


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)


def get_customer_cash(customers):
    return customers["cash"] 


def remove_customer_cash(customer, cash):
    customer["cash"] -= cash 

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

#Optional

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
            return True
    else:
            return False 

