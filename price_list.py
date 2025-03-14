import csv
import os

class PriceList:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceList, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, filename="price_list.csv"):
        self.current_dir = os.path.dirname(__file__)
        self.pricelist = {}
        self.load_pricelist(filename)

    def load_pricelist(self, filename):
        with open(os.path.join(self.current_dir, filename), mode="r") as file:
            reader = csv.reader(file)
            for rows in reader:
                self.pricelist[rows[1]] = {'description': rows[0], 'price': float(rows[2])}

    def save_pricelist(self, filename):
        with open(os.path.join(self.current_dir, filename), mode="w") as file:
            writer = csv.writer(file)
            for product, data in self.pricelist.items():
                writer.writerow([data['description'], product, data['price']])

    def get_price(self, product):
        return self.pricelist.get(product, None)

    def get_pricelist(self):
        return self.pricelist

# Example usage:
if __name__ == "__main__":
    price_list = PriceList()
    print(price_list.pricelist)