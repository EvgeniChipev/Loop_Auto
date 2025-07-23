import streamlit as st
import zipfile
import tempfile
import shutil
import os

from gcode.gcode_editor import process_gcode
from three_mf.unpacker import unpack_3mf, repackage_3mf

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

        # Run automation
        try:
            gcode_path, extracted_folder = unpack_3mf(input_path, tempdir)

            process_gcode(gcode_path, loop_count)
            repackage_3mf(extracted_folder, output_path)

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
