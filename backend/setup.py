from setuptools import setup

setup(
    name="app",
    packages=["app", "models", "router", "helpers", "colored_print"],
    include_package_data=True,
    install_requires=['flask']
)