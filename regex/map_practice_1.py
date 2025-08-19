#!/usr/bin/env python3

products = ["Shampoo", "Toothpaste", "Soap"]
prices = [6.99, 3.49, 2.50]

#"Shampoo - $6.99"
#"Toothpaste - $3.49"
#"Soap - $2.50"

formatted_prices = list(map(lambda product, price: print(f"{product} - ${price}"), products, prices))