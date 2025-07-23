from three_mf.unpacker import unpack_3mf, repackage_3mf
from gcode.gcode_editor import process_gcode
import os

def automate_3mf(input_file, output_file, loop_count=3):
    unpack_dir = "temp"
    gcode_filename = unpack_3mf(input_file, unpack_dir)
    gcode_path = os.path.join(unpack_dir, gcode_filename)

    process_gcode(gcode_path, loop_count)
    repackage_3mf(unpack_dir, output_file)

if __name__ == "__main__":
    automate_3mf("input.3mf", "output_looped.3mf", loop_count=3)
