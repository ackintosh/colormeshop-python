# colormeshop.ScriptApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_script_tag**](ScriptApi.md#create_script_tag) | **POST** /v1/script_tags.json | スクリプトタグの作成
[**delete_script_tag**](ScriptApi.md#delete_script_tag) | **DELETE** /v1/script_tags/{scriptTagId}.json | スクリプトタグの削除
[**get_script_tag**](ScriptApi.md#get_script_tag) | **GET** /v1/script_tags/{scriptTagId}.json | スクリプトタグの取得
[**get_script_tags**](ScriptApi.md#get_script_tags) | **GET** /v1/script_tags.json | スクリプトタグの取得
[**update_script_tag**](ScriptApi.md#update_script_tag) | **PUT** /v1/script_tags/{scriptTagId}.json | スクリプトタグの更新


# **create_script_tag**
> object create_script_tag(unknown_base_type)

スクリプトタグの作成

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
api_instance = colormeshop.ScriptApi(colormeshop.ApiClient(configuration))
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object | 作成するスクリプトタグの情報

try:
    # スクリプトタグの作成
    api_response = api_instance.create_script_tag(unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->create_script_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)| 作成するスクリプトタグの情報 | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_script_tag**
> delete_script_tag(script_tag_id)

スクリプトタグの削除

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
api_instance = colormeshop.ScriptApi(colormeshop.ApiClient(configuration))
script_tag_id = 56 # int | 

try:
    # スクリプトタグの削除
    api_instance.delete_script_tag(script_tag_id)
except ApiException as e:
    print("Exception when calling ScriptApi->delete_script_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_tag_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_script_tag**
> object get_script_tag(script_tag_id)

スクリプトタグの取得

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
api_instance = colormeshop.ScriptApi(colormeshop.ApiClient(configuration))
script_tag_id = 56 # int | 

try:
    # スクリプトタグの取得
    api_response = api_instance.get_script_tag(script_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->get_script_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_tag_id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_script_tags**
> object get_script_tags()

スクリプトタグの取得

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
api_instance = colormeshop.ScriptApi(colormeshop.ApiClient(configuration))

try:
    # スクリプトタグの取得
    api_response = api_instance.get_script_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->get_script_tags: %s\n" % e)
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

# **update_script_tag**
> object update_script_tag(script_tag_id, unknown_base_type)

スクリプトタグの更新

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
api_instance = colormeshop.ScriptApi(colormeshop.ApiClient(configuration))
script_tag_id = 56 # int | 
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object | 作成するスクリプトタグの情報

try:
    # スクリプトタグの更新
    api_response = api_instance.update_script_tag(script_tag_id, unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptApi->update_script_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_tag_id** | **int**|  | 
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)| 作成するスクリプトタグの情報 | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

