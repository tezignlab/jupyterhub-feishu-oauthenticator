#!/usr/bin/env python3

# Developed by Tezign.com
# All rights reserved.


from setuptools import setup, find_packages


setup(
    name="jupyterhub-feishu-oauthenticator",
    version="0.1.0",
    description="FeiShu OAuthenticator for Jupyterhub",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Tezign",
    author_email="dev@tezign.com",
    url="https://github.com/tezignlab/jupyterhub_feishu_authenticator",
    install_requires=['oauthenticator>=14.0.0'],
    packages=find_packages(),
)
