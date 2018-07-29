# colormeshop.CustomerApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer**](CustomerApi.md#get_customer) | **GET** /v1/customers/{customerId}.json | 顧客データの取得
[**get_customers**](CustomerApi.md#get_customers) | **GET** /v1/customers.json | 顧客データのリストを取得
[**post_customers**](CustomerApi.md#post_customers) | **POST** /v1/customers.json | 顧客データを追加


# **get_customer**
> object get_customer(customer_id)

顧客データの取得

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
api_instance = colormeshop.CustomerApi(colormeshop.ApiClient(configuration))
customer_id = 56 # int | 

try:
    # 顧客データの取得
    api_response = api_instance.get_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers**
> object get_customers(ids=ids, name=name, furigana=furigana, mail=mail, postal=postal, tel=tel, mobile=mobile, make_date_min=make_date_min, make_date_max=make_date_max, update_date_min=update_date_min, update_date_max=update_date_max)

顧客データのリストを取得

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
api_instance = colormeshop.CustomerApi(colormeshop.ApiClient(configuration))
ids = 'ids_example' # str | 顧客IDで検索。カンマ区切りで複数指定可能 (optional)
name = 'name_example' # str | 顧客名で部分一致検索 (optional)
furigana = 'furigana_example' # str | 顧客フリガナがで部分一致検索 (optional)
mail = 'mail_example' # str | 顧客メールアドレスで部分一致検索 (optional)
postal = 'postal_example' # str | 顧客の郵便番号で部分一致検索 (optional)
tel = 'tel_example' # str | 顧客の電話番号で部分一致検索 (optional)
mobile = True # bool | `true`なら会員登録済みの顧客から検索 (optional)
make_date_min = 'make_date_min_example' # str | 指定日時以降に登録された顧客から検索 (optional)
make_date_max = 'make_date_max_example' # str | 指定日時以前に登録された顧客から検索 (optional)
update_date_min = 'update_date_min_example' # str | 指定日時以降に更新された顧客から検索 (optional)
update_date_max = 'update_date_max_example' # str | 指定日時以降に更新された顧客から検索 (optional)

try:
    # 顧客データのリストを取得
    api_response = api_instance.get_customers(ids=ids, name=name, furigana=furigana, mail=mail, postal=postal, tel=tel, mobile=mobile, make_date_min=make_date_min, make_date_max=make_date_max, update_date_min=update_date_min, update_date_max=update_date_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| 顧客IDで検索。カンマ区切りで複数指定可能 | [optional] 
 **name** | **str**| 顧客名で部分一致検索 | [optional] 
 **furigana** | **str**| 顧客フリガナがで部分一致検索 | [optional] 
 **mail** | **str**| 顧客メールアドレスで部分一致検索 | [optional] 
 **postal** | **str**| 顧客の郵便番号で部分一致検索 | [optional] 
 **tel** | **str**| 顧客の電話番号で部分一致検索 | [optional] 
 **mobile** | **bool**| &#x60;true&#x60;なら会員登録済みの顧客から検索 | [optional] 
 **make_date_min** | **str**| 指定日時以降に登録された顧客から検索 | [optional] 
 **make_date_max** | **str**| 指定日時以前に登録された顧客から検索 | [optional] 
 **update_date_min** | **str**| 指定日時以降に更新された顧客から検索 | [optional] 
 **update_date_max** | **str**| 指定日時以降に更新された顧客から検索 | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customers**
> object post_customers(unknown_base_type)

顧客データを追加

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
api_instance = colormeshop.CustomerApi(colormeshop.ApiClient(configuration))
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object | 

try:
    # 顧客データを追加
    api_response = api_instance.post_customers(unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->post_customers: %s\n" % e)
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

