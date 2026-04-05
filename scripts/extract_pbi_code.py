import os
import glob

def main():
    # 1. Define paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    output_file = os.path.join(project_root, 'powerbi_codebase.txt')

    files_to_export = []

    # 2. Dynamically find the SemanticModel directory for TMDL files
    semantic_model_dirs = glob.glob(os.path.join(project_root, '*.SemanticModel'))
    if semantic_model_dirs:
        semantic_model_dir = semantic_model_dirs[0]
        definition_dir = os.path.join(semantic_model_dir, 'definition')
        if os.path.exists(definition_dir):
            tmdl_files = glob.glob(os.path.join(definition_dir, '**', '*.tmdl'), recursive=True)
            files_to_export.extend(tmdl_files)
            print(f"🔍 Found {len(tmdl_files)} TMDL files.")
        else:
            print(f"⚠️ Warning: 'definition' folder not found inside {os.path.basename(semantic_model_dir)}.")
    else:
        print("⚠️ Warning: No .SemanticModel directory found. Ensure this is a .pbip project.")

    # 3. Collect Documentation Files
    docs_dir = os.path.join(project_root, 'docs')
    if os.path.exists(docs_dir):
        doc_files = glob.glob(os.path.join(docs_dir, '**', '*.md'), recursive=True)
        doc_files.extend(glob.glob(os.path.join(docs_dir, '**', '*.txt'), recursive=True))
        files_to_export.extend(doc_files)
        print(f"🔍 Found {len(doc_files)} Documentation files.")
    else:
        print("⚠️ Warning: 'docs' directory not found.")

    # 4. Collect Script Files
    scripts_dir = os.path.join(project_root, 'scripts')
    if os.path.exists(scripts_dir):
        script_files = glob.glob(os.path.join(scripts_dir, '**', '*.py'), recursive=True)
        # Exclude the output file if it accidentally gets caught or placed here
        script_files = [f for f in script_files if not f.endswith('powerbi_codebase.txt')]
        files_to_export.extend(script_files)
        print(f"🔍 Found {len(script_files)} Script files.")
    else:
        print("⚠️ Warning: 'scripts' directory not found.")

    if not files_to_export:
        print("❌ Error: No files found to export.")
        return

    # 5. Read and stitch files together
    print(f"\n📦 Compiling {len(files_to_export)} total files into {os.path.basename(output_file)}...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("=== POWER BI PROJECT FULL EXPORT ===\n")
        outfile.write("This file contains the complete TMDL data model, project documentation, and automation scripts.\n")
        outfile.write("=" * 80 + "\n\n")

        for file_path in files_to_export:
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

    print(f"✅ Success! Full codebase exported to: {output_file}")

if __name__ == "__main__":
    main()