from setuptools import find_packages, setup
from typing import List

Hypen_E_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    'this function will return the list of requiremenst'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        
        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)
    return requirements
                


setup(
    name='MLproject',
    version='0.0.1',
    author='Nahid-droid',
    author_email='mammadovnahid08@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)