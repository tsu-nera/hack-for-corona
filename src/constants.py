import os

# data name
DATA_DIR = "data"
RAWDATA_DIR = "rawdata"

# file name
PATIENTS_FILE = "patients.csv"
CONTACTS_FILE = "contacts.csv"
QUERENT_FILE = "querent.csv"
HOSPITAL_FILE = "hospital.csv"

# data
PATIENTS_FILE_PATH = os.path.join(DATA_DIR, PATIENTS_FILE)

# rawdata
PATIENTS_RAWFILE_PATH = os.path.join(RAWDATA_DIR, PATIENTS_FILE)
CONTACTS_RAWFILE_PATH = os.path.join(RAWDATA_DIR, CONTACTS_FILE)
QUERENT_RAWFILE_PATH = os.path.join(RAWDATA_DIR, QUERENT_FILE)
HOSPITAL_RAWFILE_PATH = os.path.join(RAWDATA_DIR, HOSPITAL_FILE)
