import os
from invoke import task, run

import src.tool as tool
import src.constants as constants


@task
def evaluate_notebook(c):
    '''
    コロナのデータ分析のためのJupyter Notebookを評価
    '''
    command_base = "jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute --inplace --ExecutePreprocessor.kernel_name=python"
    file_path = os.path.join("notebooks", "kanagawa-corona.ipynb")
    command = " ".join([command_base, file_path])

    run(command)


@task
def get_rawdata(c):
    '''
    神奈川県が公開しているコロナに関するオープンデータを取得
    '''
    get_patients(c)
    get_contacts(c)
    get_querent(c)
    get_hospital(c)


@task
def get_patients(c):
    '''
    陽性患者数及び陽性患者の属性データ
    http://www.pref.kanagawa.jp/docs/t3u/dst/s0060925.html
    '''
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/patient.csv"
    tool.download_csv(url, constants.PATIENTS_RAWFILE_PATH)


@task
def get_contacts(c):
    '''
    専用ダイヤル相談件数
    http://www.pref.kanagawa.jp/docs/t3u/dst/s0352970.html
    '''
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/contacts.csv"
    tool.download_csv(url, constants.CONTACTS_RAWFILE_PATH)


@task
def get_querent(c):
    '''
    帰国者・接触者電話相談センター相談件数
    https://www.pref.kanagawa.jp/docs/t3u/dst/s9516276.html
    '''
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/querent.csv"
    tool.download_csv(url, constants.QUERENT_RAWFILE_PATH)


@task
def get_hospital(c):
    '''
    医療機関（病院）の状況
    https://www.pref.kanagawa.jp/docs/t3u/dst/s0361985.html
    '''
    url = "http://www.pref.kanagawa.jp/osirase/1369/data/csv/hospital.csv"
    tool.download_csv(url, constants.HOSPITAL_RAWFILE_PATH)
