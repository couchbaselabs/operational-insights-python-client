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

"""Routing the SDK's logs into an application's own logging setup.

The SDK logs through Python's standard logging module and never configures the root logger, so an
application integrates with it the same way it would with any other library: attach a handler to the
SDK's logger and set the level.
"""

import logging
import sys

from couchbase_operational_insights import LOG_DATE_FORMAT, LOG_FORMAT, LOGGER_NAME
from couchbase_operational_insights.cluster import Cluster
from couchbase_operational_insights.credential import Credential


def configure_application_logging() -> None:
    # Whatever the application already does.  Here, a handler on stdout using the SDK's own format.
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT))

    # LOGGER_NAME is 'couchbase_operational_insights'.
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)


def main() -> None:
    configure_application_logging()

    # Update this to your cluster
    endpoint = 'https://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(endpoint, cred)

    statement = 'SELECT * FROM `travel-sample`.inventory.airline LIMIT 10;'
    res = cluster.execute_query(statement)
    for row in res.rows():
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')


if __name__ == '__main__':
    main()
