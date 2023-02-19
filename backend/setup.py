from setuptools import setup

setup(
    name="app",
    packages=["app", "app/controller"],
    include_package_data=True,
    install_requires=['flask']
)