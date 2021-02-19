import os 
import geopandas as gpd

root_path = os.getcwd()
data_path = os.path.join(root_path, 'data')
os.chdir(data_path)

bldg_gdf = gpd.read_file('Z_KAIS_TL_SPBD_BULD_11000.shp', encoding='cp949') #EPSG:5181

sig_cd_ls = list(bldg_gdf['SIG_CD'].unique())
my_bldg_gdf = bldg_gdf.loc[bldg_gdf['SIG_CD']=='11620']

print(my_bldg_gdf.crs) # none
my_bldg_gdf.set_crs(epsg=5181, inplace=True)
print(my_bldg_gdf.crs) # 5181
new_bldg_gdf = my_bldg_gdf.to_crs(epsg=4326)
print(new_bldg_gdf.crs) # 4326

new_bldg_gdf.to_file('new_bldg_gdf.shp', driver='ESRI Shapefile')