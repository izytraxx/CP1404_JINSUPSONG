"""
products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ...]
on_sale_products = ?
"""
products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]

#-------------for loop way--------------
on_sale_product = []

for each in products:
    if each[2] == True:
        on_sale_product.append(each)

print(on_sale_product)
#-----------list comprehension-----------
on_sale = [each for each in products if each[2] == True]
print(on_sale)