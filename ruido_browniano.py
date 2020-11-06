import sys
sys.path.insert(1,'dsp-modulo')

import numpy as numpy
import thinkplot as plt

from thinkdsp import decorate
from thinkdsp import BrownianNoise

senal = BrownianNoise()
wave = senal.make_wave(duration=0.5, framerate=22050)
#wave.write("ruido_browniano.wav")

wave.plot()
decorate(xlabel="Tiempo", ylabel= "Amplitud")
plt.show()

espectro = wave.make_spectrum()
espectro.plot_power()
loglog = dict(xscale="log", yscale= "log")
decorate(xlabel="Frecuencia", ylabel= "Poder", **loglog)
plt.show()

pendiente = espectro.estimate_slope()
print("Pendiente: " + str(pendiente.slope))