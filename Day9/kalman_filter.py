import numpy as np 

class KF:
    def __init__(self, initial_x, initial_v, accel_variance):

        # State vector [position, velocity]
        self.x = np.array((initial_x,initial_v))

        # State covariance matrix (uncertainty in the state)
        self.P = np.eye(2) # forma identity matrix of 2x2;

        self.accel_variance = accel_variance

    @property
    def pos(self):
        return self.x[0]
    
    @property
    def vel(self):
        return self.x[1]
    
    def predict(self, dt:float):
        '''Predict the next state (position and velocity)
        using the current state and the acceleration variance
         X = F*x
         P = F*p*Ft + G*Gt*a
        '''
        F = np.array([[1,dt], [0,1]])
        G = np.array([[0.5 * dt ** 2], [dt]])
        
        new_X = F.dot(self.x)
        new_P = F.dot(self.P).dot(F.T) + G.dot(G.T) * self.accel_variance

        self.P = new_P
        self.x = new_X
    
    def update(self, meas_value:float, meas_variance: float):
        # y = z - H*x
        # S = H*P*Ht + R (Ht is transpose of H)
        # K = P*Ht*S^-1
        # x = x + K*y
        # P = (I - K*H)*P

        H = np.array([1,0]).reshape((1,2))
        z = np.array([meas_value])
        R = np.array([meas_variance])

        y = z - H.dot(self.x)
        S = H.dot(self.P).dot(H.T) + R
        K = self.P.dot(H.T).dot(np.linalg.inv(S))

        new_x = self.x + K.dot(y)
        new_P = (np.eye(2) - K.dot(H)).dot(self.P)

        self.x = new_x
        self.P = new_P
