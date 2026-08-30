import random
import math
import matplotlib.pyplot as plt

# Number of stars
stars = 1000

x = []
y = []

# Generate galaxy
for i in range(stars):
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(0, 10)

    # Spiral effect
    spiral = angle + distance * 1.5

    # Add some randomness
    px = distance * math.cos(spiral) + random.gauss(0, 0.4)
    py = distance * math.sin(spiral) + random.gauss(0, 0.4)

    x.append(px)
    y.append(py)

# Create galaxy
plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=1, alpha=0.8)

# Add bright galaxy center
plt.scatter(0, 0, s=300, alpha=0.5)

# Add random planets
for i in range(8):
    px = random.uniform(-8, 8)
    py = random.uniform(-8, 8)
    size = random.randint(10, 40)

    plt.scatter(px, py, s=size)

plt.title("🌌 My Random Galaxy")
plt.axis("off")
plt.show()