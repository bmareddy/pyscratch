# Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 

# Order Number	Book Title and Author	Quantity	Price per Item
# 34587	Learning Python, Mark Lutz	4	40.95
# 98762	Programming Python, Mark Lutz	5	56.80
# 77226	Head First Python, Paul Barry	3	32.95
# 88112	Einführung in Python3, Bernd Klein	3	24.99


# Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €. 
# Write a Python program using lambda and map.

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95], ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]

# --------- Using lambda and map ------------- #
min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), map(lambda x: (x[0],x[2] * x[3]), orders)))
print(invoice_totals)

# --------- Using List comprehension ------------- #
min_order = 100
invoice_totals = list(({k: v if v >= min_order else v+10 for k,v in ({x[0]: x[2]*x[3] for x in orders}).items()}).items())
print(invoice_totals)