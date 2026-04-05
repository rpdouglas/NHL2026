import os
import glob

def main():
    # 1. Define paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    output_file = os.path.join(project_root, 'powerbi_codebase.txt')

    # 2. Dynamically find the SemanticModel directory
    # (Assuming there is only one .SemanticModel folder in the root)
    semantic_model_dirs = glob.glob(os.path.join(project_root, '*.SemanticModel'))

    if not semantic_model_dirs:
        print("❌ Error: Could not find a .SemanticModel directory in the parent folder.")
        print("Make sure you saved the Power BI file as a .pbip project.")
        return

    semantic_model_dir = semantic_model_dirs[0]
    definition_dir = os.path.join(semantic_model_dir, 'definition')

    if not os.path.exists(definition_dir):
        print(f"❌ Error: Could not find the 'definition' folder inside {os.path.basename(semantic_model_dir)}.")
        print("Make sure TMDL format is enabled in your Power BI preview features.")
        return

    # 3. Recursively collect all .tmdl files
    tmdl_files = glob.glob(os.path.join(definition_dir, '**', '*.tmdl'), recursive=True)

    if not tmdl_files:
        print("⚠️ No .tmdl files found. Is the model empty?")
        return

    # 4. Read and stitch files together
    print(f"🔍 Found {len(tmdl_files)} TMDL files. Extracting...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("=== POWER BI TMDL CODEBASE EXPORT ===\n")
        outfile.write("This file contains the complete M queries, DAX measures, and relationships for the data model.\n")
        outfile.write("=" * 80 + "\n\n")

        for file_path in tmdl_files:
            # Get a clean relative path to use as the file header
            relative_path = os.path.relpath(file_path, project_root)
            
            outfile.write(f"// {'-' * 74}\n")
            outfile.write(f"// FILE: {relative_path}\n")
            outfile.write(f"// {'-' * 74}\n\n")
            
            try:
                # 'utf-8-sig' handles the Byte Order Mark (BOM) that Microsoft tools often add
                with open(file_path, 'r', encoding='utf-8-sig') as infile:
                    content = infile.read()
                    outfile.write(content)
            except Exception as e:
                outfile.write(f"// [ERROR READING FILE: {e}]\n")
            
            outfile.write("\n\n\n")

    print(f"✅ Success! Codebase exported to: {output_file}")

if __name__ == "__main__":
    main()