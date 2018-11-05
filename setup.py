from setuptools import setup

setup(
    name="pycalc",
    version="1.0",
    description="Pure-python command-line calculator.",
    author="Ira Revkina",
    author_email="irina_revkina@epam.com",
    packages=["pycalc", "tests"],
    test_suite="tests",
    python_requires='>=3.6',
    entry_points={
          'console_scripts': [
              'pycalc = pycalc.main:main',
          ],
       }
    )
