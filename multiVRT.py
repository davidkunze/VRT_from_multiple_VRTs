import os
from osgeo import gdal, osr, ogr
import subprocess
import pathlib


input_folders = [r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\he\flugzeug\2022\he_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\he\flugzeug\2023\he_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2021\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2022\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2023\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\ni\flugzeug\2024\ni_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\sh\flugzeug\2021\sh_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\sh\flugzeug\2022\sh_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\st\flugzeug\2022\st_lverm\tdop\daten', r'\\lb-srv\LB-Projekte\fernerkundung\luftbild\st\flugzeug\2023\st_lverm\tdop\daten']
out_path = r"\\lb-srv\LB-Projekte\fernerkundung\luftbild\nwfva\flugzeug\2024\lverm\tdop\daten"
vrt_name = 'nwfva_lverm_tdop.vrt'
vrt =  os.path.join(out_path, vrt_name)



def get_file_paths(path_data, formats):
    path_data = pathlib.Path(path_data)
    # Collect file paths matching the formats
    for file_format in formats:
        input_windows_path.extend(path_data.rglob(file_format))
    # Convert paths to strings and filter out those in cog_folder

#get cogs
input_windows_path = []
for x in input_folders:
    get_file_paths(os.path.join(x+r'\kacheln'),['*.tif'])
input_data = [str(x) for x in input_windows_path]
input_data_str = '\n'.join(input_data)
input_list_txt_cog = os.path.join(out_path, 'input_list_cog.txt')
with open(input_list_txt_cog, 'w') as file:
    file.write(input_data_str)
    file.close()

#get vrt-ovr-files
input_windows_path = []
for x in input_folders:
    get_file_paths(x,['*.vrt.ovr'])
input_data = [str(x) for x in input_windows_path]
input_data_str = '\n'.join(input_data)
input_list_txt_vrt_ovr = os.path.join(out_path, 'input_list_vrt_ovr.txt')
with open(input_list_txt_vrt_ovr, 'w') as file:
    file.write(input_data_str)
    file.close()

buildvrtString = 'gdalbuildvrt -overwrite -b 1 -b 2 -b 3 -allow_projection_difference -input_file_list '+ input_list_txt_cog + ' ' + vrt
# subprocess.run(buildvrtString)

buildvrtString = 'gdalbuildvrt -overwrite -b 1 -b 2 -b 3 -allow_projection_difference -input_file_list '+ input_list_txt_vrt_ovr + ' ' + vrt + '.ovr'
subprocess.run(buildvrtString)
