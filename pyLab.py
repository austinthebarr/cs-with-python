import matplotlib.pyplot as plt
import numpy as np 

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myQuadratic.append(i**3)
    myExponential.append(1.5 ** i)

plt.plot(np.array(mySamples), np.array(myLinear))
plt.plot(np.array(mySamples), np.array(myQuadratic))
# plt.plot(np.array(mySamples), np.array(myCubic))
# plt.show(block=True)
plt.plot(np.array(mySamples), np.array(myExponential))
plt.show(block=True)