# colormeshop.SaleApi

All URIs are relative to *https://api.shop-pro.jp/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_sale**](SaleApi.md#cancel_sale) | **PUT** /v1/sales/{saleId}/cancel.json | 受注のキャンセル
[**get_sale**](SaleApi.md#get_sale) | **GET** /v1/sales/{saleId}.json | 受注データの取得
[**get_sales**](SaleApi.md#get_sales) | **GET** /v1/sales.json | 受注データのリストを取得
[**send_sales_mail**](SaleApi.md#send_sales_mail) | **POST** /v1/sales/{saleId}/mails.json | メールの送信
[**stat_sale**](SaleApi.md#stat_sale) | **GET** /v1/sales/stat.json | 売上集計の取得
[**update_sale**](SaleApi.md#update_sale) | **PUT** /v1/sales/{saleId}.json | 受注データの更新


# **cancel_sale**
> object cancel_sale(sale_id, unknown_base_type=unknown_base_type)

受注のキャンセル

受注をキャンセルすると、以下のことが起こります。  - 該当受注の商品購入数が0になる - 該当受注の合計金額が0になる - 該当受注の`canceled`が`true`になる - 該当受注に使用されたショップポイント・GMOポイントがキャンセルされる - 該当受注の決済がAmazon Pay、または楽天ペイ（オンライン決済）である場合は、決済金額が自動的に購入者へ返金される - カラメル等の販売手数料が0になる 

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
api_instance = colormeshop.SaleApi(colormeshop.ApiClient(configuration))
sale_id = 56 # int | 
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object |  (optional)

try:
    # 受注のキャンセル
    api_response = api_instance.cancel_sale(sale_id, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->cancel_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sale_id** | **int**|  | 
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sale**
> object get_sale(sale_id)

受注データの取得

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
api_instance = colormeshop.SaleApi(colormeshop.ApiClient(configuration))
sale_id = 56 # int | 

try:
    # 受注データの取得
    api_response = api_instance.get_sale(sale_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->get_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sale_id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales**
> object get_sales(ids=ids, after=after, before=before, make_date_min=make_date_min, make_date_max=make_date_max, update_date_min=update_date_min, update_date_max=update_date_max, customer_ids=customer_ids, customer_name=customer_name, customer_furigana=customer_furigana, customer_mail=customer_mail, accepted_mail_state=accepted_mail_state, paid_mail_state=paid_mail_state, delivered_mail_state=delivered_mail_state, mobile=mobile, paid=paid, delivered=delivered, payment_ids=payment_ids, fields=fields, limit=limit, offset=offset)

受注データのリストを取得

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
api_instance = colormeshop.SaleApi(colormeshop.ApiClient(configuration))
ids = 'ids_example' # str | 受注IDで検索。カンマ区切りで複数指定可能 (optional)
after = 'after_example' # str | 指定日時以降の受注から検索 (optional)
before = 'before_example' # str | 指定日時以前の受注から検索 (optional)
make_date_min = 'make_date_min_example' # str | `after`と同義 (optional)
make_date_max = 'make_date_max_example' # str | `before`と同義 (optional)
update_date_min = 'update_date_min_example' # str | 指定日時以降に更新された受注から検索 (optional)
update_date_max = 'update_date_max_example' # str | 指定日時以降に更新された受注から検索 (optional)
customer_ids = 'customer_ids_example' # str | 購入した顧客IDで検索。カンマ区切りにすることで複数検索が可能 (optional)
customer_name = 'customer_name_example' # str | 購入した顧客名で部分一致検索 (optional)
customer_furigana = 'customer_furigana_example' # str | 購入した顧客フリガナがで部分一致検索 (optional)
customer_mail = 'customer_mail_example' # str | 購入した顧客メールアドレスで部分一致検索 (optional)
accepted_mail_state = 56 # int | 受注メールの送信状態で検索  - `0`: 未送信 - `1`: 送信済み - `2`: 送信しない  (optional)
paid_mail_state = 56 # int | 入金メールの送信状態で検索  - `0`: 未送信 - `1`: 送信済み - `2`: 送信しない  (optional)
delivered_mail_state = 56 # int | 配送メールの送信状態で検索  - `0`: 未送信 - `1`: 送信済み - `2`: 送信しない  (optional)
mobile = True # bool | `true`なら携帯からの受注のみ取得 (optional)
paid = True # bool | `true`なら入金済みの受注のみ取得 (optional)
delivered = True # bool | `true`なら配送済みの受注のみ取得 (optional)
payment_ids = 'payment_ids_example' # str | 使用された決済のIDで検索。カンマ区切りで複数指定可能 (optional)
fields = 'fields_example' # str | レスポンスJSONのキーをカンマ区切りで指定 (optional)
limit = 56 # int | レスポンスの件数を指定。指定がない場合は10。最大50 (optional)
offset = 56 # int | 指定した数値+1件目以降のデータを返す (optional)

try:
    # 受注データのリストを取得
    api_response = api_instance.get_sales(ids=ids, after=after, before=before, make_date_min=make_date_min, make_date_max=make_date_max, update_date_min=update_date_min, update_date_max=update_date_max, customer_ids=customer_ids, customer_name=customer_name, customer_furigana=customer_furigana, customer_mail=customer_mail, accepted_mail_state=accepted_mail_state, paid_mail_state=paid_mail_state, delivered_mail_state=delivered_mail_state, mobile=mobile, paid=paid, delivered=delivered, payment_ids=payment_ids, fields=fields, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->get_sales: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| 受注IDで検索。カンマ区切りで複数指定可能 | [optional] 
 **after** | **str**| 指定日時以降の受注から検索 | [optional] 
 **before** | **str**| 指定日時以前の受注から検索 | [optional] 
 **make_date_min** | **str**| &#x60;after&#x60;と同義 | [optional] 
 **make_date_max** | **str**| &#x60;before&#x60;と同義 | [optional] 
 **update_date_min** | **str**| 指定日時以降に更新された受注から検索 | [optional] 
 **update_date_max** | **str**| 指定日時以降に更新された受注から検索 | [optional] 
 **customer_ids** | **str**| 購入した顧客IDで検索。カンマ区切りにすることで複数検索が可能 | [optional] 
 **customer_name** | **str**| 購入した顧客名で部分一致検索 | [optional] 
 **customer_furigana** | **str**| 購入した顧客フリガナがで部分一致検索 | [optional] 
 **customer_mail** | **str**| 購入した顧客メールアドレスで部分一致検索 | [optional] 
 **accepted_mail_state** | **int**| 受注メールの送信状態で検索  - &#x60;0&#x60;: 未送信 - &#x60;1&#x60;: 送信済み - &#x60;2&#x60;: 送信しない  | [optional] 
 **paid_mail_state** | **int**| 入金メールの送信状態で検索  - &#x60;0&#x60;: 未送信 - &#x60;1&#x60;: 送信済み - &#x60;2&#x60;: 送信しない  | [optional] 
 **delivered_mail_state** | **int**| 配送メールの送信状態で検索  - &#x60;0&#x60;: 未送信 - &#x60;1&#x60;: 送信済み - &#x60;2&#x60;: 送信しない  | [optional] 
 **mobile** | **bool**| &#x60;true&#x60;なら携帯からの受注のみ取得 | [optional] 
 **paid** | **bool**| &#x60;true&#x60;なら入金済みの受注のみ取得 | [optional] 
 **delivered** | **bool**| &#x60;true&#x60;なら配送済みの受注のみ取得 | [optional] 
 **payment_ids** | **str**| 使用された決済のIDで検索。カンマ区切りで複数指定可能 | [optional] 
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

# **send_sales_mail**
> send_sales_mail(sale_id, unknown_base_type=unknown_base_type)

メールの送信

受注・入金確認・商品発送メールを送ることができます。

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
api_instance = colormeshop.SaleApi(colormeshop.ApiClient(configuration))
sale_id = 56 # int | 
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object |  (optional)

try:
    # メールの送信
    api_instance.send_sales_mail(sale_id, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling SaleApi->send_sales_mail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sale_id** | **int**|  | 
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stat_sale**
> object stat_sale(make_date=make_date)

売上集計の取得

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
api_instance = colormeshop.SaleApi(colormeshop.ApiClient(configuration))
make_date = 'make_date_example' # str | 集計対象とする売上の作成日。形式は\"2017-04-12\"、\"2017/04/12\"など。指定しない場合は今日の日付が使われる (optional)

try:
    # 売上集計の取得
    api_response = api_instance.stat_sale(make_date=make_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->stat_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make_date** | **str**| 集計対象とする売上の作成日。形式は\&quot;2017-04-12\&quot;、\&quot;2017/04/12\&quot;など。指定しない場合は今日の日付が使われる | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sale**
> object update_sale(sale_id, unknown_base_type=unknown_base_type)

受注データの更新

該当受注の決済がAmazon Pay、または楽天ペイ（オンライン決済）である場合は、熨斗・メッセージカード・ラッピングの手数料を更新すると、決済金額が自動的に購入者に請求もしくは返金されます。

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
api_instance = colormeshop.SaleApi(colormeshop.ApiClient(configuration))
sale_id = 56 # int | 
unknown_base_type = colormeshop.UNKNOWN_BASE_TYPE() # object |  (optional)

try:
    # 受注データの更新
    api_response = api_instance.update_sale(sale_id, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->update_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sale_id** | **int**|  | 
 **unknown_base_type** | [**object**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

