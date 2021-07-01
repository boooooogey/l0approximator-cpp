import numpy as np

y = np.r_[np.random.rand(10), np.random.rand(16)+15, np.random.rand(6)+10]

with open("y.array","w") as file:
    for i in y:
        file.write(str(i) + "\n")
