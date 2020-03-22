import pandas as pd

import src.constants as const


def read_patients():
    return pd.read_csv(const.MASTER_FILE_PATH)
