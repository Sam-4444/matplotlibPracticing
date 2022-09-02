import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
print(x)

plt.plot(x,np.sin(x),"--")
plt.show()
plt.plot(x, color="red")
plt.show()
plt.scatter(x[:10],x[:10]+2)
plt.show()
plt.plot(x[:10],x[:10]+2,color="purple",linewidth=1,linestyle="--",marker="*",markersize=4)
plt.show()
nlp=np.arange(20,40).reshape(4,5)
print(nlp)