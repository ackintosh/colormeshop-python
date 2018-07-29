# colormeshop.ChargeApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_application_charge**](ChargeApi.md#activate_application_charge) | **POST** /v1/application_charges/{applicationChargeId}/activate.json | スポット課金データをアクティベートする
[**get_application_charge**](ChargeApi.md#get_application_charge) | **GET** /v1/application_charges/{applicationChargeId}.json | スポット課金データの取得
[**get_application_charges**](ChargeApi.md#get_application_charges) | **GET** /v1/application_charges.json | スポット課金一覧の取得
[**post_application_charge**](ChargeApi.md#post_application_charge) | **POST** /v1/application_charges.json | スポット課金データの作成


# **activate_application_charge**
> object activate_application_charge(application_charge_id)

スポット課金データをアクティベートする

スポット課金データをアクティベートするAPIです。

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
api_instance = colormeshop.ChargeApi(colormeshop.ApiClient(configuration))
application_charge_id = 56 # int | 

try:
    # スポット課金データをアクティベートする
    api_response = api_instance.activate_application_charge(application_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeApi->activate_application_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_charge_id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_charge**
> object get_application_charge(application_charge_id)

スポット課金データの取得

スポット課金データを取得するAPIです。

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
api_instance = colormeshop.ChargeApi(colormeshop.ApiClient(configuration))
application_charge_id = 56 # int | 

try:
    # スポット課金データの取得
    api_response = api_instance.get_application_charge(application_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeApi->get_application_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_charge_id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_charges**
> object get_application_charges(limit=limit, since_id=since_id)

スポット課金一覧の取得

スポット課金一覧を取得するAPIです。

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
api_instance = colormeshop.ChargeApi(colormeshop.ApiClient(configuration))
limit = 56 # int | レスポンスの件数を指定します。指定がない場合は10件。最大50件。 (optional)
since_id = 56 # int | 指定した課金ID以降のデータを返します。 (optional)

try:
    # スポット課金一覧の取得
    api_response = api_instance.get_application_charges(limit=limit, since_id=since_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeApi->get_application_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| レスポンスの件数を指定します。指定がない場合は10件。最大50件。 | [optional] 
 **since_id** | **int**| 指定した課金ID以降のデータを返します。 | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_application_charge**
> object post_application_charge(unknown_base_type)

スポット課金データの作成

スポット課金データを作成するAPIです。

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
api_instance = colormeshop.ChargeApi(colormeshop.ApiClient(configuration))
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object | 

try:
    # スポット課金データの作成
    api_response = api_instance.post_application_charge(unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeApi->post_application_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

