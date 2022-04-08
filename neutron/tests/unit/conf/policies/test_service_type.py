# Copyright (c) 2021 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from neutron import policy
from neutron.tests.unit.conf.policies import test_base as base


class ServiceTypeAPITestCase(base.PolicyBaseTestCase):

    def setUp(self):
        super(ServiceTypeAPITestCase, self).setUp()
        self.target = {}


class SystemAdminTests(ServiceTypeAPITestCase):

    def setUp(self):
        super(SystemAdminTests, self).setUp()
        self.context = self.system_admin_ctx

    def test_get_service_provider(self):
        self.assertTrue(
            policy.enforce(self.context, 'get_service_provider', self.target))


class SystemMemberTests(SystemAdminTests):

    def setUp(self):
        self.skipTest("SYSTEM_MEMBER persona isn't supported in phase1 of the "
                      "community goal")
        super(SystemMemberTests, self).setUp()
        self.context = self.system_member_ctx


class SystemReaderTests(SystemMemberTests):

    def setUp(self):
        self.skipTest("SYSTEM_READER persona isn't supported in phase1 of the "
                      "community goal")
        super(SystemReaderTests, self).setUp()
        self.context = self.system_reader_ctx


class ProjectAdminTests(ServiceTypeAPITestCase):

    def setUp(self):
        super(ProjectAdminTests, self).setUp()
        self.context = self.project_admin_ctx

    def test_get_service_provider(self):
        self.assertTrue(
            policy.enforce(self.context, 'get_service_provider', self.target))


class ProjectMemberTests(ProjectAdminTests):

    def setUp(self):
        super(ProjectMemberTests, self).setUp()
        self.context = self.project_member_ctx


class ProjectReaderTests(ProjectMemberTests):

    def setUp(self):
        super(ProjectReaderTests, self).setUp()
        self.context = self.project_reader_ctx
