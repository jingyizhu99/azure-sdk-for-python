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
    python cosmos_db_sql_client_encryption_key_create_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CosmosDBManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subId",
    )

    response = client.sql_resources.begin_create_update_client_encryption_key(
        resource_group_name="rgName",
        account_name="accountName",
        database_name="databaseName",
        client_encryption_key_name="cekName",
        create_update_client_encryption_key_parameters={
            "properties": {
                "resource": {
                    "encryptionAlgorithm": "AEAD_AES_256_CBC_HMAC_SHA256",
                    "id": "cekName",
                    "keyWrapMetadata": {
                        "algorithm": "RSA-OAEP",
                        "name": "customerManagedKey",
                        "type": "AzureKeyVault",
                        "value": "AzureKeyVault Key URL",
                    },
                    "wrappedDataEncryptionKey": "VGhpcyBpcyBhY3R1YWxseSBhbiBhcnJheSBvZiBieXRlcy4gVGhpcyByZXF1ZXN0L3Jlc3BvbnNlIGlzIGJlaW5nIHByZXNlbnRlZCBhcyBhIHN0cmluZyBmb3IgcmVhZGFiaWxpdHkgaW4gdGhlIGV4YW1wbGU=",
                }
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cosmos-db/resource-manager/Microsoft.DocumentDB/preview/2023-11-15-preview/examples/CosmosDBSqlClientEncryptionKeyCreateUpdate.json
if __name__ == "__main__":
    main()
