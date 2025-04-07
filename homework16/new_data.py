import torch
import numpy as np

x_data = np.linspace(-4, 4, 1000)
y_data = np.linspace(-4, 4, 1000)
X, Y = np.meshgrid(x_data, y_data)

# Pattern: a circular ripple effect
pattern = np.sin(np.sqrt(X**2 + Y**2))

# Dataset setup
N, D_in, H, D_out = 1000, 2, 50, 1

# Input data
x = torch.rand(N, D_in) * 8 - 4  # range: [-4, 4]
r = torch.sqrt(x[:, 0]**2 + x[:, 1]**2)
y = torch.sin(r).unsqueeze(1)

# Noise
noise = torch.randn(N, D_out) * 0.2
y += noise

# Plotting
x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()
