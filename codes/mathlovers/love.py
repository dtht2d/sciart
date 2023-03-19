import numpy as np
from matplotlib import pyplot as plt
#Heart outline function
def f(x,y):
   return (x**2 + y**2 - 1)**3 - x**2 * y**3
#Heart outline1
x = np.linspace(-1.5, 1.5, 200)
y = np.linspace(-1.5, 1.5, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Define smaller heart shape
x2 = np.arange(-0.7, 0.7, 0.005)
y2 = np.arange(-0.7, 0.7, 0.005)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = f(X2, Y2)

fig, ax = plt.subplots(figsize=(7, 7))
plt.title('Heart \n $(x^2 +y^2-1)^3=x^2y^3$', fontsize=18, fontweight='bold')
plt.xlabel('YOU', fontsize=15, fontweight='bold')
plt.ylabel('I', fontsize=15, fontweight='bold')
# Drawing heart line with color
plt.contour(X, Y, Z, levels=[-1,0], colors='white', linewidths=4)

# Add smaller heart shape inside
#ax.fill(X.flatten(), -Z.flatten(), 'red', alpha=0.3, zorder=7)
#ax.fill(-X.flatten(), Y.flatten(), 'red', alpha=0.3, zorder=7)
ax.imshow(Z2, cmap='Reds', interpolation='None', extent=[-1.5, 1.5, -1.5, 1.5], alpha=0.3)
plt.savefig('/Users/duonghoang/Documents/GitHub/sciart/plots/heart.png', dpi=300, bbox_inches='tight')
