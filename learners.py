import numpy as np
import matplotlib.pyplot as plt
import math
m=1200
c=3e8

print("{:<10} {:<10} {:<15}".format("speed(v/c)", "momentum(p)", "relativemomentum(p_rel)"))

speed=[]
momentum=[]
relativistic_momentum=[]

for i in range(10):
    v=i*0.1*c
    p=m*v
    gamma = 1/(np.sqrt(1-v**2/c**2))
    p_rel=m*v*gamma
    print("{:<10.1f} {:<15.3e} {:<15.4e}".format(i * 0.1, p, p_rel))
    speed.append(i * 0.1)
    momentum.append(p)
    relativistic_momentum.append(p_rel)

plt.figure(figsize=(10, 6))
plt.plot(speed, momentum, label='Classical Momentum', marker='o')
plt.plot(speed, relativistic_momentum, label='Relativistic Momentum', marker='s')

# Add labels, title, and legend
plt.xlabel('Speed (v/c)')
plt.ylabel('Momentum (kg·m/s)')
plt.title('Classical and Relativistic Momentum vs. Speed')
plt.legend()
plt.grid(True)
plt.show()    


