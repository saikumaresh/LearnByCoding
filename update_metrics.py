import os
import subprocess

# Get the repository root directory instead of the current working directory
def get_repo_root():
    # Use 'git rev-parse --show-toplevel' to get the repository root directory
    return subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode('utf-8')

def count_files_and_directories(base_path):
    total_files = 0
    total_dirs = 0
    python_files = 0
    total_lines = 0
    
    # Traverse all directories and files starting from base_path
    for dirpath, dirnames, filenames in os.walk(base_path):
        # Skip hidden directories and files
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        filenames = [f for f in filenames if not f.startswith('.')]  # Skip hidden files
        
        total_dirs += 1  # Count each directory found
        for file in filenames:
            total_files += 1  # Count each file found
            if file.endswith('.py'):
                python_files += 1  # Count Python files
            
            # Use 'errors="ignore"' to skip unreadable files
            try:
                with open(os.path.join(dirpath, file), 'r', errors='ignore') as f:
                    total_lines += len(f.readlines())  # Count lines in the file
            except Exception as e:
                print(f"Skipping file due to error: {file}. Error: {e}")

    return total_files, total_dirs, total_lines, python_files

def update_readme():
    # Get the base path to the repository root
    base_path = get_repo_root()
    
    total_files, total_dirs, total_lines, python_files = count_files_and_directories(base_path) 

    readme_path = os.path.join(base_path, 'README.md')  # Ensure correct path to README.md
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"{readme_path} not found!")
        return

    try:
        start_index = content.index('<!-- metrics-section-start -->\n') + 1
        end_index = content.index('<!-- metrics-section-end -->\n')
    except ValueError:
        print("Metrics section markers not found in README.md.")
        return

    # Update the metrics section
    metrics_content = [
        f'📁 Total Number of Files: {total_files} \n','\n',
        f'📂 Total Number of Directories: {total_dirs} \n','\n',
        f'🐍 Total Number of Python files: {python_files} \n','\n',
        f'📜 Total Number of Lines of Code: {total_lines} \n','\n',
    ]

    content[start_index:end_index] = metrics_content

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(content)

def generate_repo_structure(repo_path):
    """
    Generate repository structure in 'DirectoryName(FileCount)' format.
    """
    structure_lines = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files = [f for f in files if not f.startswith('.')]
        level = root.replace(repo_path, "").count(os.sep)
        indent = "  " * level
        folder_name = os.path.basename(root) or "Root"
        file_count = len(files)
        structure_lines.append(f"{indent}- {folder_name} ({file_count})")
    return structure_lines

def update_readme_repo(repo_path, readme_file):
    """
    Update README with metrics and repository structure.
    """
    # Generate repository structure
    structure_lines = generate_repo_structure(repo_path)

    with open(readme_file, "r") as f:
        content = f.readlines()

    # Update Metrics Section (if needed)

    # Update Repository Structure Section
    start_marker = "## 📂 Repository Structure\n"
    start_idx = content.index(start_marker) + 1
    end_idx = start_idx
    while end_idx < len(content) and content[end_idx].startswith("  "):
        end_idx += 1

    # Replace with new structure
    updated_content = (
        content[:start_idx]
        + [line + "\n" for line in structure_lines]
        + content[end_idx:]
    )

    with open(readme_file, "w") as f:
        f.writelines(updated_content)

if __name__ == '__main__':
    update_readme()
    repo_path = "."  # Repository root
    readme_file = "README.md"
    update_readme_repo(repo_path, readme_file)
