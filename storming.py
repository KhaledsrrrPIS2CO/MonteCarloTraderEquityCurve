import random
sudden_convex_interval = random.randint(20, 40)


for i in range(100):
    test = random.randint(20, 40)
    intervalcounter = 0
    print("the test of randomint btw 20 40 is::", test)

    # Introduce a random convex payoff with a random frequency
    if i % sudden_convex_interval == 0:
        intervalcounter+= 1
print("intervalcounter:", intervalcounter)


