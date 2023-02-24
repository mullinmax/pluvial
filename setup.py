# If you do not want to use a setup.py file you can use a requirements.txt file instead and the build will use that instead

from setuptools import setup, find_packages

setup(
    name='beryl',  # name of your project
    version='0.0.2',  # version number of your project
    packages=find_packages(),  # packages to include in your project
    include_package_data=True,  # include non-Python files in your package
    description='Markdown-based static site generator',  # brief description of your project
    author='Maxwell Mullin',  # author of your project
    author_email='inbox@max-was-here.com',  # author's email address
    python_requires='>=3.6',  # minimum required version of Python for your project
    install_requires=[  # packages required to run your project
        'flask',
        'waitress',
        'markdown',
        'beautifulsoup4',
        'pygments'
    ],
    extras_require={  # optional dependencies for building or testing your project
        'build': [
            # dependencies required for building your package
        ],
        'test': [
            # dependencies required for testing your package
            'pytest'
        ],
    },
)
