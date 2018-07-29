# SaleDelivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 配送ID | [optional] 
**account_id** | **str** | ショップアカウントID | [optional] 
**sale_id** | **int** | 売上ID | [optional] 
**delivery_id** | **int** | 使用された配送方法ID | [optional] 
**detail_ids** | **list[int]** | この配送に含まれる受注明細IDの配列 | [optional] 
**name** | **str** | 宛名 | [optional] 
**furigana** | **str** | 宛名のフリガナ | [optional] 
**postal** | **str** | 郵便番号 | [optional] 
**pref_id** | **int** | 都道府県の通し番号。北海道が1、沖縄が47 | [optional] 
**pref_name** | **str** | 都道府県名 | [optional] 
**address1** | **str** | 住所1 | [optional] 
**address2** | **str** | 住所2 | [optional] 
**tel** | **str** | 電話番号 | [optional] 
**preferred_date** | **str** | 配送希望日 | [optional] 
**preferred_period** | **str** | 配送希望時間帯 | [optional] 
**slip_number** | **str** | 配送伝票番号 | [optional] 
**noshi_text** | **str** | 熨斗の文言 | [optional] 
**noshi_charge** | **int** | 熨斗の料金 | [optional] 
**card_name** | **str** | メッセージカードの表示名 | [optional] 
**card_text** | **str** | メッセージカードのテキスト | [optional] 
**card_charge** | **int** | メッセージカードの料金 | [optional] 
**wrapping_name** | **str** | ラッピングの表示名 | [optional] 
**wrapping_charge** | **int** | ラッピングの料金 | [optional] 
**delivery_charge** | **int** | 配送料 | [optional] 
**total_charge** | **int** | 配送料・手数料の小計 | [optional] 
**memo** | **str** | 備考 | [optional] 
**delivered** | **bool** | 発送済みであるか否か | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


