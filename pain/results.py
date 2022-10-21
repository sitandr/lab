import physlab.disperse as dsp

@dsp.disperse(log=False)
def χ(m, V, P, r, T):
	return 4*(m*1e-3)*(V*1e-3)/(P*(r*1e-3)**4*T**2)

print('Air:', χ(m=(4.787, 0.001),
        V=(1.14, 0.01),
        P=(100_950, 10),
        r=(5.95, 0.01),
        T=(0.363, 0.003)))

print('CO2:', χ(m=(4.787, 0.001),
        V=(1.14, 0.01),
        P=(101_400, 10),
        r=(5.95, 0.01),
        T=(0.360, 0.001)))
