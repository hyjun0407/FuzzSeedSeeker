import subprocess
import os
import shutil
     
previous_files = []


def find_lines_with_string(filename, search_string):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if search_string in line:
                    return line.strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def count_lines_with_string(filename, target_string):
    count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if target_string in line:
                    count += 1
    except FileNotFoundError:
        print(f"File '{filename}'not exist")
    except Exception as e:
        print(f"error: {str(e)}")

    return count

def make_temp_covfold(directory_path):
    try:
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            print(f"'{directory_path}' removed")
        
        os.makedirs(directory_path)
        print(f"'{directory_path}' recreated")
    except Exception as e:
        print(f"error: {str(e)}")

def run_dynamic_rio(run_process_command,filename):
    dynamic_rio_path = "C:\\Users\\hyjun\\Downloads\\DynamoRIO-Windows-10.0.0\\bin64\\drrun.exe -t drcov -logdir C:\\CoverageDump -dump_text -- " + run_process_command.replace("@@",filename)
    try:
        subprocess.run(dynamic_rio_path, shell=True)
    except FileNotFoundError:
        print(f"not found '{dynamic_rio_path}'")
    except Exception as e:
        print(f"error: {str(e)}")

def find_files_with_string(directory, search_string):
    result = []

    for root, _, files in os.walk(directory):
        for filename in files:
            if search_string in filename:
                result.append(os.path.join(root, filename))

    return result

def rename_new_files(file_path, new_file_paths):        
        try:
            os.rename(file_path, new_file_paths)
        except Exception as e:
            print(f"error: {str(e)}")

def make_cov_file(coverageDumpPath, coverageFilePath):
    make_temp_covfold(coverageDumpPath)

    search_string = 'drcov'

    if os.path.exists(coverageFilePath):
        for root, dirs, files in os.walk(coverageFilePath):
            for file in files:
                file_path = os.path.join(root, file)
                
                run_process_command = "C:\\Users\\hyjun\\Downloads\\DefenderFuzzing-ver3\\x64\\Release\\HarnessForDef.exe -f @@"
                filename = file_path.replace(coverageFilePath+"\\","")
                run_dynamic_rio(run_process_command,file_path)

                new_path = find_files_with_string(coverageDumpPath, search_string)
                new_filename = new_path[0].replace(coverageDumpPath+"\\","")
                parts = filename.split(".")
                #if len(parts) > 1:
                #    parts[-1] = "cov"
                #    filenamewithcov = ".".join(parts)
                #else:
                filenamewithcov = filename + ".cov"
                rename_new_files(new_path[0],new_path[0].replace(new_filename,filenamewithcov))
    else:
        print(f"'{coverageFilePath}' directory Not Found")


def Check_cov_per_file(modulename,covfilepath):
    if os.path.exists(covfilepath):
        results = {}
        for root, dirs, files in os.walk(covfilepath):
            for file in files:
                file_path = os.path.join(root, file)

                search_string = modulename
                finded_one = find_lines_with_string(file_path, search_string)   
                if(finded_one != None):
                    parts = finded_one.split(',')
                    first_number = parts[0].strip()
                    firstnum = int(first_number)
                    if firstnum < 10:
                        search_string1 = "module[  x]"
                        modified_string = search_string1.replace("[  x]", f"[  {first_number}]")
                    else:
                        search_string1 = "module[ x]"
                        modified_string = search_string1.replace("[ x]", f"[ {first_number}]")
                    finded_module = count_lines_with_string(file_path,modified_string)
                    results[file_path] = finded_module
                else:
                    results[file_path] = 0
        print("")
        print("---------------------------------------------------")
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
        for file_path, finded_module in sorted_results:
            print(file_path + "'s Count : " + str(finded_module))
        print("---------------------------------------------------")



#make_cov_file("C:\\CoverageDump","C:\\CoverageValidate")
Check_cov_per_file("mpengine.dll", "C:\\CoverageDump")
