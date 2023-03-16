import matplotlib.pyplot as plt
import numpy as np

#plt.plot([0, 10], [0, 300], 'o')
#plt.show()

#plt.plot([0, 2, 5, 7, 9, 11], [0, 2, 5, 15, 12, 30])
#plt.show()

#plt.plot([0, 2, 4], [5, 10, 7], ls='dotted', marker="o")
#plt.xlabel("Month")
#plt.ylabel("Sales")
#plt.title("Sales during time")
#plt.grid()
#plt.show()


#plt.subplot(1, 2, 1)
#plt.plot([0, 2, 4, 6, 8, 10], [3, 8, 1, 10, 5, 12])

#plt.subplot(1, 2, 2)
#plt.plot([0, 10], [0, 300])
#plt.show()

####scatter plot######compare plots###
#x = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#y = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
#plt.scatter(x, y)

#x = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
#y = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
#plt.scatter(x,y)
#plt.show()

####bar chart###

#x = np.array(["A", "B", "C", "D"])
#y = np.array([4, 5, 1, 10])
#plt.bar(x, y)
#plt.show()

####pie chart###

mylabels = np.array(["Potatoes", "Bacon", "Tomatoes", "Sausages"])
x = np.array([25, 35, 15, 25])
plt.pie(x, labels=mylabels)
plt.legend()  ###adds a list of explanation
plt.show()