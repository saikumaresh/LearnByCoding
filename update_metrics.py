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


def count_files_and_directories(base_path):
    directory_structure = {}  # To store the directory structure and file count

    for dirpath, dirnames, filenames in os.walk(base_path):
        # Skip hidden files and directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        filenames = [f for f in filenames if not f.startswith('.')]

        if dirpath == base_path:
            # Skip the root directory itself from being added to the structure
            continue

        file_count = len(filenames)
        if file_count > 0:
            directory_structure[dirpath] = file_count
        else:
            subdirs = [d for d in dirnames if os.path.isdir(os.path.join(dirpath, d))]
            if subdirs:
                directory_structure[dirpath] = len(subdirs)
            else:
                directory_structure[dirpath] = 0

    return directory_structure

def format_directory_structure(directory_structure):
    formatted_structure = ""
    for directory, count in directory_structure.items():
        # Split the directory path into parts
        parts = directory.split(os.sep)
        indent = "│   " * (len(parts) - 1)
        folder_name = parts[-1]

        if count == 0:
            formatted_structure += f"{indent}└── {folder_name}/\n"
        else:
            formatted_structure += f"{indent}├── {folder_name}/ ({count})\n"
    return formatted_structure

def update_readme_repo():
    base_path = get_repo_root()
    directory_structure = count_files_and_directories(base_path)

    readme_path = os.path.join(base_path, 'README.md')
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

    # Prepare the metrics content
    metrics_content = [
        f'📁 Total Number of Files: {sum(1 for f in directory_structure.values() if f > 0)}\n',
        f'📂 Total Number of Directories: {len(directory_structure)}\n',
        f'\n## 📂 Repository Structure\n\n' + format_directory_structure(directory_structure)
    ]
    
    # Update the README content by replacing the old metrics section
    content[start_index:end_index] = metrics_content

    # Write the updated content to the README file
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(content)

if __name__ == '__main__':
    update_readme()
    update_readme_repo()
