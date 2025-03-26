import pandas as pd
import matplotlib.pyplot as plt


markets_labels = [1, 2, 3]
markets_colors = ['red', 'blue', 'green']

plt.title("Прибыль магазинов")
plt.bar(['h', 't', 'q'], [2000, 50000, 3000], label=markets_labels, color=markets_colors)

# размер текста на графике
plt.legend(title='Магазины')

plt.show()