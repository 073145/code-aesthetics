"""
TÍTULO: Equações do Atrator de Lorenz
DESCRIÇÃO: 
Definição matemática do sistema de equações diferenciais ordinárias 
para estudo de sensibilidade às condições iniciais (Efeito Borboleta).
"""

import numpy as np

def lorenz_system(state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    
    # Derivadas parciais
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    
    return np.array([dx, dy, dz])

# Estado Inicial Teórico
initial_state = np.array([1.0, 1.0, 1.0])
