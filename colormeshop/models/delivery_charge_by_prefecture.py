# coding: utf-8

"""
    カラーミーショップ API

    # カラーミーショップ API  [カラーミーショップ](https://shop-pro.jp) APIでは、受注の検索や商品情報の更新を行うことができます。  ## 利用手順  はじめに、カラーミーデベロッパーアカウントを用意します。[デベロッパー登録ページ](https://api.shop-pro.jp/developers/sign_up)から登録してください。  次に、[登録ページ](https://api.shop-pro.jp/oauth/applications/new)からアプリケーション登録を行ってください。 スマートフォンのWebViewを利用する場合は、リダイレクトURLに`urn:ietf:wg:oauth:2.0:oob`を入力してください。  その後、カラーミーショップアカウントの認証ページを開きます。認証ページのURLは、`https://api.shop-pro.jp/oauth/authorize`に必要なパラメータをつけたものです。  |パラメータ名|値| |---|---| |`client_id`|アプリケーション詳細画面で確認できるクライアントID| |`response_type`|\"code\"という文字列| |`scope`| 別表参照| |`redirect_url`|アプリケーション登録時に入力したリダイレクトURL|  `scope`は、以下のうち、アプリケーションが利用したい機能をスペース区切りで指定してください。  |スコープ|機能| |---|---| |`read_products`|商品データの参照| |`write_products`|在庫データの更新| |`read_sales`|受注・顧客データの参照| |`write_sales`|受注データの更新|  以下のようなURLとなります。  ``` https://api.shop-pro.jp/oauth/authorize?client_id=CLIENT_ID&redirect_uri=REDIRECT_URL&response_type=code&scope=read_products%20write_products ```  初めてこのページを訪れる場合は、カラーミーショップアカウントのIDとパスワードの入力を求められます。 承認ボタンを押すと、このアプリケーションがショップのデータにアクセスすることが許可され、リダイレクトURLへリダイレクトされます。  承認された場合は、`code`というクエリパラメータに認可コードが付与されます。承認がキャンセルされた、またはエラーが起きた場合は、 `error`パラメータにエラーの内容を表す文字列が与えられます。  アプリケーション登録時のリダイレクトURLに`urn:ietf:wg:oauth:2.0:oob`を指定した場合は、以下のようなURLにリダイレクトされます。 末尾のパスが認可コードになっています。  ``` https://api.shop-pro.jp/oauth/authorize/AUTH_CODE ```  認可コードの有効期限は発行から10分間です。  最後に、認可コードとアクセストークンを交換します。以下のパラメータを付けて、`https://api.shop-pro.jp/oauth/token`へリクエストを送ります。  |パラメータ名|値| |---|---| |`client_id`|アプリケーション詳細画面に表示されているクライアントID| |`client_secret`|アプリケーション詳細画面に表示されているクライアントシークレット| |`code`|取得した認可コード| |`grant_type`|\"authorization_code\"という文字列| |`redirect_uri`|アプリケーション登録時に入力したリダイレクトURL|  ```console # curl での例  $ curl -X POST \\   -d'client_id=CLIENT_ID' \\   -d'client_secret=CLIENT_SECRET' \\   -d'code=CODE' \\   -d'grant_type=authorization_code'   \\   -d'redirect_uri=REDIRECT_URI'  \\   'https://api.shop-pro.jp/oauth/token' ```  リクエストが成功すると、以下のようなJSONが返ってきます。  ```json {   \"access_token\": \"d461ab8XXXXXXXXXXXXXXXXXXXXXXXXX\",   \"token_type\": \"bearer\",   \"scope\": \"read_products write_products\" } ```  アクセストークンに有効期限はありませんが、許可済みアプリケーション一覧画面から失効させることができます。なお、同じ認可コードをアクセストークンに交換できるのは1度だけです。  取得したアクセストークンは、Authorizationヘッダに入れて使用します。以下にショップ情報を取得する際の例を示します。  ```console # curlの例  $ curl -H 'Authorization: Bearer d461ab8XXXXXXXXXXXXXXXXXXXXXXXXX' https://api.shop-pro.jp/v1/shop.json ```  ## エラー  カラーミーショップAPI v1では  - エラーコード - エラーメッセージ - ステータスコード  の配列でエラーを表現します。以下に例を示します。  ```json {   \"errors\": [     {       \"code\": 404100,       \"message\": \"レコードが見つかりませんでした。\",       \"status\": 404     }   ] } ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DeliveryChargeByPrefecture(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pref_id': 'int',
        'pref_name': 'str',
        'charge': 'int'
    }

    attribute_map = {
        'pref_id': 'pref_id',
        'pref_name': 'pref_name',
        'charge': 'charge'
    }

    def __init__(self, pref_id=None, pref_name=None, charge=None):  # noqa: E501
        """DeliveryChargeByPrefecture - a model defined in OpenAPI"""  # noqa: E501

        self._pref_id = None
        self._pref_name = None
        self._charge = None
        self.discriminator = None

        if pref_id is not None:
            self.pref_id = pref_id
        if pref_name is not None:
            self.pref_name = pref_name
        if charge is not None:
            self.charge = charge

    @property
    def pref_id(self):
        """Gets the pref_id of this DeliveryChargeByPrefecture.  # noqa: E501

        都道府県の通し番号。北海道が1、沖縄が47、海外が48  # noqa: E501

        :return: The pref_id of this DeliveryChargeByPrefecture.  # noqa: E501
        :rtype: int
        """
        return self._pref_id

    @pref_id.setter
    def pref_id(self, pref_id):
        """Sets the pref_id of this DeliveryChargeByPrefecture.

        都道府県の通し番号。北海道が1、沖縄が47、海外が48  # noqa: E501

        :param pref_id: The pref_id of this DeliveryChargeByPrefecture.  # noqa: E501
        :type: int
        """
        if pref_id is not None and pref_id > 48:  # noqa: E501
            raise ValueError("Invalid value for `pref_id`, must be a value less than or equal to `48`")  # noqa: E501
        if pref_id is not None and pref_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `pref_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._pref_id = pref_id

    @property
    def pref_name(self):
        """Gets the pref_name of this DeliveryChargeByPrefecture.  # noqa: E501

        都道府県名  # noqa: E501

        :return: The pref_name of this DeliveryChargeByPrefecture.  # noqa: E501
        :rtype: str
        """
        return self._pref_name

    @pref_name.setter
    def pref_name(self, pref_name):
        """Sets the pref_name of this DeliveryChargeByPrefecture.

        都道府県名  # noqa: E501

        :param pref_name: The pref_name of this DeliveryChargeByPrefecture.  # noqa: E501
        :type: str
        """

        self._pref_name = pref_name

    @property
    def charge(self):
        """Gets the charge of this DeliveryChargeByPrefecture.  # noqa: E501

        配送料  # noqa: E501

        :return: The charge of this DeliveryChargeByPrefecture.  # noqa: E501
        :rtype: int
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this DeliveryChargeByPrefecture.

        配送料  # noqa: E501

        :param charge: The charge of this DeliveryChargeByPrefecture.  # noqa: E501
        :type: int
        """

        self._charge = charge

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeliveryChargeByPrefecture):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other