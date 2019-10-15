# descomentar las siguientes dos líneas si surge un error con matplotlib inline
# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')

# permite hacer plot en lineas de comando
%matplotlib inline 

# importando módulos 
import matplotlib.pyplot as plt  # módulo para hacer plot
import numpy as np  # módulo para trabajar con array

plt.xkcd()  # Estilo de plot

T = np.linspace(1, 24*10, 100) 

s1 = 100
arg1 = T/s1
R1 = np.exp(-arg1)

s2 = 50
arg2 = T/s2
R2 = np.exp(-arg2)

plt.plot(T/24,R1*100,'.',color='r' )
plt.plot(T/24,R2*100,'.',color='b' )

plt.title('Curva del olvido')
plt.xlabel('t [dias]')
plt.ylabel('R[%]')
plt.show()