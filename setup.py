#!/usr/bin/env python3

# Developed by Tezign.com
# All rights reserved.


from setuptools import setup, find_packages


setup(
    name="jupyterhub-feishu-oauthenticator",
    version="0.0.1",
    description="FeiShu OAuthenticator for Jupyterhub",
    author="Tezign",
    author_email="support@tezign.com",
    url="https://github.com/tezignlab/jupyterhub_feishu_authenticator",
    install_requires=['oauthenticator>=14.0.0'],
    packages=find_packages(),
)
