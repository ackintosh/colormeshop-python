# colormeshop.ProductApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_pickup**](ProductApi.md#delete_product_pickup) | **DELETE** /v1/products/{productId}/pickups/{pickupType}.json | おすすめ商品情報の削除
[**get_product**](ProductApi.md#get_product) | **GET** /v1/products/{productId}.json | 商品データの取得
[**get_products**](ProductApi.md#get_products) | **GET** /v1/products.json | 商品一覧の取得
[**post_product_pickup**](ProductApi.md#post_product_pickup) | **POST** /v1/products/{productId}/pickups.json | おすすめ商品情報の追加
[**update_product**](ProductApi.md#update_product) | **PUT** /v1/products/{productId}.json | 商品データの更新


# **delete_product_pickup**
> object delete_product_pickup(product_id, pickup_type)

おすすめ商品情報の削除

商品に付加されたおすすめ商品情報を削除します

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
api_instance = colormeshop.ProductApi(colormeshop.ApiClient(configuration))
product_id = 56 # int | 商品ID
pickup_type = 56 # int | おすすめ商品情報種別（0:おすすめ商品, 1:売れ筋商品, 3:新着商品, 4:イチオシ商品）

try:
    # おすすめ商品情報の削除
    api_response = api_instance.delete_product_pickup(product_id, pickup_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->delete_product_pickup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| 商品ID | 
 **pickup_type** | **int**| おすすめ商品情報種別（0:おすすめ商品, 1:売れ筋商品, 3:新着商品, 4:イチオシ商品） | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> object get_product(product_id)

商品データの取得

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
api_instance = colormeshop.ProductApi(colormeshop.ApiClient(configuration))
product_id = 56 # int | 商品ID

try:
    # 商品データの取得
    api_response = api_instance.get_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| 商品ID | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> object get_products(ids=ids, category_id_big=category_id_big, category_id_small=category_id_small, model_number=model_number, name=name, display_state=display_state, stocks=stocks, stock_managed=stock_managed, recent_zero_stocks=recent_zero_stocks, make_date_min=make_date_min, make_date_max=make_date_max, update_date_min=update_date_min, update_date_max=update_date_max, fields=fields, limit=limit, offset=offset)

商品一覧の取得

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
api_instance = colormeshop.ProductApi(colormeshop.ApiClient(configuration))
ids = 'ids_example' # str | 商品IDで検索。カンマ区切りにすることで複数検索が可能 (optional)
category_id_big = 56 # int | 大カテゴリーIDで検索 (optional)
category_id_small = 56 # int | 小カテゴリーIDで検索 (optional)
model_number = 'model_number_example' # str | 型番で部分一致検索 (optional)
name = 'name_example' # str | 商品名で部分一致検索 (optional)
display_state = 'display_state_example' # str | 掲載設定で検索 (optional)
stocks = 56 # int | 在庫管理している商品のうち、在庫数が指定した数値以下の商品を検索。オプションごとに在庫管理している商品は、合計在庫数で検索される (optional)
stock_managed = True # bool | 在庫管理している、またはしていない商品から検索 (optional)
recent_zero_stocks = True # bool | `true` の場合、過去1週間以内に更新された商品から検索 (optional)
make_date_min = 'make_date_min_example' # str | 指定日時以降に作成された商品から検索 (optional)
make_date_max = 'make_date_max_example' # str | 指定日時以前に作成された商品から検索 (optional)
update_date_min = 'update_date_min_example' # str | 指定日時以降に更新された商品から検索 (optional)
update_date_max = 'update_date_max_example' # str | 指定日時以降に更新された商品から検索 (optional)
fields = 'fields_example' # str | レスポンスJSONのキーをカンマ区切りで指定 (optional)
limit = 56 # int | レスポンスの件数を指定。指定がない場合は10。最大50 (optional)
offset = 56 # int | 指定した数値+1件目以降のデータを返す (optional)

try:
    # 商品一覧の取得
    api_response = api_instance.get_products(ids=ids, category_id_big=category_id_big, category_id_small=category_id_small, model_number=model_number, name=name, display_state=display_state, stocks=stocks, stock_managed=stock_managed, recent_zero_stocks=recent_zero_stocks, make_date_min=make_date_min, make_date_max=make_date_max, update_date_min=update_date_min, update_date_max=update_date_max, fields=fields, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| 商品IDで検索。カンマ区切りにすることで複数検索が可能 | [optional] 
 **category_id_big** | **int**| 大カテゴリーIDで検索 | [optional] 
 **category_id_small** | **int**| 小カテゴリーIDで検索 | [optional] 
 **model_number** | **str**| 型番で部分一致検索 | [optional] 
 **name** | **str**| 商品名で部分一致検索 | [optional] 
 **display_state** | **str**| 掲載設定で検索 | [optional] 
 **stocks** | **int**| 在庫管理している商品のうち、在庫数が指定した数値以下の商品を検索。オプションごとに在庫管理している商品は、合計在庫数で検索される | [optional] 
 **stock_managed** | **bool**| 在庫管理している、またはしていない商品から検索 | [optional] 
 **recent_zero_stocks** | **bool**| &#x60;true&#x60; の場合、過去1週間以内に更新された商品から検索 | [optional] 
 **make_date_min** | **str**| 指定日時以降に作成された商品から検索 | [optional] 
 **make_date_max** | **str**| 指定日時以前に作成された商品から検索 | [optional] 
 **update_date_min** | **str**| 指定日時以降に更新された商品から検索 | [optional] 
 **update_date_max** | **str**| 指定日時以降に更新された商品から検索 | [optional] 
 **fields** | **str**| レスポンスJSONのキーをカンマ区切りで指定 | [optional] 
 **limit** | **int**| レスポンスの件数を指定。指定がない場合は10。最大50 | [optional] 
 **offset** | **int**| 指定した数値+1件目以降のデータを返す | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_product_pickup**
> object post_product_pickup(product_id, unknown_base_type)

おすすめ商品情報の追加

おすすめ商品情報(おすすめ商品、売れ筋商品、新着商品、イチオシ商品のいずれか)を商品に追加します。

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
api_instance = colormeshop.ProductApi(colormeshop.ApiClient(configuration))
product_id = 56 # int | 商品ID
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object | 

try:
    # おすすめ商品情報の追加
    api_response = api_instance.post_product_pickup(product_id, unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->post_product_pickup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| 商品ID | 
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> object update_product(product_id, product_update_request=product_update_request)

商品データの更新

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
api_instance = colormeshop.ProductApi(colormeshop.ApiClient(configuration))
product_id = 56 # int | 商品ID
product_update_request = colormeshop.ProductUpdateRequest() # ProductUpdateRequest | 商品データ (optional)

try:
    # 商品データの更新
    api_response = api_instance.update_product(product_id, product_update_request=product_update_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| 商品ID | 
 **product_update_request** | [**ProductUpdateRequest**](ProductUpdateRequest.md)| 商品データ | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

