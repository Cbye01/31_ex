class Product:
    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Total Products created: {Product.total_products}")


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Warranty Period: {self.warranty_period} months")


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")



if __name__ == "__main__":
    product1 = Product("Book", 20)
    electronic_product1 = ElectronicProduct("Laptop", 1500, 12)
    clothing_product1 = ClothingProduct("T-Shirt", 15, "M")
    
    print("\nProduct Information:")
    product1.display_info()
    
    print("\nElectronic Product Information:")
    electronic_product1.display_info()
    
    print("\nClothing Product Information:")
    clothing_product1.display_info()
