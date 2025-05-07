from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This fuction will return the list of requrements
    This is a parameter called file_path. The : str means it should be a string (i.e., a file path like "requirements.txt").
    This is a return type hint. It tells us the function will return a list of strings.
    : this starts the fucntion body
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Raj Rishi',
    author_email='rajrishisharma2000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

    
)