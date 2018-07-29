# ApplicationChargeCreateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 課金ID | [optional] 
**account_id** | **str** | アカウントID | [optional] 
**oauth_application_id** | **int** | アプリケーションID | [optional] 
**application_charge_plan_id** | **int** | 課金プランID | [optional] 
**return_url** | **str** | ショップオーナー様が課金の許可/拒否を行った後に遷移するURL | [optional] 
**confirmation_url** | **str** | ショップオーナー様が課金のOK/NGを行う確認画面ページのURLです。 URLには課金IDとsignatureを含んでいます。  | [optional] 
**status** | **str** | ステータス | [optional] 
**make_date** | **int** | 作成日時 | [optional] 
**update_date** | **int** | 更新日時 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


