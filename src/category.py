class Category:
    counter_category = 0
    counter_products = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        self.counter_category =+1
        self.counter_products += len(products)
