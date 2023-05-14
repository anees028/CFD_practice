import numpy as np
import matplotlib.pyplot as pl

x, dx = np.linspace(0.,1.,11, retstep=True)


print("X  = ",x)
print("First Element : ",x[0])
print("Second Element : ",x[1])
print("Last Element : ",x[-1])

x2 = np.linspace(0., 1., 41)
dx2 = x2[1] - x2[0]

# y1 = f1(x)
# y2 = f2(x)
# y3 = f3(x)

def f1(z):
    y1 = 1 - 2 * z
    return y1

def f2(z):
    y1 = (z - 0.4)**2
    return y1

def f3(z):
    y1 = np.sin(2 * np.pi * z)
    return y1

x, dx = np.linspace(0.0, 1.0, 11, retstep=True)
z, dz = np.linspace(-5., -1., 21, retstep=True)


print("dx = ", dx, "      dz = ", dz )
print("x = ", x)
print("z = ", z)


#Calling the functions
y1b = 1 - 2 * x
y1 = f1(x)

pl.plot(x, y1b, 'b-', lw=1)
pl.plot(x[x<0.5], y1[x<0.5], 'r--', lw=3, label='$f_1(x)$')
pl.plot(x, f2(x), 'g-.', label='$f_2(x)$')
pl.plot(x[x<0.5], f3(x)[x<0.5], 'k:', label='$f_3(x)$')
pl.legend()
pl.xlabel('$x$')
pl.ylabel('$y$')
pl.grid()
pl.xlim(0., 1.)
pl.ylim(-1.2, 1.2)


pl.show()

