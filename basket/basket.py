from shop_page.models import Goods

class Basket(object):
    
    def __init__(self):
        self.good_ids = []
        self.empty = True
        self.quantity = 0

    def add_item(self, good_id, quantity = 1):
        self.good_ids.append(Goods.objects.get(id=good_id))
        self.empty = False
        self.quantity +=1

basket = Basket()

def add_to_basket(good_id):
    basket.add_item(good_id)




    
    
    
        
