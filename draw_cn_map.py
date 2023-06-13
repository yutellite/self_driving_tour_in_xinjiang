import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile of China from a local file or a remote URL
# 地图数据来源，https://www.datacentermap.com/china/
china = gpd.read_file('D:/ywx_workshop/ywx_python_map/ne_10m_admin_0_countries_chn/ne_10m_admin_0_countries_chn.shp')
china = china[china['ADMIN'] == 'China']

# Set up the plot, 1980*1200
fig, ax = plt.subplots(figsize=(19.8, 12))

# Plot the China shapefile
china.plot(ax=ax, color='white', edgecolor='black')

# Set the axis limits and remove the axis ticks
ax.set_xlim([73, 135])
ax.set_ylim([18, 54])
ax.set_xticks([])
ax.set_yticks([])

# Save the plot
plt.savefig("china.png", dpi=400)

