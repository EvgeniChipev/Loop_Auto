import zipfile
import os
import shutil

def unpack_3mf(filepath, extract_to):
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)

    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    for root, dirs, files in os.walk(extract_to):
        for file in files:
            if file.endswith(".gcode"):
                return os.path.join(root[len(extract_to)+1:], file)

    raise FileNotFoundError("G-code file not found in 3MF")

def repackage_3mf(folder, output_path):
    shutil.make_archive("temp_output", 'zip', folder)
    os.rename("temp_output.zip", output_path)
