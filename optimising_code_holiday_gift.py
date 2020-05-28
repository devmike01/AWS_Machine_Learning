import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')

gift_costs = np.array(gift_costs).astype(int)


#Needs refactoring
start = time.time()
total_price =0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08


#Refractor
total_price = ([cost*1.08 for cost in gift_costs[cost < 25]]).sum() * 1.08

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))

start = time.time()

total_price = #Todo

print(total_price)
print('Duration: {} secons'.format(time.time() -start))
