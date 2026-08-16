
# Part A 

# Output:

# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']

# Explanation:

# The bug is using a mutable default argument (cart=[]). Default arguments are created only once when the function is defined, not every time it is called. Since lists are mutable, the same default list is reused across function calls, so "apple" and "banana" remain in the list when "eggs" is added later.
# The third call is different because it passes a new list (["bread"]), so it doesn't use the shared default list.






# Part B – Fix It

# The correct approach is to use None as the default value instead of an empty list.

# def add_item(item, cart=None):
#     if cart is None:
#         cart = []


#     cart.append(item)
#     return cart
# Explanation

# Using cart=None avoids sharing the same list across multiple function calls. Since None is immutable, it is safe to use as a default parameter.

# Inside the function, we check:

# if cart is None:
#     cart = []

# If no cart is provided, a new empty list is created for that function call. This ensures that each call without a cart argument starts with its own independent list.

# For example:

# print(add_item("apple"))
# print(add_item("banana"))

# Output:

# ['apple']
# ['banana']










# Part C – Test It

def create_cart(owner, discount=0):
    """
    Creates a new shopping cart.
    discount=0 is safe because integers are immutable.
    """
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    """
    Adds an item to the cart.
    """
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    """
    Tuples are immutable.
    Attempting to modify them raises TypeError.
    """
    try:
        price_tuple[1] = new_price
    except TypeError as e:
        print("Error:", e)


def calculate_total(cart):
    """
    Calculates total after discount.
    """
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)

    return total - discount_amount


# Customer 1

cart1 = create_cart("Sid", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 800, 2)


# Customer 2


cart2 = create_cart("Achu", 20)

add_to_cart(cart2, "Book", 500, 3)
add_to_cart(cart2, "Pen", 20, 5)


# Display carts


print("Cart 1")
print(cart1)

print()

print("Cart 2")
print(cart2)

print()

print("Total for Cart 1 =", calculate_total(cart1))
print("Total for Cart 2 =", calculate_total(cart2))

print()

price = ("Laptop", 50000)
update_price(price, 60000)



# Output : 

# Cart 1
# {
# 'owner': 'Sid',
# 'items': [
#     {'name': 'Laptop', 'price': 50000, 'qty': 1},
#     {'name': 'Mouse', 'price': 800, 'qty': 2}
# ],
# 'discount': 10
# }

# Cart 2
# {
# 'owner': 'Achu',
# 'items': [
#     {'name': 'Book', 'price': 500, 'qty': 3},
#     {'name': 'Pen', 'price': 20, 'qty': 5}
# ],
# 'discount': 20
# }

# Total for Cart 1 = 46440.0
# Total for Cart 2 = 1280.0

# Error: 'tuple' object does not support item assignment









# 1. Why is discount=0 safe but cart=[] dangerous?
# --->   0 is an integer, which is immutable. It cannot be modified, so sharing it as a default value is safe.
# --->   [] is a list, which is mutable. Python creates the default list only once and reuses it for every call without a cart argument, causing unexpected shared state.


# 2. What is the difference between rebinding and mutating?
# Mutating changes the contents of the existing object.
# lst = [1, 2]
# lst.append(3)
# lst becomes [1, 2, 3]
# Rebinding makes a variable refer to a new object.
# lst = [1, 2]
# lst = [10, 20]
# lst now points to a different list


# 3. Which of these are mutable?
# --> Mutable : list , dict , set
# --> Immutable : int , float , str , tuple , bool

# 4. When you pass a list into a function and modify it, do the changes reflect outside?
# ---> Yes. Python passes a reference to the same list object. If the function mutates the list (using methods like append(), extend(), remove(), etc.), the caller sees those changes because both the caller and the function refer to the same object. If the function rebinds the parameter to a new list (lst = []), the caller's list is unaffected.