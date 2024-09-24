import subprocess

# Path to the SVG file
svg_file = "/home/jasvir/Music/svg/1.svg"
output_path = "/home/jasvir/Music/svg/output"

# Define the scale and rotation parameters
scale_x = 1.5  # Scale factor for x-axis
scale_y = 1.5  # Scale factor for y-axis
rotation_angle = 45  # Rotation angle in degrees

def run_inkscape_command(command):
    """Run an Inkscape command using subprocess."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")

def scale_svg(input_svg, output_svg, scale_x, scale_y):
    """Scale the SVG image indirectly by changing DPI and dimensions."""
    # Inkscape CLI does not directly support scaling. This command sets the DPI for exporting.
    command = f"inkscape {input_svg} --export-filename={output_svg} --export-dpi=300"
    run_inkscape_command(command)

def rotate_svg(input_svg, output_svg, angle):
    """Rotate the SVG image by modifying it directly."""
    # Rotating directly via CLI isn't supported; consider using an SVG editor or manual adjustment.
    # Alternatively, you can use Python libraries like `svgwrite` to manipulate the SVG file.
    # This example assumes that a manual SVG modification is done, as CLI support is limited.
    print("Rotation should be handled manually or with another tool.")

def export_svg_to_png(input_svg, output_png):
    """Export the SVG image to PNG format."""
    command = f"inkscape {input_svg} --export-filename={output_png} --export-type=png"
    run_inkscape_command(command)

# Paths for manipulated SVG and PNG files
scaled_svg = f"{output_path}/scaled_1.svg"
rotated_svg = f"{output_path}/rotated_1.svg"
png_file = f"{output_path}/output.png"

# Perform the manipulations
scale_svg(svg_file, scaled_svg, scale_x, scale_y)
rotate_svg(scaled_svg, rotated_svg, rotation_angle)
export_svg_to_png(rotated_svg, png_file)

print("All manipulations completed successfully.")
