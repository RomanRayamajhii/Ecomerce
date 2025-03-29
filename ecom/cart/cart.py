from store.models import Product,Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request
        # Ensure the session has a cart
        cart = self.session.get('session_key', {})

        if 'session_key' not in self.session:
            cart=self.session['session_key']={}  # Initialize empty cart
        
        
        self.cart=cart
    def db_add(self,product,quantity):
        # Check if the product is already in the cart
        product_id = str(product)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
            self.save()
        self.session.modified = True  # Mark session as modified
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user_id=self.request.user)
            carty =str(self.cart)
            carty=carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))
        
    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price:':str(product.price)}  # Store updated cart in session
            self.cart[product_id]=int(quantity)
        self.session.modified = True  # Mark session as modified
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user_id=self.request.user)
            carty =str(self.cart)
            carty=carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))

    def __len__(self):
        return len(self.cart)
    def get_pords(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        return products
    def get_quants(self):
        quantities=self.cart
        return quantities
    
    
    def update(self, product, quantity):
        product_id = str(product.id)
        
        self.cart[product_id] = quantity
        self.save()
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user_id=self.request.user)
            carty =str(self.cart)
            carty=carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))

    def save(self):
        self.session.modified = True
    def delete(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session['session_key'] = self.cart
        self.session.modified=True
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user_id=self.request.user)
            carty =str(self.cart)
            carty=carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))
    
    
    def total(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        quantities=self.cart
        total=0
        for key,value in quantities.items():
            key =int(key)
            for product in products:
                if product.id==key:
                    if product.is_sale:
                        total+=(product.sale_price*value)
                    else:
                        total+=(product.price*value)
                        
                    
        return total
            
            
                
        
    
    