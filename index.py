class Product:

    def __init__(self,name,price,deal_price,rating):
        self.name =name 
        self.price = price
        self.deal_price = deal_price
        self.rating =rating 
        self.you_saved = price - deal_price 
    

    def display_product_details(self):

        print("Product : {}".format(self.name))
        print("Price : {}".format(self.price)) 
        print("deal_price : {}".format(self.deal_price))
        print("rating : {}".format(self.rating))
        print("you_saved : {}".format(self.you_saved)) 

    def get_deal_price(self):
        return self.deal_price

class Electronic_Items(Product): 

    def __init__(self, name, price, deal_price, rating,warranty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_months = warranty_in_months 

    def get_warranty(self):
        return self.warranty_in_months

    def display_product_details(self):
        super().display_product_details() 
        print("warranty in months {}".format(self.warranty_in_months))
   
class GroceryItem(Product):

    def __init__(self, name, price, deal_price, rating,experiy_date):
        super().__init__(name, price, deal_price, rating)
        self.experiy_date = experiy_date 

    def get_experiy(self):
        return self.experiy_date 
    
    def display_product_details(self):
        super().display_product_details()
        print("experiy in date {}".format(self.experiy_date))
      
class Order:
    def __init__(self,delivery_address, delivery_speep):
        self.item_in_card = []

        self.delivey_address =  delivery_address 
        self.delivery_speep =delivery_speep 

    def add_items(self,product,quantity):
        self.item_in_card.append((product,quantity)) 
    
    def display_order_details(self):
        for product,quantity in self.item_in_card:
            product.display_product_details() 
            print("Quantity : {}".format(quantity))

    def total_price(self):
        total_amount = 0 

        for product,quantity in self.item_in_card:

            price = product.get_deal_price() * quantity 
            total_amount += price
        print("total Bill : {}".format(total_amount)) 


tv = Electronic_Items("TV",7000,5000,4.0,24)
# tv.display_product_details()
# tv.set_warranty(14)
# milk = GroceryItem("Milk",26,21,3.5,"2/3/2023") 
# milk.display_product_details()
# milk.set_experiy("2/5/2024")

order = Order("chengam","one day delivery")
order.add_items(tv,1)
# print()
# order.add_items(milk,3)
# print()

order.display_order_details() 

# print()
order.total_price()