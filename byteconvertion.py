import os
import subprocess
import shutil
import glob


# Define the repositories and their corresponding branch/tag to build
repos = [
    {'url': 'https://github.com/dineshkhs/testv.git', 'ref': 'main'}
    
]

# Define the directory to store the generated wheel files
wheel_dir = 'wheelhouse'

# Define the Build directory to clone the repositories to

#if not os.path.exists("/Build"):
 #os.makedirs("/Build")

#tmp_dir = '/Build'


# Define a function to delete the .git folder from a given directory


# Clone each repository to the temporary directory and build the .whl package
for repo in repos:
    # Construct the clone command with the specified branch/tag
    clone_cmd = ['git', 'clone', '-b', repo['ref'], repo['url']]
    #clone_cmd = ['git', 'clone', '--depth','1','--branch', repo['commitID'], repo['url'], os.path.join(tmp_dir, repo['url'].split('/')[-1].split('.')[0])]
    
    # Clone the repository
    subprocess.check_call(clone_cmd)
        

    os.chdir(os.path.join(repo['url'].split('/')[-1].split('.')[0]))
   
    # Create a virtual environment
    subprocess.check_call(['python', '-m', 'venv','--upgrade-deps', '.venv'])
    
 
    # Activate the virtual environment
    activate_script = os.path.join('.venv', 'bin', 'activate')

    subprocess.rucheck_calln([activate_script, '&&','python', '-m','pip', 'install', 'wheel', 'setuptools','&&','exit'], check=True, shell=False)

   
    subprocess.check_call([activate_script,'&&','python', '-c', 'from setuptools import setup; setup()','bdist_egg','--exclude-source-files','&&','exit'], shell=False, check=True)
    
    
    #subprocess.run(['python', '-c', '"from setuptools import setup; setup()"','bdist_egg','--exclude-source-files'], check=True)

    subprocess.check_call([activate_script,'&&','python', '-m', 'wheel','convert','dist/*.egg','&&','exit'], shell=False, check=True)
    os.makedirs(os.path.join('..', wheel_dir), exist_ok=True)
    whl_file = os.path.join('.', glob.glob('*.whl')[0])
   # whl_file = os.path.join('.','*.whl')
    shutil.copy(whl_file, os.path.join('..', wheel_dir))
     
# Clean up the temporary directory
os.chdir('..')
#shutil.rmtree(tmp_dir)


