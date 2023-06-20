from setuptools import find_packages,setup

editable_installation_flag = '-e .'

def get_requirements(file_path):

    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]

        if editable_installation_flag in requirements:
            requirements.remove(editable_installation_flag)

    return requirements



setup(
      
    name='Breast Cancer Prediction',
    version = "0.0.1",
    author = 'Aman Vishwakarma',
    author_email = 'amansharma1729ds@gmail.com',
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()

)