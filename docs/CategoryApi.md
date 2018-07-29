# colormeshop.CategoryApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_categories**](CategoryApi.md#get_product_categories) | **GET** /v1/categories.json | 商品カテゴリー一覧を取得


# **get_product_categories**
> object get_product_categories()

商品カテゴリー一覧を取得

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
api_instance = colormeshop.CategoryApi(colormeshop.ApiClient(configuration))

try:
    # 商品カテゴリー一覧を取得
    api_response = api_instance.get_product_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->get_product_categories: %s\n" % e)
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

