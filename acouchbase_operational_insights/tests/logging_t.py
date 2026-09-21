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


from __future__ import annotations

import pytest

from acouchbase_operational_insights.protocol._core.client_adapter import _AsyncClientAdapter
from couchbase_operational_insights.credential import Credential

TEST_CLUSTER_ID = 'test-cluster'


class LogPrefixTestSuite:
    TEST_MANIFEST = [
        'test_prefix_before_client_created_is_not_cached',
        'test_prefix_reflects_secure_connection',
    ]

    @staticmethod
    def _adapter(http_endpoint: str = 'http://localhost:8095') -> _AsyncClientAdapter:
        cred = Credential.from_username_and_password('Administrator', 'password')
        return _AsyncClientAdapter(http_endpoint, cred, cluster_id=TEST_CLUSTER_ID)

    @pytest.mark.anyio
    async def test_prefix_before_client_created_is_not_cached(self) -> None:
        adapter = self._adapter()
        # The async cluster creates its client on the first query, and logs 'Creating the client'
        # first, so this is the normal path; caching the prefix here would pin a truncated form
        # for the life of the cluster.
        assert adapter.log_prefix == f'[{TEST_CLUSTER_ID}]'
        await adapter.create_client()
        try:
            assert adapter.log_prefix == f'[{TEST_CLUSTER_ID}/{adapter.client_id}/http]'
        finally:
            await adapter.close_client()

    @pytest.mark.anyio
    async def test_prefix_reflects_secure_connection(self) -> None:
        adapter = self._adapter('https://localhost:8095')
        await adapter.create_client()
        try:
            assert adapter.log_prefix == f'[{TEST_CLUSTER_ID}/{adapter.client_id}/https]'
        finally:
            await adapter.close_client()


class LogPrefixTests(LogPrefixTestSuite):
    @pytest.fixture(scope='class', autouse=True)
    def validate_test_manifest(self) -> None:
        def valid_test_method(meth: str) -> bool:
            attr = getattr(LogPrefixTests, meth)
            return callable(attr) and not meth.startswith('__') and meth.startswith('test')

        method_list = [meth for meth in dir(LogPrefixTests) if valid_test_method(meth)]
        test_list = set(LogPrefixTestSuite.TEST_MANIFEST).symmetric_difference(method_list)
        if test_list:
            pytest.fail(f'Test manifest invalid.  Missing/extra tests: {test_list}.')
