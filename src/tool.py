import pandas as pd

import src.constants as const


def read_patients():
    return pd.read_csv(const.MASTER_FILE_PATH)


def cut_ku(x):
    if "区" in x:
        return x.split("市")[0] + "市"
    else:
        return x
