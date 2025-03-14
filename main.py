from shopping_list import ShoppingList


shopping_list = ShoppingList()
shopping_list.add_item("Booster", 2)
shopping_list.add_item("Pizza", 1)
shopping_list.print_prices()
print(f"Total: {shopping_list.get_total()}")
