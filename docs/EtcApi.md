# colormeshop.EtcApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device_token**](EtcApi.md#delete_device_token) | **DELETE** /v1/device_tokens/{token}.json | デバイストークンの削除


# **delete_device_token**
> delete_device_token(token)

デバイストークンの削除

### Example
```python
from __future__ import print_function
import time
import colormeshop
from colormeshop.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = colormeshop.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = colormeshop.EtcApi(colormeshop.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # デバイストークンの削除
    api_instance.delete_device_token(token)
except ApiException as e:
    print("Exception when calling EtcApi->delete_device_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

