import numpy as np
from matplotlib import pyplot as plt
import os


# Complete the following to make the plot
if __name__ == "__main__":
    DATA_FILE = 'sdss_galaxy_colors.npy'
    DATA_DIRECTORY = 'week05'

    INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)
    data = np.load(INPUT_FILE)

    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')

    # Define our colour indexes u-g and r-i
    ug = data['u'] - data['g']
    ri = data['r'] - data['i']

    # Make a redshift array
    redshift = data['redshift']

    # Create the plot with plt.scatter and plt.colorbar
    plot = plt.scatter(ug, ri, s=1, lw=0, c=redshift, cmap=cmap)

    cb = plt.colorbar(plot)
    cb.set_label('Redshift')

    # Define your axis labels and plot title
    plt.xlabel('Colour index u-g')
    plt.ylabel('Colour index r-i')
    plt.title('Redshift (colour) u-g versus r-i')

    # Set any axis limits
    plt.xlim(-0.5, 2.5)
    plt.ylim(-0.5, 1)

    plt.show()