import numpy as np 
import matplotlib.pyplot as plt
from kalman_filter import KF

plt.ion()
plt.figure()

# initializes the Kalman Filter
kf = KF(initial_x=0.0, initial_v=1.0, accel_variance=0.1)
# time step for predictions.
DT = 0.1
# specifies the number of steps for which predictions will be made
NUM_STEPS = 1000
# measurements every steps
MEAS_EVERY_STEPS = 20

# collects the state vectors [position, velocity] from each prediction step.
mus = []
# collects the covariance matrices from each prediction step.
covs = []

real_xs = []
real_vs = []

# assumption
real_x = 0
real_v = 0.9
meas_variance = 0.1**2 # will simulate noise

for step in range(NUM_STEPS):
    covs.append(kf.P)
    mus.append(kf.x)

    real_x = real_x + DT * real_v

    kf.predict(dt=DT)
    if (step != 0) and (step%MEAS_EVERY_STEPS==0) :
        kf.update(meas_value = real_x + np.random.randn() * np.sqrt(meas_variance)
                  , meas_variance=meas_variance)
        
    real_xs.append(real_x)
    real_vs.append(real_v)
plt.subplot(2,1, 1)
plt.title('position')
plt.plot([mu[0] for mu in mus], 'r')
# plot original
plt.plot(real_xs, 'b')
# plot the lower and upper bound of the position with 2 
# standard deviations (using the covariance matrix) as a dashed red line.
plt.plot([mu[0] - 2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs) ], 'r--')
plt.plot([mu[0] + 2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs) ], 'r--')


# same for velocity
plt.subplot(2,1, 2)
plt.title('velocity')
plt.plot([mu[1] for mu in mus], 'r')
plt.plot(real_vs, 'b')
plt.plot([mu[1] - 2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs) ], 'r--')
plt.plot([mu[1] + 2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs) ], 'r--')

plt.show()
plt.ginput(10)