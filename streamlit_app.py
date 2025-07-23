import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import zipfile
import tempfile
import shutil
import importlib

from gcode.gcode_editor import process_gcode
# from three_mf.unpacker import unpack_3mf, repackage_3mf
import importlib
three_mf_unpacker = importlib.import_module('three_mf.unpacker')
unpack_3mf = three_mf_unpacker.unpack_3mf
repackage_3mf = three_mf_unpacker.repackage_3mf

# Debug block to show sys.path and directory contents
try:
    st.info("Debug: sys.path and directory listing")
    root_dir = os.path.dirname(os.path.abspath(__file__))
    three_mf_dir = os.path.join(root_dir, 'three_mf')
    st.code(f"sys.path: {sys.path}\n\nRoot dir: {os.listdir(root_dir)}\n\nthree_mf dir: {os.listdir(three_mf_dir)}")
except Exception as e:
    st.error(f"Debug error: {e}")

st.title("🛠️ Bambu Loop Automator")
st.write("Upload a `.3mf` file and loop your model automatically with your custom G-code templates.")

uploaded_file = st.file_uploader("Upload your .3mf file", type=["3mf"])
loop_count = st.number_input("Number of print loops", min_value=1, max_value=50, value=3)

if uploaded_file:
    with tempfile.TemporaryDirectory() as tempdir:
        input_path = os.path.join(tempdir, uploaded_file.name)
        output_path = os.path.join(tempdir, "output_looped.3mf")

        # ✅ Fixed file saving for zipfile to work
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("input_path exists:", os.path.isfile(input_path))
        st.write("input_path:", input_path)

        # Check if the uploaded file is a valid zip archive
        import zipfile
        if not zipfile.is_zipfile(input_path):
            st.error("The uploaded file is not a valid .3mf (zip) file. Please check your file and try again.")
            st.stop()

        # Debug: Show contents of the zip before extraction
        with zipfile.ZipFile(input_path, 'r') as zip_ref:
            st.write("Files in .3mf zip:", zip_ref.namelist())

        # Run automation
        try:
            gcode_path, extracted_folder = unpack_3mf(input_path, tempdir)

            process_gcode(gcode_path, loop_count)
            repackage_3mf(extracted_folder, output_path)

            # Debug output (visually prominent)
            st.info("Debug Output:")
            st.code(f"Output path: {output_path}\nFiles in tempdir: {os.listdir(tempdir)}\nIs output_path a file? {os.path.isfile(output_path)}")

            with open(output_path, "rb") as f:
                st.download_button("📥 Download Modified 3MF", f, file_name="looped_output.3mf")

        except Exception as e:
            # Debug: List all files and directories in tempdir
            debug_files = []
            for root, dirs, files in os.walk(tempdir):
                for name in files:
                    debug_files.append(os.path.join(root, name))
            st.write("Files in tempdir after extraction:", debug_files)
            st.error(f"❌ Error: {str(e)}")
