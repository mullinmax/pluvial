# If you do not want to use a setup.py file you can use a requirements.txt file instead and the build will use that instead

from setuptools import setup, find_packages

setup_dict = {
    name:'beryl',
    version:'0.0.2',
    packages:find_packages(),  # Automatically finds identifies packages in repo to include
    include_package_data:True,  # if non-Python files should be included
    description:'Markdown-based static site generator',
	long_description:open('README.md').read(),
	long_description_content_type:'text/markdown',
    author:'Maxwell Mullin',  # author of your project
    author_email:'inbox@max-was-here.com',  # author's email address
	license:'MIT'
	classifiers:[
		# https://pypi.org/classifiers/
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Topic :: Internet :: WWW/HTTP',

		# Pick your license as you wish (should match "license" above)
		'License :: OSI Approved :: MIT License',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11'
	],
    python_requires:'>=3.6, <3.11',  # min and max supported versions of Python
    install_requires:[  # packages required to run your project
        'flask',
        'waitress',
        'markdown',
        'beautifulsoup4',
        'pygments'
    ],
    extras_require:{  # optional dependencies for building or testing your project
        'build':[
            # dependencies required for building your package
        ],
        'test':[
            # dependencies required for testing your package
            'pytest'
        ],
    },
}

setup(**setup_dict)
