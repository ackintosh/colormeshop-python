# ProductCategory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_big** | **int** | 大カテゴリーID | [optional] 
**id_small** | **int** | 小カテゴリーID。大カテゴリーのことを表している場合は0 | [optional] 
**account_id** | **str** | ショップアカウントID | [optional] 
**name** | **str** | 商品カテゴリー名 | [optional] 
**image_url** | **str** | 商品カテゴリー画像URL | [optional] 
**expl** | **str** | 商品カテゴリー説明 | [optional] 
**sort** | **int** | 表示順 | [optional] 
**display_state** | **str** | 掲載設定 | [optional] 
**make_date** | **int** | 商品カテゴリー作成日時 | [optional] 
**update_date** | **int** | 商品カテゴリー更新日時 | [optional] 
**children** | [**list[ProductCategory]**](ProductCategory.md) | 子カテゴリー情報。子カテゴリーのことを表している場合はこのキーはレスポンスに含まれない | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


