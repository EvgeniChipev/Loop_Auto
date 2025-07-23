import zipfile
import os
import shutil

def unpack_3mf(filepath, extract_to):
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)

    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Look specifically for Metadata/plate_1.gcode
    target_gcode = os.path.join(extract_to, 'Metadata', 'plate_1.gcode')
    if os.path.isfile(target_gcode):
        return target_gcode

    raise FileNotFoundError("'Metadata/plate_1.gcode' not found in 3MF archive")

def repackage_3mf(folder, output_path):
    shutil.make_archive("temp_output", 'zip', folder)
    os.rename("temp_output.zip", output_path)
