# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_extended_resource_request(
    resource_group_name: str,
    resource_namespace: str,
    resource_type: str,
    resource_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Security/adaptiveNetworkHardenings",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "resourceNamespace": _SERIALIZER.url("resource_namespace", resource_namespace, "str"),
        "resourceType": _SERIALIZER.url("resource_type", resource_type, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str,
    resource_namespace: str,
    resource_type: str,
    resource_name: str,
    adaptive_network_hardening_resource_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Security/adaptiveNetworkHardenings/{adaptiveNetworkHardeningResourceName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "resourceNamespace": _SERIALIZER.url("resource_namespace", resource_namespace, "str"),
        "resourceType": _SERIALIZER.url("resource_type", resource_type, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "adaptiveNetworkHardeningResourceName": _SERIALIZER.url(
            "adaptive_network_hardening_resource_name", adaptive_network_hardening_resource_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_enforce_request(
    resource_group_name: str,
    resource_namespace: str,
    resource_type: str,
    resource_name: str,
    adaptive_network_hardening_resource_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    adaptive_network_hardening_enforce_action: Literal["enforce"] = kwargs.pop(
        "adaptive_network_hardening_enforce_action", "enforce"
    )
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Security/adaptiveNetworkHardenings/{adaptiveNetworkHardeningResourceName}/{adaptiveNetworkHardeningEnforceAction}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "resourceNamespace": _SERIALIZER.url("resource_namespace", resource_namespace, "str"),
        "resourceType": _SERIALIZER.url("resource_type", resource_type, "str"),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "adaptiveNetworkHardeningResourceName": _SERIALIZER.url(
            "adaptive_network_hardening_resource_name", adaptive_network_hardening_resource_name, "str"
        ),
        "adaptiveNetworkHardeningEnforceAction": _SERIALIZER.url(
            "adaptive_network_hardening_enforce_action", adaptive_network_hardening_enforce_action, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class AdaptiveNetworkHardeningsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2020_01_01.SecurityCenter`'s
        :attr:`adaptive_network_hardenings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list_by_extended_resource(
        self, resource_group_name: str, resource_namespace: str, resource_type: str, resource_name: str, **kwargs: Any
    ) -> Iterable["_models.AdaptiveNetworkHardening"]:
        """Gets a list of Adaptive Network Hardenings resources in scope of an extended resource.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param resource_namespace: The Namespace of the resource. Required.
        :type resource_namespace: str
        :param resource_type: The type of the resource. Required.
        :type resource_type: str
        :param resource_name: Name of the resource. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AdaptiveNetworkHardening or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.security.v2020_01_01.models.AdaptiveNetworkHardening]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        cls: ClsType[_models.AdaptiveNetworkHardeningsList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_extended_resource_request(
                    resource_group_name=resource_group_name,
                    resource_namespace=resource_namespace,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_extended_resource.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AdaptiveNetworkHardeningsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_extended_resource.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Security/adaptiveNetworkHardenings"
    }

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        resource_namespace: str,
        resource_type: str,
        resource_name: str,
        adaptive_network_hardening_resource_name: str,
        **kwargs: Any
    ) -> _models.AdaptiveNetworkHardening:
        """Gets a single Adaptive Network Hardening resource.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param resource_namespace: The Namespace of the resource. Required.
        :type resource_namespace: str
        :param resource_type: The type of the resource. Required.
        :type resource_type: str
        :param resource_name: Name of the resource. Required.
        :type resource_name: str
        :param adaptive_network_hardening_resource_name: The name of the Adaptive Network Hardening
         resource. Required.
        :type adaptive_network_hardening_resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdaptiveNetworkHardening or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.AdaptiveNetworkHardening
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        cls: ClsType[_models.AdaptiveNetworkHardening] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_namespace=resource_namespace,
            resource_type=resource_type,
            resource_name=resource_name,
            adaptive_network_hardening_resource_name=adaptive_network_hardening_resource_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdaptiveNetworkHardening", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Security/adaptiveNetworkHardenings/{adaptiveNetworkHardeningResourceName}"
    }

    def _enforce_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        resource_namespace: str,
        resource_type: str,
        resource_name: str,
        adaptive_network_hardening_resource_name: str,
        body: Union[_models.AdaptiveNetworkHardeningEnforceRequest, IO],
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        adaptive_network_hardening_enforce_action: Literal["enforce"] = kwargs.pop(
            "adaptive_network_hardening_enforce_action", "enforce"
        )
        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "AdaptiveNetworkHardeningEnforceRequest")

        request = build_enforce_request(
            resource_group_name=resource_group_name,
            resource_namespace=resource_namespace,
            resource_type=resource_type,
            resource_name=resource_name,
            adaptive_network_hardening_resource_name=adaptive_network_hardening_resource_name,
            subscription_id=self._config.subscription_id,
            adaptive_network_hardening_enforce_action=adaptive_network_hardening_enforce_action,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._enforce_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _enforce_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Security/adaptiveNetworkHardenings/{adaptiveNetworkHardeningResourceName}/{adaptiveNetworkHardeningEnforceAction}"
    }

    @overload
    def begin_enforce(
        self,
        resource_group_name: str,
        resource_namespace: str,
        resource_type: str,
        resource_name: str,
        adaptive_network_hardening_resource_name: str,
        body: _models.AdaptiveNetworkHardeningEnforceRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[None]:
        """Enforces the given rules on the NSG(s) listed in the request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param resource_namespace: The Namespace of the resource. Required.
        :type resource_namespace: str
        :param resource_type: The type of the resource. Required.
        :type resource_type: str
        :param resource_name: Name of the resource. Required.
        :type resource_name: str
        :param adaptive_network_hardening_resource_name: The name of the Adaptive Network Hardening
         resource. Required.
        :type adaptive_network_hardening_resource_name: str
        :param body: Required.
        :type body: ~azure.mgmt.security.v2020_01_01.models.AdaptiveNetworkHardeningEnforceRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword adaptive_network_hardening_enforce_action: Enforces the given rules on the NSG(s)
         listed in the request. Default value is "enforce". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype adaptive_network_hardening_enforce_action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_enforce(
        self,
        resource_group_name: str,
        resource_namespace: str,
        resource_type: str,
        resource_name: str,
        adaptive_network_hardening_resource_name: str,
        body: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[None]:
        """Enforces the given rules on the NSG(s) listed in the request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param resource_namespace: The Namespace of the resource. Required.
        :type resource_namespace: str
        :param resource_type: The type of the resource. Required.
        :type resource_type: str
        :param resource_name: Name of the resource. Required.
        :type resource_name: str
        :param adaptive_network_hardening_resource_name: The name of the Adaptive Network Hardening
         resource. Required.
        :type adaptive_network_hardening_resource_name: str
        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword adaptive_network_hardening_enforce_action: Enforces the given rules on the NSG(s)
         listed in the request. Default value is "enforce". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype adaptive_network_hardening_enforce_action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_enforce(
        self,
        resource_group_name: str,
        resource_namespace: str,
        resource_type: str,
        resource_name: str,
        adaptive_network_hardening_resource_name: str,
        body: Union[_models.AdaptiveNetworkHardeningEnforceRequest, IO],
        **kwargs: Any
    ) -> LROPoller[None]:
        """Enforces the given rules on the NSG(s) listed in the request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param resource_namespace: The Namespace of the resource. Required.
        :type resource_namespace: str
        :param resource_type: The type of the resource. Required.
        :type resource_type: str
        :param resource_name: Name of the resource. Required.
        :type resource_name: str
        :param adaptive_network_hardening_resource_name: The name of the Adaptive Network Hardening
         resource. Required.
        :type adaptive_network_hardening_resource_name: str
        :param body: Is either a AdaptiveNetworkHardeningEnforceRequest type or a IO type. Required.
        :type body: ~azure.mgmt.security.v2020_01_01.models.AdaptiveNetworkHardeningEnforceRequest or
         IO
        :keyword adaptive_network_hardening_enforce_action: Enforces the given rules on the NSG(s)
         listed in the request. Default value is "enforce". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype adaptive_network_hardening_enforce_action: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        adaptive_network_hardening_enforce_action: Literal["enforce"] = kwargs.pop(
            "adaptive_network_hardening_enforce_action", "enforce"
        )
        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._enforce_initial(  # type: ignore
                resource_group_name=resource_group_name,
                resource_namespace=resource_namespace,
                resource_type=resource_type,
                resource_name=resource_name,
                adaptive_network_hardening_resource_name=adaptive_network_hardening_resource_name,
                body=body,
                adaptive_network_hardening_enforce_action=adaptive_network_hardening_enforce_action,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: PollingMethod = cast(PollingMethod, ARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_enforce.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Security/adaptiveNetworkHardenings/{adaptiveNetworkHardeningResourceName}/{adaptiveNetworkHardeningEnforceAction}"
    }
