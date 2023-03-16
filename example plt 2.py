import numpy as np
import matplotlib.pyplot as plt

####define array####
products = np.array([["Apple", "Orange"], ["Eggs", "Bacon"], ["Fish", "Bread"], ["Candy", "Chocolate"],
                     ["Beef", "Chicken"]])

###randomly choose 5 products one of each row###
random = np.random.randint(2, size=5)

##list of random products##
choices = []

counter = 0
for product in products:
    choices.append(product[random[counter]])
    counter += 1
print(choices)

###randomized array with percentages###
percentages=[]
for i in range(4):
    percentages.append(np.random.randint(25))
percentages.append(100-np.sum(percentages))  ###add up to 100###
print(percentages)

plt.pie(percentages, labels=choices)
plt.legend(loc="lower right", ncol=1)
plt.show()