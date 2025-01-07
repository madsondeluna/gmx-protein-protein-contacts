import os
import subprocess

# Define paths for the files
define_paths = {
    "contact_file": "contact_AB.dat",
    "transform_in": "transform-to-xyzmatrix.in",
    "transform_out": "transform-to-xyzmatrix.out",
    "awk_script": "transform-to-xyzmatrix.awk",
    "gnuplot_script": "heatmapplot.gnu",
    "output_graph": "heatmap_output.png",
}

# Step 1: Sort contacts

def sort_contacts(input_file, output_file):
    with open(input_file, "r") as f:
        lines = sorted(f.readlines())
    
    with open(output_file, "w") as f:
        f.write("\n")  # Add blank line at the beginning
        f.writelines(lines)
        f.write("END\n")  # Add END at the end

# Step 2: Transform to xyz-matrix

def transform_to_xyzmatrix(input_file, output_file, awk_script, init_res, final_res):
    command = [
        "awk",
        f"-v InitResChainA={init_res}",
        f"-v FinalResChainA={final_res}",
        "-f", awk_script,
        input_file,
    ]
    with open(output_file, "w") as out:
        subprocess.run(command, stdout=out)

# Step 3: Generate the heatmap using gnuplot

def generate_heatmap(gnuplot_script, output_graph):
    with open(gnuplot_script, "r") as f:
        script = f.read()
    script = script.replace(
        "set terminal ...",  # Modify this line to configure output type
        f"set terminal pngcairo; set output '{output_graph}'"
    )
    modified_script_path = "modified_heatmapplot.gnu"
    with open(modified_script_path, "w") as f:
        f.write(script)
    
    subprocess.run(["gnuplot", modified_script_path])

# Execution pipeline
def main():
    paths = define_paths

    # Step 1: Sort contacts
    print("Sorting contacts...")
    sort_contacts(paths["contact_file"], paths["transform_in"])

    # Step 2: Transform to xyz-matrix
    print("Transforming to xyz-matrix...")
    transform_to_xyzmatrix(
        paths["transform_in"],
        paths["transform_out"],
        paths["awk_script"],
        init_res=1,  # Example values; change as needed
        final_res=10
    )

    # Step 3: Generate the heatmap
    print("Generating heatmap...")
    generate_heatmap(paths["gnuplot_script"], paths["output_graph"])
    
    print("Analysis complete. Heatmap saved as", paths["output_graph"])

if __name__ == "__main__":
    main()
