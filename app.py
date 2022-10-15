# from tkinter import Variable
# from flask import Flask
# app = Flask(__name__)

# @app.get('/hello')
# def get_hello():
#     return 'Hello World'

# app.run(debug=True)

# import math
# math.prod(Variable)

import random
print(random.random())

def add_two(num_one, num_two):
    return num_one + num_two
    

aa=add_two(3, 9)
print(aa)

x = 15
if (x > 10):
    print("that is a large number!")
elif(x == 10):
    print("that is the number 10!")
else:
    print('that is a small number!')

y = [2]
y.extend([1, 4, 5, 6, 8])
print(y)

fruits = []
fruits.extend(['apple', 'pineapple', 'orange'])
print(fruits)