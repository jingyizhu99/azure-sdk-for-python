# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.datafactory import DataFactoryManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-datafactory
# USAGE
    python pipeline_runs_cancel.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataFactoryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="12345678-1234-1234-1234-12345678abc",
    )

    client.pipeline_runs.cancel(
        resource_group_name="exampleResourceGroup",
        factory_name="exampleFactoryName",
        run_id="16ac5348-ff82-4f95-a80d-638c1d47b721",
    )


# x-ms-original-file: specification/datafactory/resource-manager/Microsoft.DataFactory/stable/2018-06-01/examples/PipelineRuns_Cancel.json
if __name__ == "__main__":
    main()
