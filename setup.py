# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Setup the eventhubs module.

"""

import eventhubs
from setuptools import setup

setup(name='eventhubs',
      version=eventhubs.__version__,
      description='Python client library for Azure Event Hubs',
      url='http://github.com/azure/azure-event-hubs-python',
      author='microsoft',
      license='MIT',
      packages=['eventhubs'],
      zip_safe=False)
