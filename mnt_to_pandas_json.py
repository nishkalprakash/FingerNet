# read all mnt files and save it in one pandas readable json file
#%%
import os
import json
import pandas as pd
from pathlib import Path
# read all mnt files
inp_path = r"output\20231205-203643\0"

path = Path(r"anguli_2.5k_50k")
out_path = f"output/{path}.json"
ext = ".tiff"
# read all mnt files using pathlib
# mnt_files = []
js_dict_array = []
for file in Path(inp_path).glob('*.mnt'):
    js_dict = {'path':(path/f"{file.stem}{ext}").as_posix()}
    mnt_in = [list(map(float,i.split())) for i in file.read_text().strip().split('\n')[2:]]
    js_dict['mv'] = mnt_in
    js_dict_array.append(js_dict)

# save it in json file
pd.DataFrame(js_dict_array).to_json(out_path, orient='records')

#%%
# read json file
# in_json_path = r"output\FVC2002_DB1_B_minutia_net.json"
# df = pd.read_json(in_json_path, orient='records')

# %%
# df.head()
# %%
