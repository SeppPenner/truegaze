#
# Copyright (c) 2019 Nightwatch Cybersecurity.
#
# This file is part of truegaze
# (see https://github.com/nightwatchcybersecurity/truegaze).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from truegaze.plugins import ACTIVE_PLUGINS
from truegaze.plugins.base import BasePlugin
from truegaze.plugins.adobe_mobile_sdk import AdobeMobileSdkPlugin

# Tests for the package itself
class TestPluginsPackage(object):
    def test_active_plugins(self):
        assert len(ACTIVE_PLUGINS) == 2
        assert BasePlugin not in ACTIVE_PLUGINS
        assert AdobeMobileSdkPlugin in ACTIVE_PLUGINS
