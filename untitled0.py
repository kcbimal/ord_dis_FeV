import numpy as np
from mayavi import mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the lattice constant (length of the unit cell edge)
a = 3.304  # You can adjust this value as needed

# Generate lattice vectors for BCC
lattice_vectors = np.array([[0, 0, 0], [0.5, 0.5, 0.5]]) * a

# Create a mesh grid to represent the lattice
n = 2  # Adjust the number of unit cells in each direction as needed
cell_indices = np.arange(0, n, 1)
mesh = np.array(np.meshgrid(cell_indices, cell_indices, cell_indices)).T.reshape(-1, 3)

# Generate atom positions within the unit cell
atom_positions = lattice_vectors[0]  # Place an atom at the origin of the unit cell

# Repeat the unit cell to create the entire lattice
lattice = np.tile(mesh, (1, 1)) * a + atom_positions

# Create random colors for each atom
num_atoms = len(lattice)
colors = np.random.rand(num_atoms, 3)  # Generate random RGB colors

# Create a Mayavi figure
mlab.figure('BCC Lattice', bgcolor=(1, 1, 1), size=(800, 600))

# Plot the lattice using points
mlab.points3d(
    lattice[:, 0], lattice[:, 1], lattice[:, 2],
    scale_mode='none', scale_factor=0.2, color=(0, 0, 1), mode='sphere'
)

# Add labels to the axes
mlab.xlabel('X')
mlab.ylabel('Y')
mlab.zlabel('Z')

# Title for the plot
mlab.title('BCC Lattice using Mayavi')

# Show the Mayavi plot
mlab.show()

# Plot the BCC lattice (2D)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(lattice[:, 0], lattice[:, 1], lattice[:, 2], c='b', marker='o', s=100)

# Add labels to the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the view to be inclined by 30 degrees
ax.view_init(elev=60, azim=30)

# Title for the plot
plt.title('Body-Centered Cubic (BCC) Lattice with 1 Atom per Unit Cell')

# Add coordinate labels to the Matplotlib plot
for i, atom_coord in enumerate(lattice):
    ax.text(atom_coord[0], atom_coord[1], atom_coord[2], f'({atom_coord[0]:.2f}, {atom_coord[1]:.2f}, {atom_coord[2]:.2f})')

# Print coordinates of each atom to the console
for i, atom_coord in enumerate(lattice):
    print(f'At.#{i+1}: ({atom_coord[0]:.3f}, {atom_coord[1]:.3f}, {atom_coord[2]:.3f})')

plt.show()
