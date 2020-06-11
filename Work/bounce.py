# bounce.py
# 
# Exercise 1.5

height = 100
rebound = 3/5
bounces = 0

while (bounces < 10):
    height = round(height*rebound, 4)
    bounces += 1
    print(bounces, height)
