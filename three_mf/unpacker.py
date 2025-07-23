import zipfile
import os
import shutil

def unpack_3mf(filepath, extract_to):
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)

    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Look for Metadata/plate_1.gcode at any depth
    for root, dirs, files in os.walk(extract_to):
        for file in files:
            if file == "plate_1.gcode" and "Metadata" in root:
                extracted_folder = root.split("Metadata")[0].rstrip(os.sep)
                print(f"DEBUG: Found plate_1.gcode at {os.path.join(root, file)}; extracted_folder: {extracted_folder}")
                return os.path.join(root, file), extracted_folder

    raise FileNotFoundError("'Metadata/plate_1.gcode' not found in 3MF archive (checked all locations)")

def repackage_3mf(folder, output_path):
    output_dir = os.path.dirname(output_path)
    base_name = os.path.splitext(output_path)[0]
    print("DEBUG: Before make_archive, output_dir:", output_dir, "base_name:", base_name, "folder:", folder)
    print("DEBUG: Files in output_dir before:", os.listdir(output_dir))
    shutil.make_archive(base_name, 'zip', folder)
    print("DEBUG: Files in output_dir after make_archive:", os.listdir(output_dir))
    os.rename(base_name + ".zip", output_path)
    print("DEBUG: Files in output_dir after rename:", os.listdir(output_dir))
