import setuptools

setuptools.setup(
    name="atig",
    version="0.0.1",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts':
        ['atig=main:main'],
    })
