from setuptools import setup, find_packages

setup(
    name="Chakra_Recon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scapy==2.5.0",
        "ipaddress==1.0.23",
        "typing-extensions==4.5.0",
    ],

) 
