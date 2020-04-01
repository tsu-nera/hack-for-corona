import requests
import pandas as pd

import src.constants as const


def read_patients():
    return pd.read_csv(const.PATIENTS_FILE_PATH)


def cut_ku(x):
    if "区" in x:
        return x.split("市")[0] + "市"
    else:
        return x


def download_csv(url, file_path):
    r = requests.get(url)

    r.encoding = r.apparent_encoding

    with open(file_path, 'w') as f:
        f.write(r.text)
