import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

beta = 1 # Rate der Infektionen pro Zeiteinheit
sigma = 1 # Latenzzeit
gamma = 0.1 # infektiösen Zeit, Zeit bis Symtome auftreten

def seir_f(t, y, beta, sigma, gamma):
    s, e, i, r = y
    return np.array([-beta * i * s,
                     -sigma * e + beta * i * s,
                     -gamma * i + sigma * e,
                     gamma * i])

sol = solve_ivp(seir_f, [0, 60], [0.99, 0, 0.01, 0],rtol=1e-6, args=(beta, sigma, gamma))
#(function, zeitspanne, S,e,i,r, rtol(kantenglättung im graph), functions parameter)
fig = plt.figure() # Kurven
ax = fig.gca() # Graphachsen
curves = ax.plot(sol.t, sol.y.T) # sol.y.T, y element als Tuple
ax.legend(curves, ['S', 'E', 'I', 'R'])
plt.show()