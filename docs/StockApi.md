# colormeshop.StockApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stocks**](StockApi.md#get_stocks) | **GET** /v1/stocks.json | 在庫情報の取得


# **get_stocks**
> object get_stocks(ids=ids, category_id_big=category_id_big, category_id_small=category_id_small, model_number=model_number, name=name, display_state=display_state, stocks=stocks, recent_zero_stocks=recent_zero_stocks, fields=fields, limit=limit, offset=offset)

在庫情報の取得

在庫情報を商品名や型番で検索できるAPIです。 

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
api_instance = colormeshop.StockApi(colormeshop.ApiClient(configuration))
ids = 'ids_example' # str | 商品IDで検索。カンマ区切りにすることで複数検索が可能 (optional)
category_id_big = 56 # int | 大カテゴリーIDで検索 (optional)
category_id_small = 56 # int | 小カテゴリーIDで検索 (optional)
model_number = 'model_number_example' # str | 型番で部分一致検索 (optional)
name = 'name_example' # str | 商品名で部分一致検索 (optional)
display_state = 'display_state_example' # str | 掲載設定で検索 (optional)
stocks = 56 # int | 在庫管理している商品のうち、在庫数が指定した数値以下の商品を検索。オプションごとに在庫管理している商品は、合計在庫数で検索される (optional)
recent_zero_stocks = True # bool | `true` の場合、過去1週間以内に更新された商品から検索 (optional)
fields = 'fields_example' # str | レスポンスJSONのキーをカンマ区切りで指定 (optional)
limit = 56 # int | レスポンスの件数を指定。指定がない場合は10。最大50 (optional)
offset = 56 # int | 指定した数値+1件目以降のデータを返す (optional)

try:
    # 在庫情報の取得
    api_response = api_instance.get_stocks(ids=ids, category_id_big=category_id_big, category_id_small=category_id_small, model_number=model_number, name=name, display_state=display_state, stocks=stocks, recent_zero_stocks=recent_zero_stocks, fields=fields, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockApi->get_stocks: %s\n" % e)
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
 **recent_zero_stocks** | **bool**| &#x60;true&#x60; の場合、過去1週間以内に更新された商品から検索 | [optional] 
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

