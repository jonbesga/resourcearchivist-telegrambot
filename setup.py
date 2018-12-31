from setuptools import setup, find_packages

setup(
    name='resource-archivist',
    version='0.1.0',
    description='',
    author='Jon Besga',
    author_email='jonan.bsg@gmail.com',
    packages=find_packages(),
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'archivist=archivist.main:run',
        ],
    },
)
