from setuptools import find_packages, setup
from typing import List

E_DOT = '-e .'

def get_requirements(file_name:str) -> List[str]:

    requirements = []
    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)

    return requirements        


setup(

    name='mlproject',
    version='1.0.0',
    author='Vishal B',
    author_email='vishalbabu1205@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)