# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read an image
img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define mean and standard deviation of Gaussian noise
mean = 0
std = 20

# Generate Gaussian noise
noise = np.random.normal(mean, std, img.shape)

# Add noise to the image
noisy_img = img + noise

# Clip the values to be between 0 and 255
noisy_img = np.clip(noisy_img, 0, 255)

# Convert the noisy image to uint8
noisy_img = noisy_img.astype(np.uint8)

# Plot the original and noisy images
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(noisy_img)
plt.title('Noisy image')
plt.axis('off')
plt.show()
