import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile of the USA from the geopandas datasets
usa = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
usa = usa[usa.name == 'United States of America']

# Plot the map
fig, ax = plt.subplots(figsize=(10, 10))
usa.plot(ax=ax, color='white', edgecolor='black')
ax.set_title('Map of the USA')
plt.show()
