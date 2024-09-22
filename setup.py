from setuptools import find_packages, setup


def get_requirements(requirements_file):
    with open(requirements_file,'r') as rf:
        tools=rf.readlines()
        tools=[req.replace("\n","") for req in tools if req!="-e ."]
    return tools


setup(
    name="Employee Management System",
    version="1.0.0",
    author="Ravi Yadav",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)