import zipfile
import os
import shutil

def unpack_3mf(filepath, extract_to):
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)

    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Find the top-level folder (usually named after the .3mf file)
    extracted_items = os.listdir(extract_to)
    for item in extracted_items:
        item_path = os.path.join(extract_to, item)
        if os.path.isdir(item_path):
            target_gcode = os.path.join(item_path, 'Metadata', 'plate_1.gcode')
            if os.path.isfile(target_gcode):
                return target_gcode, item_path

    raise FileNotFoundError("'Metadata/plate_1.gcode' not found in 3MF archive (checked inside top-level folders)")

def repackage_3mf(folder, output_path):
    # Get the directory and base name for the output
    output_dir = os.path.dirname(output_path)
    base_name = os.path.splitext(output_path)[0]
    # Create the archive in the same directory as output_path
    shutil.make_archive(base_name, 'zip', folder)
    os.rename(base_name + ".zip", output_path)
