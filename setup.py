from setuptools import setup, find_packages

setup(
    name='ShapeSet',
    version='0.1.0',
    author='Manideep Reddy Enugala',
    author_email='enugalamanideepreddy99@gmail.com',
    description='This package helps to add and multiply two numbers',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=["numpy","opencv-python","tqdm"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)