# Payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 決済方法ID | [optional] 
**account_id** | **str** | ショップアカウントID | [optional] 
**name** | **str** | 決済名 | [optional] 
**fee** | **int** | 決済手数料 | [optional] 
**ip_code** | **str** | GMOイプシロン等との契約コード | [optional] 
**memo** | **str** | 説明 | [optional] 
**memo_mobile** | **str** | フィーチャーフォン向けショップ用の説明 | [optional] 
**sort** | **int** | 表示順 | [optional] 
**image_url** | **str** | 決済画像URL | [optional] 
**type** | **int** | 決済タイプを表す数値。  |type|決済| |---|---| |0|代引き| |1|銀行振込| |2|郵便振替| |3|クレジット（ZEUS）| |4|クロネコ@ペイメント| |5|NP後払い| |6|クレジット（イプシロン）| |7|コンビニ決済（イプシロン）| |8|カラーミークレジット| |9|その他決済| |10|ウェブマネー| |11|イーバンクデビット| |12|ネット銀行（イプシロン）| |13|電子マネー（イプシロン）| |14|ATM・コンビニ・ネット銀行決済（ペイジェント）| |15|Do-Link決済（イプシロン）| |16|ペイジー（イプシロン）| |17|後払い.com| |18|ジャパンネット銀行（送料無料キャンペーン）| |19|クロネコwebコレクト| |20|PayPal（イプシロン）| |21|Yahoo!ウォレット（イプシロン）| |22|全額ポイント利用| |23|スマートフォンキャリア決済（イプシロン）| |24|GMO PG マルチペイメントクレジットカード| |25|住信SBIネット銀行（イプシロン）| |26|GMO後払い（イプシロン）| |27|GMO後払い（GMOペイメントサービス）| |28| - | |29|ATM（ペイジー）（ペイジェント）| |30|カード（ペイジェント）| |31|コンビニ番号方式（ペイジェント）| |32|インターネットバンキング（ペイジェント）| |33|PayPal（ペイパル）| |34|SMBC GMO PAYMENTクレジットカード| |35|Amazon Pay| |36|楽天ペイ（オンライン決済）|  | [optional] 
**display** | **bool** | 表示設定。&#x60;true&#x60;なら表示される | [optional] 
**use_mobile** | **bool** | フィーチャーフォン向けショップでの表示設定 | [optional] 
**make_date** | **int** | 決済作成日時 | [optional] 
**update_date** | **int** | 決済更新日時 | [optional] 
**cod** | **object** | 代引き決済の設定情報。代引き決済の場合のみ存在する | [optional] 
**card** | **object** | クレジットカードの設定情報。クレジットカード決済の場合のみ存在する | [optional] 
**financial** | **object** | 銀行振り込みの設定情報。銀行振り込み決済の場合のみ存在する | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


