# colormeshop.GiftApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gift**](GiftApi.md#get_gift) | **GET** /v1/gift.json | ギフト設定を取得


# **get_gift**
> object get_gift()

ギフト設定を取得

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
api_instance = colormeshop.GiftApi(colormeshop.ApiClient(configuration))

try:
    # ギフト設定を取得
    api_response = api_instance.get_gift()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftApi->get_gift: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

