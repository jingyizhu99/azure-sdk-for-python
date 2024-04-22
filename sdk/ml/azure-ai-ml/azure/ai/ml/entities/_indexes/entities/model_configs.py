# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from dataclasses import dataclass
from typing import Any, Dict, Optional
from azure.ai.ml._utils.utils import camel_to_snake
from azure.ai.ml.entities import WorkspaceConnection, AzureOpenAIWorkspaceConnection


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
    :param connection_name: The name of the workspace connection of this model.
    :type connection_name: str
    :param model_kwargs: Additional keyword arguments for the model.
    :type model_kwargs: Dict[str, Any]
    """
    api_base: str
    api_key: str
    api_version: Optional[str]
    connection_name: str
    model_name: str
    model_kwargs: Dict[str, Any]

    @staticmethod
    def from_connection(
        connection: WorkspaceConnection, model_name: str, **model_kwargs
    ) -> 'ModelConfiguration':
        """Create an model configuration from a Connection.
        
        :param connection: The Connection object.
        :type connection: ~azure.ai.ml.entities.WorkspaceConnection
        :param model_name: The name of the model.
        :type model_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param model_kwargs: Additional keyword arguments for the model.
        :type model_kwargs: Dict[str, Any]
        :return: The model configuration.
        :rtype: ~azure.ai.ml.entities._indexes.entities.ModelConfiguration
        :raises TypeError: If the connection is not an AzureOpenAIConnection.
        :raises ValueError: If the connection does not contain an OpenAI key.
        """
        if not isinstance(connection, AzureOpenAIWorkspaceConnection) or camel_to_snake(connection.type) != "azure_open_ai":
            raise TypeError(
                "Only AzureOpenAI connection objects are supported."
            )
        key = connection.credentials.get("key")
        if key is None:
            import os
            if "AZURE_OPENAI_API_KEY" in os.environ:
                key = os.getenv("AZURE_OPENAI_API_KEY")
            else:
                raise ValueError("Unable to retrieve openai key from connection object nor env variable.")

        return ModelConfiguration(
            api_base=connection.target,
            api_key=connection.credentials.key,
            api_version=connection.api_version,
            connection_name=connection.name,
            model_name=model_name,
            model_kwargs=model_kwargs,
        )