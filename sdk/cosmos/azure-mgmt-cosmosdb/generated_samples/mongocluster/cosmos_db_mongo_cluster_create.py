# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.cosmosdb import CosmosDBManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cosmosdb
# USAGE
    python cosmos_db_mongo_cluster_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CosmosDBManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="ffffffff-ffff-ffff-ffff-ffffffffffff",
    )

    response = client.mongo_clusters.begin_create_or_update(
        resource_group_name="TestResourceGroup",
        mongo_cluster_name="myMongoCluster",
        parameters={
            "location": "westus2",
            "properties": {
                "administratorLogin": "mongoAdmin",
                "administratorLoginPassword": "password",
                "nodeGroupSpecs": [
                    {"diskSizeGB": 128, "enableHa": True, "kind": "Shard", "nodeCount": 3, "sku": "M30"}
                ],
                "serverVersion": "5.0",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cosmos-db/resource-manager/Microsoft.DocumentDB/preview/2023-11-15-preview/examples/mongo-cluster/CosmosDBMongoClusterCreate.json
if __name__ == "__main__":
    main()
