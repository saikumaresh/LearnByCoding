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

def count_files_in_directory(directory):
    """Counts files in the specified directory and all its subdirectories."""
    return sum([len(files) for _, _, files in os.walk(directory)])

def generate_directory_structure(directory, level=0):
    """Generates a string representing the directory structure."""
    structure = ""
    folder_items = sorted(os.listdir(directory))
    for item in folder_items:
        item_path = os.path.join(directory, item)
        
        # Get the relative path for display and count files in the folder
        relative_path = os.path.relpath(item_path, start=directory)
        file_count = count_files_in_directory(item_path) if os.path.isdir(item_path) else None

        # Add folder or file with appropriate indentation and file count
        if os.path.isdir(item_path):
            # Format file count as '(X)' if there are files inside, else empty
            count_display = f" ({file_count})" if file_count > 0 else ""
            structure += f"{'│   ' * level}├── {item}{count_display}\n"
            # Recursive call for subdirectory
            structure += generate_directory_structure(item_path, level + 1)
    
    return structure

def update_readme_structure():
    """Updates the README.md file with the directory structure and file counts."""
    structure = generate_directory_structure(os.getcwd())
    
    readme_path = "README.md"
    with open(readme_path, "r") as readme_file:
        lines = readme_file.readlines()

    # Find the line in README where the directory structure should be inserted
    start_idx, end_idx = None, None
    for i, line in enumerate(lines):
        if line.strip() == "## Repository Structure":
            start_idx = i + 1
        elif start_idx and line.strip().startswith("##"):
            end_idx = i
            break
    if end_idx is None:
        end_idx = len(lines)

    # Insert the new directory structure between start_idx and end_idx
    updated_lines = lines[:start_idx] + [structure] + lines[end_idx:]
    
    with open(readme_path, "w") as readme_file:
        readme_file.writelines(updated_lines)

if __name__ == '__main__':
    update_readme()
    update_readme_structure()
