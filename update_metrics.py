import os

def count_lines_of_code():
    total_loc = 0
    allowed_extensions = {'.py', '.txt'}  # Specify the allowed file extensions
    for root, dirs, files in os.walk('.'):
        for file in files:
            if not any(file.endswith(ext) for ext in allowed_extensions):
                continue  # Skip files that do not have the specified extensions
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    total_loc += len(f.readlines())
            except (UnicodeDecodeError, FileNotFoundError) as e:
                print(f"Skipping file due to decoding issue: {file}")
                continue
    return total_loc

def count_commits():
    # This is a placeholder. Implement your commit counting logic here.
    return 0

def calculate_code_coverage():
    # This is a placeholder. Implement your code coverage calculation here.
    return 0.0

def update_readme():
    total_loc = count_lines_of_code()  # Count lines of code
    total_commits = count_commits()  # Count total commits
    code_coverage = calculate_code_coverage()  # Calculate code coverage

    readme_path = 'README.md'
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
        f'Total Number of Lines of Code: {total_loc}\n','\n',
        f'Total Number of Commits: {total_commits}\n','\n',
        f'Percentage of Code Coverage: {code_coverage:.2f}%\n',
    ]

    content[start_index:end_index] = metrics_content

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(content)

if __name__ == '__main__':
    update_readme()