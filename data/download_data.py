from pathlib import Path
from openneuro import download
current_script_folder = Path(__file__).parent
download(
    dataset="ds005620",
    target_dir=str(current_script_folder)+'/ds005620',
    include=[
        "dataset_description.json",
        "participants*",
        "CHANGES*",
        "*task-awake_acq-EC*",
        "*task-sed_acq-rest*",
    ],
)






