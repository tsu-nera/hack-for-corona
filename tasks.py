import os
from invoke import task, run


@task
def evaluate_notebook(c):
    command_base = "jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute --inplace --ExecutePreprocessor.kernel_name=python"
    file_path = os.path.join("notebooks", "kanagawa-corona.ipynb")
    command = " ".join([command_base, file_path])

    run(command)
