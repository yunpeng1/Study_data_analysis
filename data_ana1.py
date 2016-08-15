from gosl_fig import *
from scipy.interpolate import interp1d

Exp = Read('Experimental.txt')
Sim = Read('Simulation.txt')

# plot(Exp['ed'],Exp['q/p'],'bo-')
# plot(Sim['ed'],Sim['q/p'],'go-')

E_x = Exp['ed']
E_y = Exp['q/p']
S_x = Sim['ed']
S_y = Sim['q/p']

Ef = interp1d(E_x,E_y)
Sf = interp1d(S_x,S_y)

plot(E_x,Ef(E_x),'bo-',label='Experimental data')
plot(E_x,Sf(E_x),'go-',label='linear interpolation data')
plot(S_x,Sf(S_x),'ro-',label='Simulation data')

axis([min(E_x),max(E_x),min(E_y),max(E_y)+0.1])
legend(loc='best')

show()