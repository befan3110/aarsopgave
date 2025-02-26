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
                print(f"Cannot remove {quantity} {item}(s), only {self.items[item]} available.")
        else:
            print(f"{item} not found in the shopping list.")

    def get_items(self):
        return self.items

# Example usage:
if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_item("Apples", 3)
    shopping_list.add_item("Bananas", 2)
    print(shopping_list.get_items())  # Output: {'Apples': 3, 'Bananas': 2}
    shopping_list.remove_item("Apples", 1)
    print(shopping_list.get_items())  # Output: {'Apples': 2, 'Bananas': 2}
    shopping_list.remove_item("Bananas", 2)
    print(shopping_list.get_items())  # Output: {'Apples': 2}
