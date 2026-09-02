#  Copyright 2016-2025. Couchbase, Inc.
#  All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import os
import sys

from setuptools import setup

sys.path.append('.')
import couchbase_operational_insights_version  # nopep8 # isort:skip # noqa: E402

try:
    couchbase_operational_insights_version.gen_version()
except couchbase_operational_insights_version.CantInvokeGit:
    pass

PYCBOI_README = os.path.join(os.path.dirname(__file__), 'README.md')
PYCBOI_VERSION = couchbase_operational_insights_version.get_version()

print(f'Python Operational Insights SDK version: {PYCBOI_VERSION}')

setup(
    name='couchbase-operational-insights',
    version=PYCBOI_VERSION,
    long_description=open(PYCBOI_README, 'r').read(),
    long_description_content_type='text/markdown',
)
