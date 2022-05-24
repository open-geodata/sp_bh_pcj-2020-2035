import os


data_path = os.path.join('..', 'data')
os.makedirs(data_path, exist_ok=True)

input_path = os.path.join(data_path, 'input')
os.makedirs(input_path, exist_ok=True)

output_path = os.path.join(data_path, 'output')
os.makedirs(output_path, exist_ok=True)

output_path_gpkg = os.path.join(output_path, 'gpkg')
os.makedirs(output_path_gpkg, exist_ok=True)

output_path_gjson = os.path.join(output_path, 'geojson')
os.makedirs(output_path_gjson, exist_ok=True)

output_path_zips = os.path.join(output_path, 'zips')
os.makedirs(output_path_zips, exist_ok=True)

output_path_tabs = os.path.join(output_path, 'tabs')
os.makedirs(output_path_tabs, exist_ok=True)

#tab_path = os.path.join(data_path, 'tab')
#os.makedirs(tab_path, exist_ok=True)
