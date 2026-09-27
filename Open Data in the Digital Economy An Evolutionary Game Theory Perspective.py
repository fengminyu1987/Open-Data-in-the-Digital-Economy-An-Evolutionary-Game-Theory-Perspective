import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#自由参数
alpha = 0.3
VV1 = np.arange(1, 5, 0.1)
CC2 = np.arange(3, 7, 0.1)
rs=[]
for V1 in VV1:
    rs_temp=[]
    for C2 in CC2:
        #parameters
        C1 = 6
        C3 = 5
        V2 = 1
        R1 = 2
        L1 = 5
        L2 = 7
        P = 3
        R2 = 4
        F = 1
        #x: provider, y: user, z: regulator
        def f(t,u):
            x, y, z = u
            dxdt = x*(1-x)*(2*z*F+y*R1+y*L1-C1)
            dydt = y*(1-y)*(2*z*F+x*R1+x*L2+x*alpha*(V1-V2)+alpha*V2-C2)
            dzdt = z*(1-z)*(x*y*R2+P-C3)
            dudt = [dxdt, dydt, dzdt]
            return dudt
        u0=[0.5,0.5,0.5]
        t = np.linspace(0,50,50)
        sol = odeint(f,u0,t,tfirst=True)
        res=sol.T
        rs_temp.append(round(res[1][-1],2))
    rs.append(rs_temp)
rsout=np.array(rs)
rsout=rsout[::-1]