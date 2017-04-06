﻿# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import unittest

import azure.mgmt.resource.features.models
from testutils.common_recordingtestcase import record
from tests.mgmt_testcase import HttpStatusCode, AzureMgmtTestCase


class MgmtResourceFeaturesTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtResourceFeaturesTest, self).setUp()
        self.features_client = self.create_mgmt_client(
            azure.mgmt.resource.FeatureClient
        )

    @record
    def test_features(self):
        features = list(self.features_client.features.list_all())
        self.assertGreater(len(features), 0)
        self.assertTrue(all(isinstance(v, azure.mgmt.resource.features.models.FeatureResult) for v in features))


        features = list(self.features_client.features.list('Microsoft.Compute'))
        self.assertGreater(len(features), 0)
        self.assertTrue(all(isinstance(v, azure.mgmt.resource.features.models.FeatureResult) for v in features))

        one_feature = features[0]
        feature = self.features_client.features.get(
            'Microsoft.Compute',
            one_feature.name.split('/')[1]
        )

        self.features_client.features.register(
            'Microsoft.Compute',
            feature.name.split('/')[1]
        )


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
