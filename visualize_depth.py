import matplotlib.pyplot as plt
import numpy as np

# Load depth data
depth = np.load("outputs/coral_reef/frames/Depth/camera_0/Depth_0_0_0001_0.npy")

# Define a max threshold to consider "infinite"
depth_threshold = 100.0  # meters; adjust for your scene

# Mask out "infinite" or too-far values
infinite_mask = depth > depth_threshold
depth_masked = np.ma.masked_where(infinite_mask, depth)

# Colormap: use viridis for valid values, white for masked
cmap = plt.cm.viridis.with_extremes(bad="white")

# Plot
plt.figure(figsize=(8, 6))
img = plt.imshow(depth_masked, cmap=cmap)
cbar = plt.colorbar(img, label="Depth (meters)")
plt.title("Masked Infinite Distance Depth Map")
plt.axis("off")
plt.tight_layout()

plt.savefig(
    "outputs/coral_reef/frames/Depth/camera_0/depth_colored_with_axis.png", dpi=300
)

plt.show()
