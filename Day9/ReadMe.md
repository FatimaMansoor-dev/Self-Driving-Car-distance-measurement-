# Project: Kalman Filter for Estimating Position and Velocity

## Overview
This project implements a **Kalman Filter (KF)** to estimate the position and velocity of a moving object (e.g., an autonomous car) based on noisy measurements. The Kalman Filter uses a combination of predictions to provide accurate real-time estimates of position and velocity.

## How It Works
The Kalman Filter operates in two steps:

1. **Prediction**: Based on the object's current position and velocity, the filter predicts its future state after a small time step (`dt`).
2. **Update**: When a new measurement (like a noisy position from GPS) is available, the filter updates the predicted state using this measurement to improve accuracy.

## Key Features
- **State Vector**: Holds the position and velocity of the object.
- **Prediction Step**: Uses the current state to predict the next position and velocity.
- **Update Step**: Incorporates noisy measurements (e.g., from sensors) to correct the predicted state.
- **Covariance Matrix**: Tracks the uncertainty in the state estimate and reduces over time as more measurements are integrated.

## Structure

- **State Vector (`x`)**: 
  - `x[0]`: Position (`x`)
  - `x[1]`: Velocity (`v`)

- **Covariance Matrix (`P`)**: 2x2 matrix that holds the uncertainty in position and velocity estimates.

- **Functions**:
  - `predict(dt)`: Predicts the next state (position, velocity) based on time step `dt`.
  - `update(meas_value, meas_variance)`: Updates the predicted state with a new measurement and its uncertainty.

