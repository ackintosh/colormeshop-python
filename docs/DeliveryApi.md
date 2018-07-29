# colormeshop.DeliveryApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deliveries**](DeliveryApi.md#get_deliveries) | **GET** /v1/deliveries.json | 配送方法一覧を取得
[**get_delivery_date_setting**](DeliveryApi.md#get_delivery_date_setting) | **GET** /v1/deliveries/date.json | 配送日時設定を取得


# **get_deliveries**
> object get_deliveries()

配送方法一覧を取得

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
api_instance = colormeshop.DeliveryApi(colormeshop.ApiClient(configuration))

try:
    # 配送方法一覧を取得
    api_response = api_instance.get_deliveries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->get_deliveries: %s\n" % e)
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

# **get_delivery_date_setting**
> object get_delivery_date_setting()

配送日時設定を取得

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
api_instance = colormeshop.DeliveryApi(colormeshop.ApiClient(configuration))

try:
    # 配送日時設定を取得
    api_response = api_instance.get_delivery_date_setting()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeliveryApi->get_delivery_date_setting: %s\n" % e)
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

