import os

current_directory = os.getcwd()
print('Current working directory:', current_directory)

new_directory = 'C:/DATA/work/learning/python/local_pythonProject'
os.chdir(new_directory)
current_directory = os.getcwd()
print("Current working directory after change:", current_directory)

directory = 'C:/DATA/work/learning/python/local_pythonProject'
for dirpath, dirnames, filenames in os.walk(directory):
    print('Directory:', dirpath)
    print('Subdirectories:', dirnames)
    print('Files:', filenames)
    print()

new_directory_name = 'C:/DATA/work/learning/python/local_pythonProject/test'
os.mkdir(new_directory_name)
print(f"The Directory'{new_directory_name}' was created successfully.")

new_directory_name = 'test_1/test_2'
os.makedirs(new_directory_name)
print(f"The Directory '{new_directory_name}' and subdirectories were created successfully.")

directory_to_remove = "my_test"
os.removedirs(directory_to_remove)
print(f"The Directory '{directory_to_remove}' and subdirectories were deleted.")

directory_to_remove_1 = "test2"
os.rmdir(directory_to_remove_1)
print(f'The Directory \'{directory_to_remove_1}\' was deleted.')

old_name = 'test'
new_name = 'double_test'
os.rename(old_name, new_name)
print(f"File or Directory '{old_name}' was renamed by '{new_name}'.")

path = 'C:/DATA/work/learning/python/local_pythonProject/double_test'
file_info = os.stat(path)
print(f"Size: {file_info.st_size} bites")

environment_variables = os.environ
print('Environment Variables')
for key, value in environment_variables.items():
    print(f"{key}: {value}")

variable_name = 'pythonProject'
variable_value = os.environ.get(variable_name)
if variable_value is not None:
    print(f"Environment variable value '{variable_name}': {variable_value}")
else:
    print(f"Environment variable '{variable_name}' does not exist.")

folder = 'local_pythonProject'
sub_folder = 'test_1'
filename = 'text.txt'
full_path = os.path.join(folder, sub_folder, filename)
print(f"The path is: {full_path}")

file_path = '/local_pythonProject/test_1/text.txt'
dir_name, base_name = os.path.split(file_path)
print(f"Directory name: {dir_name}")
print(f"File name: {base_name}")

file_path = '/local_pythonProject/test_1/text.txt'
file_name = os.path.basename(file_path)
print(f"File name: {file_name}")

file_path = '/local_pythonProject/test_1/text.txt'
directory_name = os.path.dirname(file_path)
print(f"Directory name: {directory_name}")
