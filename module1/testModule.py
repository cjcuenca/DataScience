"""
    Script que llama a un modulo de otra carpeta:
    basico --> Ejercicios_18_Repaso,py
"""

import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )

from basico import Ejercicios_18_Repaso

Ejercicios_18_Repaso.suma([2, 3])