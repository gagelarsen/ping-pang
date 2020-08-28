import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'requests >= 2.24.0'
]

setuptools.setup(
    name='ping-pang',
    version='1.1.3',
    description='Ping a URL and output the status code and latency. Save to a log or CSV on an interval.',  # noqa
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/ping-pang',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
            'mock >= 4.0.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'ping-pang=pingpang.ping_logic.PingPangCLI'
        ]
    },
    python_requires='>=3.6',
)
