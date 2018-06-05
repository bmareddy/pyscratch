### https://www.python-course.eu/python3_lambda.php ###
# Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 

# Order Number	Book Title and Author	Quantity	Price per Item
# 34587	Learning Python, Mark Lutz	4	40.95
# 98762	Programming Python, Mark Lutz	5	56.80
# 77226	Head First Python, Paul Barry	3	32.95
# 88112	Einführung in Python3, Bernd Klein	3	24.99


# Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €. 
# Write a Python program using lambda and map.

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95], ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]
min_order = 100
value_increment = 10

# Recursive function
def pushPast100(n,increment = value_increment):
    if n >= 100:
        return n
    else:
        return pushPast100(n+increment)

# --------- Using lambda and map ------------- #
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + value_increment), map(lambda x: (x[0],x[2] * x[3]), orders)))
print(invoice_totals)

# --------- Using List comprehension ------------- #
invoice_totals = list(({k: v if v >= min_order else pushPast100(v) for k,v in ({x[0]: x[2]*x[3] for x in orders}).items()}).items())
print(invoice_totals)

# The same bookshop, but this time we work on a different list. The sublists of our lists look like this: 
# [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
# Write a program which returns a list of two tuples with (order number, total amount of order).

#orders = [ ["34587", ("A100",4,40.95), ("A101",2,14.99)], ["98762", ("A103",5,56.80), ("A100",3,40.95), ("A102",4,9.95)], ["77226", ("A100",1,40.95), ("A104",3,32.95)], ["88112", ("A105", 3, 24.99)]]
orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
	       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
	       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
# --------- Using lambda, map and reduce ------------- #
from functools import reduce
invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
invoice_totals = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], invoice_totals))
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + value_increment), invoice_totals))
print (invoice_totals)

# --------- Using List comprehension ------------- #
invoice_totals = list(({k: v if v >= min_order else v + value_increment for k,v in ({x[0]: sum(y[1]*y[2] for y in x[1:]) for x in orders}).items()}).items())
print (invoice_totals)