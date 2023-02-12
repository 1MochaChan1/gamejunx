from setuptools import setup

setup(
    name="app",
    packages=["app", "models"],
    include_package_data=True,
    install_requires=['flask']
)