import os
from osgeo import gdal, osr, ogr
import subprocess

input_folders = [r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\he\flugzeug\2022\he_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\he\flugzeug\2023\he_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2021\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2022\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2023\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2024\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\sh\flugzeug\2021\sh_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\sh\flugzeug\2022\sh_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\st\flugzeug\2022\st_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\st\flugzeug\2023\st_lverm\tdop\daten']
out_path = r"\\lb-srv\LB-Projekte\fernerkundung\luftbild\nwfva\flugzeug\2024\lverm\tdop\daten"
vrt_name = 'nwfva_flugzeug_2021_2023_nwfva_lverm_tdop_cog'
vrt =  os.path.join(out_path, vrt_name)


import pathlib

def get_file_paths(path_data, formats):
    path_data = pathlib.Path(path_data)
    input_windows_path = []
    # Collect file paths matching the formats
    for file_format in formats:
        input_windows_path.extend(path_data.rglob(file_format))
    # Convert paths to strings and filter out those in cog_folder
    input_data = [str(x) for x in input_windows_path]


all_files = get_file_paths(input_folders,['*.tif'])

# Print the result
for file in all_files:
    print(file)

input_list_txt = os.path.join(out_path, 'input_list.txt')

with open(input_list_txt, 'w') as file:
    file.write(all_files)
    file.close()

buildvrtString = 'gdalbuildvrt -overwrite -allow_projection_difference -input_file_list '+ input_list_txt + ' ' + vrt
subprocess.run(buildvrtString)