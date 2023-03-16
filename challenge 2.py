import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("1.supermarket.csv")
q = data.groupby("item_name").quantity.sum()

plt.bar(q.index, q, color=['orange', 'purple', 'yellow', 'red', 'green', 'blue', 'cyan'])
plt.xlabel('Items')
plt.ylabel('Amount sold')
plt.title("Most ordered items")
plt.xticks(rotation=20) ##rotate x axis labels##
plt.show()