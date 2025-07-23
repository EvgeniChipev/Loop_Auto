import os

def load_gcode(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

def save_gcode(filepath, lines):
    with open(filepath, 'w') as f:
        f.writelines(lines)

def process_gcode(gcode_path, loop_count):
    start_template = load_gcode("gcode/templates/start_a1.gcode")
    end_template = load_gcode("gcode/templates/end_a1.gcode")

    with open(gcode_path, 'r') as f:
        original = f.readlines()

    try:
        start_index = next(i for i, line in enumerate(original) if ";LAYER:0" in line)
        end_index = next(i for i, line in reversed(list(enumerate(original))) if ";END" in line or ";LAYER_END" in line)
    except StopIteration:
        raise Exception("Could not find printable section")

    model_block = original[start_index:end_index]

    result = start_template.copy()
    for _ in range(loop_count):
        result += model_block
    result += end_template

    save_gcode(gcode_path, result)
    print("✅ G-code processed with", loop_count, "loops.")
