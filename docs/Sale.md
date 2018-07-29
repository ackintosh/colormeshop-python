# Sale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 売上ID | [optional] 
**account_id** | **str** | ショップアカウントID | [optional] 
**make_date** | **int** | 受注日時 | [optional] 
**update_date** | **int** | 受注更新日時 | [optional] 
**memo** | **str** | 備考 | [optional] 
**payment_id** | **int** | 使用された決済方法ID | [optional] 
**mobile** | **bool** | モバイルからの注文であるか否か | [optional] 
**paid** | **bool** | 入金済みであるか否か | [optional] 
**delivered** | **bool** | 発送済みである否か | [optional] 
**canceled** | **bool** | キャンセル済みであるか否か | [optional] 
**accepted_mail_state** | **str** | 受注メールの送信状態  - &#x60;not_yet&#x60;: 未送信 - &#x60;sent&#x60;: 送信済み - &#x60;pass&#x60;: 送信しない  | [optional] 
**paid_mail_state** | **str** | 入金メールの送信状態  - &#x60;not_yet&#x60;: 未送信 - &#x60;sent&#x60;: 送信済み - &#x60;pass&#x60;: 送信しない  | [optional] 
**delivered_mail_state** | **str** | 発送メールの送信状態  - &#x60;not_yet&#x60;: 未送信 - &#x60;sent&#x60;: 送信済み - &#x60;pass&#x60;: 送信しない  | [optional] 
**accepted_mail_sent_date** | **int** | 受注メールの送信日時 | [optional] 
**paid_mail_sent_date** | **int** | 入金メールの送信日時 | [optional] 
**delivered_mail_sent_date** | **int** | 発送メールの送信日時 | [optional] 
**point_state** | **str** | ショップポイント付与状態  - &#x60;assumed&#x60;: 仮付与 - &#x60;fixed&#x60;: 確定済み - &#x60;canceled&#x60;: キャンセル済み  | [optional] 
**gmo_point_state** | **str** | GMOポイント付与状態  - &#x60;assumed&#x60;: 仮付与 - &#x60;fixed&#x60;: 確定済み - &#x60;canceled&#x60;: キャンセル済み  | [optional] 
**yahoo_point_state** | **str** | Yahooポイント付与状態  - &#x60;assumed&#x60;: 仮付与 - &#x60;fixed&#x60;: 確定済み - &#x60;canceled&#x60;: キャンセル済み  | [optional] 
**product_total_price** | **int** | 商品の合計金額 | [optional] 
**delivery_total_charge** | **int** | 配送料 | [optional] 
**fee** | **int** | 決済手数料 | [optional] 
**tax** | **int** | 商品合計金額に対する消費税 | [optional] 
**noshi_total_charge** | **int** | 熨斗料金 | [optional] 
**card_total_charge** | **int** | メッセージカード料金 | [optional] 
**wrapping_total_charge** | **int** | ラッピング料金 | [optional] 
**point_discount** | **int** | ショップポイントによる割引額 | [optional] 
**gmo_point_discount** | **int** | GMOポイントによる割引額 | [optional] 
**other_discount** | **int** | その他、クーポン等による割引額 | [optional] 
**other_discount_name** | **str** | その他割引の名称 | [optional] 
**total_price** | **int** | 注文総額 | [optional] 
**granted_points** | **int** | 付与されたショップポイント数 | [optional] 
**use_points** | **int** | 使用されたショップポイント数 | [optional] 
**granted_gmo_points** | **int** | 付与されたGMOポイント数 | [optional] 
**use_gmo_points** | **int** | 使用されたGMOポイント数 | [optional] 
**granted_yahoo_points** | **int** | 付与されたYahooポイント数 | [optional] 
**use_yahoo_points** | **int** | 使用されたYahooポイント数 | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**details** | [**list[SaleDetail]**](SaleDetail.md) |  | [optional] 
**sale_deliveries** | [**list[SaleDelivery]**](SaleDelivery.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


