# Delivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 配送方法ID | [optional] 
**account_id** | **str** | ショップアカウントID | [optional] 
**name** | **str** | 配送方法名 | [optional] 
**image_url** | **str** | 配送方法画像URL | [optional] 
**charge_free_type** | **str** | 配送料が無料になる基準  - &#x60;not_free&#x60;: 有料 - &#x60;free&#x60;: 無料 - &#x60;free_to_limit&#x60;: 注文金額が一定以上の場合は無料  | [optional] 
**charge_free_limit** | **int** | 配送料が無料になる金額。&#x60;charge_free_type&#x60;が&#x60;free_to_limit&#x60;の場合のみ意味を持つ | [optional] 
**charge_type** | **str** | 配送料の計算方法  - &#x60;fixed&#x60;: 固定額 - &#x60;by_price&#x60;: 注文金額によって決定 - &#x60;by_area&#x60;: 配送先都道府県によって決定 - &#x60;by_weight&#x60;: 商品重量によって決定  | [optional] 
**charge** | **object** | 配送料設定の詳細。上記の&#x60;charge_free_type&#x60;や&#x60;charge_type&#x60;に基づいて、この中から配送料が決定される | [optional] 
**tax_included** | **bool** | 送料が税込み料金であるか否か | [optional] 
**slip_number_use** | **bool** | 配送伝票番号設定を使用するか否か | [optional] 
**slip_number_url** | **str** | 配送伝票番号確認URL | [optional] 
**memo** | **str** | 配送方法の説明 | [optional] 
**memo2** | **str** | フィーチャーフォン向けショップ用の配送方法説明 | [optional] 
**sort** | **int** | 表示順 | [optional] 
**display_state** | **str** | 表示状態 | [optional] 
**preferred_date_use** | **bool** | 配送希望日を指定可能か | [optional] 
**preferred_period_use** | **bool** | 配送時間帯を指定可能か | [optional] 
**make_date** | **int** | 配送方法作成日時 | [optional] 
**update_date** | **int** | 配送方法更新日時 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


