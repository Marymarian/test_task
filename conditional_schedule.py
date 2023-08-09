import os
import matplotlib.pyplot as plt
from core import preparing_file


os.chdir("C:/Dev/test_task/sources")
filename = "working-pf-data.xlsx"
data = preparing_file(filename)


data.plot()
plt.legend(bbox_to_anchor=(1.1,1.05),shadow=True,title="Legend") # легенда за пределами, т.к. не выбирала данные
plt.title("Title")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
