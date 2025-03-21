import os
import csv

from shoppinglistopgaven.price_list import PriceList

class ShoppingList:
    """
    A class to represent a shopping list.

    Attributes
    ----------
    items : dict
        A dictionary to store shopping items and their quantities.

    Methods
    -------
    add_item(item, quantity):
        Adds an item and its quantity to the shopping list.
    
    remove_item(item, quantity):
        Removes a specified quantity of an item from the shopping list if it exists.
    
    get_items():
        Returns the dictionary of shopping items and their quantities.
    """
    def __init__(self):
        self.items = {}
        self.price_list = PriceList()

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            elif self.items[item] == quantity:
                del self.items[item]
            else:
                print(f"kan ikke fjerne {quantity} {item}(s), kun {self.items[item]} er tilgængelig.")
        else:
            print(f"{item} ikke fundet i shopping listen.")

    def get_items(self):
        return self.items

    def get_total(self):
        total = 0
        for item, quantity in self.items.items():
            price_data = self.price_list.get_price(item)
            if price_data:
                total += price_data['price'] * quantity
            else:
                print(f"Pris for {item} ikke fundet.")
        return total

    def print_prices(self):
        for item, quantity in self.items.items():
            price_data = self.price_list.get_price(item)
            if price_data:
                print(f"{item}: {price_data['price']} x {quantity} = {price_data['price'] * quantity}")
            else:
                print(f"Pris for {item} ikke fundet.")

# Example usage:
if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_item("Booster", 2)
    shopping_list.add_item("Pizza", 1)
    shopping_list.print_prices()
    print(f"dine varer koster i alt: {shopping_list.get_total()}")



