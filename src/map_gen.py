import matplotlib.pyplot as plt
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

lakes = gpd.read_file("./NHD/Shape/NHDWaterbody.shp")
rivers = gpd.read_file("./NHD/Shape/NHDFlowline.shp")
areas = gpd.read_file("./NHD/Shape/NHDArea.shp")

lakes_list = [
    "Lake Superior",
    "Fish Lake Reservoir",
    "Boulder Lake Reservoir",
    "Island Lake Reservoir",
    "Alden Lake",
    "Little Alden Lake",
    "Spring Lake",
    "Barrs Lake",
    "Briar Lake",
    "Lieuna Lake",
    "Thompson Lake",
    "Schultz Lake",
    "Jacobs Lake",
    "Horseshoe Lake",
    "Sunshine Lake",
    "Grand Lake",
    "Little Grand Lake",
    "Baby Grand Lake",
    "Long Lake",
    "Caribou Lake",
    "Pike Lake",
    "Eagle Lake",
    "Chub Lake",
    "Wild Rice Lake Reservoir",
    "Thomson Reservoir",
    "Venoah Lake"
]

rivers_list = [
    "Saint Louis River",
    "Cloquet River",
    "Nemadji River",
    "Pokegama River",
    "Amnicon River",
    #"Middle River",
    #"Poplar River",
    "Knife River",
    #"Gooseberry River",
    #"Split Rock River",
    #"Beaver River",
    #"Baptism River",
    #"Cross River",
    #"Temperance River",
    "Lester River",
    "Amity Creek",
    "Keene Creek",
    "Chester Creek",
    "Miller Creek",
    "Sargent Creek",
    "Midway River",
    "Gill Creek"
]

areas_list = [
    150,
    4366
]

lake_shapes = [lakes[lakes['gnis_name'] == name] for name in lakes_list]
river_shapes = [rivers[rivers['gnis_name'] == name] for name in rivers_list]
area_shapes = [areas[areas['ObjectID'] == id] for id in areas_list]

for name in lakes_list:
    if lakes[lakes['gnis_name'] == name].empty:
        print(f"Lake not found: {name}")

# 
fig = plt.figure(figsize=(8.0, 4.8), dpi=100)
ax = plt.axes(projection=ccrs.PlateCarree())

# 
ax.set_extent([-92.54, -91.5, 46.6, 47.1], crs=ccrs.PlateCarree())

#
ax.add_feature(cfeature.LAND, facecolor='white')

for lake in lake_shapes:
    if not lake.empty:
        lake.plot(ax=ax, transform=ccrs.PlateCarree(), color='darkgray', linewidth=0.5)
for river in river_shapes:
    river.plot(ax=ax, transform=ccrs.PlateCarree(), color='darkgray', linewidth=0.5)
for area in area_shapes:
    area.plot(ax=ax, transform=ccrs.PlateCarree(), color='darkgray', linewidth=0.5)

# Save exact-size image
plt.savefig("map.png", bbox_inches='tight', pad_inches=0, dpi=100)
plt.close()
