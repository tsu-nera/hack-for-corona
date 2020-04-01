import os
from invoke import task, run

import requests

RAWDATA_DIR = "rawdata"


@task
def evaluate_notebook(c):
    command_base = "jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute --inplace --ExecutePreprocessor.kernel_name=python"
    file_path = os.path.join("notebooks", "kanagawa-corona.ipynb")
    command = " ".join([command_base, file_path])

    run(command)


def download(url, file_path):
    r = requests.get(url)

    r.encoding = r.apparent_encoding

    with open(file_path, 'w') as f:
        f.write(r.text)


@task
def get_rawdata(c):
    get_patients(c)
    get_contacts(c)
    get_querent(c)
    get_hospital(c)


@task
def get_patients(c):
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/patient.csv"
    file_path = os.path.join(RAWDATA_DIR, "patients.csv")
    download(url, file_path)


@task
def get_contacts(c):
    '''
    専用ダイヤル相談件数
    http://www.pref.kanagawa.jp/docs/t3u/dst/s0352970.html
    '''
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/contacts.csv"
    file_path = os.path.join(RAWDATA_DIR, "contacts.csv")
    download(url, file_path)


@task
def get_querent(c):
    '''
    帰国者・接触者電話相談センター相談件数
    https://www.pref.kanagawa.jp/docs/t3u/dst/s9516276.html
    '''
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/querent.csv"
    file_path = os.path.join(RAWDATA_DIR, "querent.csv")
    download(url, file_path)


@task
def get_hospital(c):
    '''
    医療機関（病院）の状況
    https://www.pref.kanagawa.jp/docs/t3u/dst/s0361985.html
    '''
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/hospital.csv"
    file_path = os.path.join(RAWDATA_DIR, "hospital.csv")
    download(url, file_path)
