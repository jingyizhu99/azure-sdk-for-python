# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import AzureMachineLearningWorkspacesConfiguration
from .operations import (
    BatchDeploymentsOperations,
    BatchEndpointsOperations,
    CodeContainersOperations,
    CodeVersionsOperations,
    ComponentContainersOperations,
    ComponentVersionsOperations,
    ComputeOperations,
    DataContainersOperations,
    DataVersionsOperations,
    DatastoresOperations,
    EnvironmentContainersOperations,
    EnvironmentVersionsOperations,
    FeaturesetContainersOperations,
    FeaturesetVersionsOperations,
    FeaturestoreEntityContainersOperations,
    FeaturestoreEntityVersionsOperations,
    JobsOperations,
    LabelingJobsOperations,
    ModelContainersOperations,
    ModelVersionsOperations,
    OnlineDeploymentsOperations,
    OnlineEndpointsOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    QuotasOperations,
    RegistriesOperations,
    RegistryCodeContainersOperations,
    RegistryCodeVersionsOperations,
    RegistryComponentContainersOperations,
    RegistryComponentVersionsOperations,
    RegistryDataContainersOperations,
    RegistryDataVersionsOperations,
    RegistryEnvironmentContainersOperations,
    RegistryEnvironmentVersionsOperations,
    RegistryModelContainersOperations,
    RegistryModelVersionsOperations,
    SchedulesOperations,
    UsagesOperations,
    VirtualMachineSizesOperations,
    WorkspaceConnectionsOperations,
    WorkspaceFeaturesOperations,
    WorkspacesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest, HttpResponse


class AzureMachineLearningWorkspaces(object):  # pylint: disable=too-many-instance-attributes
    """These APIs allow end users to operate on Azure Machine Learning Workspace resources.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.machinelearningservices.operations.Operations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.machinelearningservices.operations.WorkspacesOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.machinelearningservices.operations.UsagesOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes:
     azure.mgmt.machinelearningservices.operations.VirtualMachineSizesOperations
    :ivar quotas: QuotasOperations operations
    :vartype quotas: azure.mgmt.machinelearningservices.operations.QuotasOperations
    :ivar compute: ComputeOperations operations
    :vartype compute: azure.mgmt.machinelearningservices.operations.ComputeOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.machinelearningservices.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.machinelearningservices.operations.PrivateLinkResourcesOperations
    :ivar workspace_connections: WorkspaceConnectionsOperations operations
    :vartype workspace_connections:
     azure.mgmt.machinelearningservices.operations.WorkspaceConnectionsOperations
    :ivar registries: RegistriesOperations operations
    :vartype registries: azure.mgmt.machinelearningservices.operations.RegistriesOperations
    :ivar workspace_features: WorkspaceFeaturesOperations operations
    :vartype workspace_features:
     azure.mgmt.machinelearningservices.operations.WorkspaceFeaturesOperations
    :ivar registry_code_containers: RegistryCodeContainersOperations operations
    :vartype registry_code_containers:
     azure.mgmt.machinelearningservices.operations.RegistryCodeContainersOperations
    :ivar registry_code_versions: RegistryCodeVersionsOperations operations
    :vartype registry_code_versions:
     azure.mgmt.machinelearningservices.operations.RegistryCodeVersionsOperations
    :ivar registry_component_containers: RegistryComponentContainersOperations operations
    :vartype registry_component_containers:
     azure.mgmt.machinelearningservices.operations.RegistryComponentContainersOperations
    :ivar registry_component_versions: RegistryComponentVersionsOperations operations
    :vartype registry_component_versions:
     azure.mgmt.machinelearningservices.operations.RegistryComponentVersionsOperations
    :ivar registry_data_containers: RegistryDataContainersOperations operations
    :vartype registry_data_containers:
     azure.mgmt.machinelearningservices.operations.RegistryDataContainersOperations
    :ivar registry_data_versions: RegistryDataVersionsOperations operations
    :vartype registry_data_versions:
     azure.mgmt.machinelearningservices.operations.RegistryDataVersionsOperations
    :ivar registry_environment_containers: RegistryEnvironmentContainersOperations operations
    :vartype registry_environment_containers:
     azure.mgmt.machinelearningservices.operations.RegistryEnvironmentContainersOperations
    :ivar registry_environment_versions: RegistryEnvironmentVersionsOperations operations
    :vartype registry_environment_versions:
     azure.mgmt.machinelearningservices.operations.RegistryEnvironmentVersionsOperations
    :ivar registry_model_containers: RegistryModelContainersOperations operations
    :vartype registry_model_containers:
     azure.mgmt.machinelearningservices.operations.RegistryModelContainersOperations
    :ivar registry_model_versions: RegistryModelVersionsOperations operations
    :vartype registry_model_versions:
     azure.mgmt.machinelearningservices.operations.RegistryModelVersionsOperations
    :ivar batch_endpoints: BatchEndpointsOperations operations
    :vartype batch_endpoints:
     azure.mgmt.machinelearningservices.operations.BatchEndpointsOperations
    :ivar batch_deployments: BatchDeploymentsOperations operations
    :vartype batch_deployments:
     azure.mgmt.machinelearningservices.operations.BatchDeploymentsOperations
    :ivar code_containers: CodeContainersOperations operations
    :vartype code_containers:
     azure.mgmt.machinelearningservices.operations.CodeContainersOperations
    :ivar code_versions: CodeVersionsOperations operations
    :vartype code_versions: azure.mgmt.machinelearningservices.operations.CodeVersionsOperations
    :ivar component_containers: ComponentContainersOperations operations
    :vartype component_containers:
     azure.mgmt.machinelearningservices.operations.ComponentContainersOperations
    :ivar component_versions: ComponentVersionsOperations operations
    :vartype component_versions:
     azure.mgmt.machinelearningservices.operations.ComponentVersionsOperations
    :ivar data_containers: DataContainersOperations operations
    :vartype data_containers:
     azure.mgmt.machinelearningservices.operations.DataContainersOperations
    :ivar data_versions: DataVersionsOperations operations
    :vartype data_versions: azure.mgmt.machinelearningservices.operations.DataVersionsOperations
    :ivar datastores: DatastoresOperations operations
    :vartype datastores: azure.mgmt.machinelearningservices.operations.DatastoresOperations
    :ivar environment_containers: EnvironmentContainersOperations operations
    :vartype environment_containers:
     azure.mgmt.machinelearningservices.operations.EnvironmentContainersOperations
    :ivar environment_versions: EnvironmentVersionsOperations operations
    :vartype environment_versions:
     azure.mgmt.machinelearningservices.operations.EnvironmentVersionsOperations
    :ivar featureset_containers: FeaturesetContainersOperations operations
    :vartype featureset_containers:
     azure.mgmt.machinelearningservices.operations.FeaturesetContainersOperations
    :ivar featureset_versions: FeaturesetVersionsOperations operations
    :vartype featureset_versions:
     azure.mgmt.machinelearningservices.operations.FeaturesetVersionsOperations
    :ivar featurestore_entity_containers: FeaturestoreEntityContainersOperations operations
    :vartype featurestore_entity_containers:
     azure.mgmt.machinelearningservices.operations.FeaturestoreEntityContainersOperations
    :ivar featurestore_entity_versions: FeaturestoreEntityVersionsOperations operations
    :vartype featurestore_entity_versions:
     azure.mgmt.machinelearningservices.operations.FeaturestoreEntityVersionsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.mgmt.machinelearningservices.operations.JobsOperations
    :ivar labeling_jobs: LabelingJobsOperations operations
    :vartype labeling_jobs: azure.mgmt.machinelearningservices.operations.LabelingJobsOperations
    :ivar model_containers: ModelContainersOperations operations
    :vartype model_containers:
     azure.mgmt.machinelearningservices.operations.ModelContainersOperations
    :ivar model_versions: ModelVersionsOperations operations
    :vartype model_versions: azure.mgmt.machinelearningservices.operations.ModelVersionsOperations
    :ivar online_endpoints: OnlineEndpointsOperations operations
    :vartype online_endpoints:
     azure.mgmt.machinelearningservices.operations.OnlineEndpointsOperations
    :ivar online_deployments: OnlineDeploymentsOperations operations
    :vartype online_deployments:
     azure.mgmt.machinelearningservices.operations.OnlineDeploymentsOperations
    :ivar schedules: SchedulesOperations operations
    :vartype schedules: azure.mgmt.machinelearningservices.operations.SchedulesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword api_version: Api Version. The default value is "2023-02-01-preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url="https://management.azure.com",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self._config = AzureMachineLearningWorkspacesConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.quotas = QuotasOperations(self._client, self._config, self._serialize, self._deserialize)
        self.compute = ComputeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.workspace_connections = WorkspaceConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registries = RegistriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace_features = WorkspaceFeaturesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_code_containers = RegistryCodeContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_code_versions = RegistryCodeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_component_containers = RegistryComponentContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_component_versions = RegistryComponentVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_data_containers = RegistryDataContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_data_versions = RegistryDataVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_environment_containers = RegistryEnvironmentContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_environment_versions = RegistryEnvironmentVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_model_containers = RegistryModelContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registry_model_versions = RegistryModelVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.batch_endpoints = BatchEndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.batch_deployments = BatchDeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.code_containers = CodeContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.code_versions = CodeVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.component_containers = ComponentContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.component_versions = ComponentVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_containers = DataContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_versions = DataVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datastores = DatastoresOperations(self._client, self._config, self._serialize, self._deserialize)
        self.environment_containers = EnvironmentContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.environment_versions = EnvironmentVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.featureset_containers = FeaturesetContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.featureset_versions = FeaturesetVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.featurestore_entity_containers = FeaturestoreEntityContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.featurestore_entity_versions = FeaturestoreEntityVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.jobs = JobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.labeling_jobs = LabelingJobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.model_containers = ModelContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.model_versions = ModelVersionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.online_endpoints = OnlineEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.online_deployments = OnlineDeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.schedules = SchedulesOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureMachineLearningWorkspaces
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
