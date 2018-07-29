# Product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ショップアカウントID | [optional] 
**id** | **int** | 商品ID | [optional] 
**name** | **str** | 商品名 | [optional] 
**stocks** | **int** | 在庫数 | [optional] 
**stock_managed** | **bool** | 在庫管理するか否か | [optional] 
**few_num** | **int** | 残りわずかとなる在庫数 | [optional] 
**model_number** | **str** | 型番 | [optional] 
**category** | **object** |  | [optional] 
**group_ids** | **list[int]** | 商品が属するグループのIDの配列 | [optional] 
**display_state** | **str** | 掲載設定 | [optional] 
**sales_price** | **int** | 販売価格 | [optional] 
**price** | **int** | 定価 | [optional] 
**members_price** | **int** | 会員価格 | [optional] 
**cost** | **int** | 原価 | [optional] 
**delivery_charge** | **int** | 個別送料 | [optional] 
**min_num** | **int** | 最小購入数量 | [optional] 
**max_num** | **int** | 最大購入数量 | [optional] 
**sale_start_date** | **int** | 掲載開始時刻 | [optional] 
**sale_end_date** | **int** | 掲載終了時刻 | [optional] 
**unit** | **str** | 単位 | [optional] 
**weight** | **int** | 重量(グラム単位) | [optional] 
**soldout_display** | **bool** | 売り切れているときもショップに表示するか | [optional] 
**sort** | **int** | 表示順 | [optional] 
**simple_expl** | **str** | 簡易説明 | [optional] 
**expl** | **str** | 商品説明 | [optional] 
**mobile_expl** | **str** | フィーチャーフォン向けショップの商品説明 | [optional] 
**smartphone_expl** | **str** | スマホ向けショップの商品説明 | [optional] 
**make_date** | **int** | 商品作成日時 | [optional] 
**update_date** | **int** | 商品更新日時 | [optional] 
**memo** | **str** | 備考 | [optional] 
**image_url** | **str** | メインの商品画像URL | [optional] 
**mobile_image_url** | **str** | メインの商品画像のモバイル用URL | [optional] 
**thumbnail_image_url** | **str** | メインの商品画像のサムネイルURL | [optional] 
**images** | **list[object]** | メインの商品画像以外の3つの画像に関する、PC用とモバイル用の画像URL | [optional] 
**options** | [**list[ProductOption]**](ProductOption.md) | 選択できるオプションの一覧 | [optional] 
**variants** | [**list[ProductVariant]**](ProductVariant.md) | オプションのバリエーション一覧 | [optional] 
**pickups** | **list[object]** | おすすめ商品情報 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


