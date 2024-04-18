# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from dataclasses import dataclass
from typing import Any, Dict, Optional
from .connection_subtypes import AzureOpenAIConnection
from azure.ai.ml._utils.utils import camel_to_snake



@dataclass
class ModelConfiguration:
    """Configuration for a embedding model.
    
    :param api_base: The base URL for the API.
    :type api_base: str
    :param api_key: The API key.
    :type api_key: str
    :param api_version: The API version.
    :type api_version: Optional[str]
    :param model_name: The name of the model.
    :type model_name: str
    :param deployment_name: The name of the deployment.
    :type deployment_name: str
    :param model_kwargs: Additional keyword arguments for the model.
    :type model_kwargs: Dict[str, Any]
    """
    api_base: str
    api_key: str
    api_version: Optional[str]
    model_name: str
    deployment_name: str
    model_kwargs: Dict[str, Any]

    @staticmethod
    def from_connection(
        connection: AzureOpenAIConnection, model_name: str, deployment_name: str, **model_kwargs
    ) -> 'ModelConfiguration':
        """Create an model configuration from a Connection.
        
        :param connection: The Connection object.
        :type connection: ~azure.ai.resource.entities.AzureOpenAIConnection
        :param model_name: The name of the model.
        :type model_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param model_kwargs: Additional keyword arguments for the model.
        :type model_kwargs: Dict[str, Any]
        :return: The model configuration.
        :rtype: ~azure.ai.resource.entities.AzureOpenAIModelConfiguration
        :raises TypeError: If the connection is not an AzureOpenAIConnection.
        :raises ValueError: If the connection does not contain an OpenAI key.
        """
        if not isinstance(connection, AzureOpenAIConnection) or camel_to_snake(connection.type) != "azure_open_ai":
            raise TypeError(
                "Only AzureOpenAI connection objects are supported."
            )
        key = connection.credentials.get("key")
        if key is None:
            raise ValueError("Unable to retrieve openai key from connection object.")

        return ModelConfiguration(
            api_base=connection.target,
            api_key=connection.credentials.key,
            api_version=connection.api_version,
            model_name=model_name,
            deployment_name=deployment_name,
            model_kwargs=model_kwargs,
        )