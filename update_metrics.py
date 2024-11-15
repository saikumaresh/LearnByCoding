import os
import subprocess

# Get the repository root directory instead of the current working directory
def get_repo_root():
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
        filenames = [f for f in filenames if not f.startswith('.') and f != '.gitkeep']  # Exclude .gitkeep

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
    base_path = get_repo_root()

    total_files, total_dirs, total_lines, python_files = count_files_and_directories(base_path) 

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
    """Counts the number of valid files in the specified directory, excluding .gitkeep files."""
    return sum(
        1 for root, _, files in os.walk(directory)
        for file in files if file != '.gitkeep'
    )

def generate_directory_structure(directory, prefix=''):
    """Generates a neatly formatted directory structure with file counts, excluding .gitkeep files."""
    structure = ''
    items = sorted(os.listdir(directory))
    for index, item in enumerate(items):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            file_count = count_files_in_directory(item_path)
            count_display = f' ({file_count})' if file_count > 0 else ''
            connector = '└── ' if index == len(items) - 1 else '├── '
            structure += f"{prefix}{connector}{item}/{count_display}\n"
            extension = '    ' if index == len(items) - 1 else '│   '
            structure += generate_directory_structure(item_path, prefix + extension)
    return structure

def update_readme_structure():
    """Updates the README.md file with the directory structure and file counts."""
    base_path = get_repo_root()
    structure = generate_directory_structure(base_path)
    readme_path = os.path.join(base_path, 'README.md')
    with open(readme_path, 'r') as readme_file:
        lines = readme_file.readlines()

    start_marker = '<!-- START OF DIRECTORY STRUCTURE -->\n'
    end_marker = '<!-- END OF DIRECTORY STRUCTURE -->\n'

    try:
        start_idx = lines.index(start_marker) + 1
        end_idx = lines.index(end_marker)
    except ValueError:
        print("Markers not found in README.md. Please ensure the markers are present.")
        return

    updated_lines = lines[:start_idx] + [structure] + lines[end_idx:]

    with open(readme_path, 'w') as readme_file:
        readme_file.writelines(updated_lines)

if __name__ == '__main__':
    update_readme()
    update_readme_structure()
