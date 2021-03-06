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


class ApplicationChargeCreateResponse(object):
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
        'id': 'int',
        'account_id': 'str',
        'oauth_application_id': 'int',
        'application_charge_plan_id': 'int',
        'return_url': 'str',
        'confirmation_url': 'str',
        'status': 'str',
        'make_date': 'int',
        'update_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'oauth_application_id': 'oauth_application_id',
        'application_charge_plan_id': 'application_charge_plan_id',
        'return_url': 'return_url',
        'confirmation_url': 'confirmation_url',
        'status': 'status',
        'make_date': 'make_date',
        'update_date': 'update_date'
    }

    def __init__(self, id=None, account_id=None, oauth_application_id=None, application_charge_plan_id=None, return_url=None, confirmation_url=None, status=None, make_date=None, update_date=None):  # noqa: E501
        """ApplicationChargeCreateResponse - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._account_id = None
        self._oauth_application_id = None
        self._application_charge_plan_id = None
        self._return_url = None
        self._confirmation_url = None
        self._status = None
        self._make_date = None
        self._update_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if oauth_application_id is not None:
            self.oauth_application_id = oauth_application_id
        if application_charge_plan_id is not None:
            self.application_charge_plan_id = application_charge_plan_id
        if return_url is not None:
            self.return_url = return_url
        if confirmation_url is not None:
            self.confirmation_url = confirmation_url
        if status is not None:
            self.status = status
        if make_date is not None:
            self.make_date = make_date
        if update_date is not None:
            self.update_date = update_date

    @property
    def id(self):
        """Gets the id of this ApplicationChargeCreateResponse.  # noqa: E501

        課金ID  # noqa: E501

        :return: The id of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationChargeCreateResponse.

        課金ID  # noqa: E501

        :param id: The id of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this ApplicationChargeCreateResponse.  # noqa: E501

        アカウントID  # noqa: E501

        :return: The account_id of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ApplicationChargeCreateResponse.

        アカウントID  # noqa: E501

        :param account_id: The account_id of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def oauth_application_id(self):
        """Gets the oauth_application_id of this ApplicationChargeCreateResponse.  # noqa: E501

        アプリケーションID  # noqa: E501

        :return: The oauth_application_id of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._oauth_application_id

    @oauth_application_id.setter
    def oauth_application_id(self, oauth_application_id):
        """Sets the oauth_application_id of this ApplicationChargeCreateResponse.

        アプリケーションID  # noqa: E501

        :param oauth_application_id: The oauth_application_id of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: int
        """

        self._oauth_application_id = oauth_application_id

    @property
    def application_charge_plan_id(self):
        """Gets the application_charge_plan_id of this ApplicationChargeCreateResponse.  # noqa: E501

        課金プランID  # noqa: E501

        :return: The application_charge_plan_id of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._application_charge_plan_id

    @application_charge_plan_id.setter
    def application_charge_plan_id(self, application_charge_plan_id):
        """Sets the application_charge_plan_id of this ApplicationChargeCreateResponse.

        課金プランID  # noqa: E501

        :param application_charge_plan_id: The application_charge_plan_id of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: int
        """

        self._application_charge_plan_id = application_charge_plan_id

    @property
    def return_url(self):
        """Gets the return_url of this ApplicationChargeCreateResponse.  # noqa: E501

        ショップオーナー様が課金の許可/拒否を行った後に遷移するURL  # noqa: E501

        :return: The return_url of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this ApplicationChargeCreateResponse.

        ショップオーナー様が課金の許可/拒否を行った後に遷移するURL  # noqa: E501

        :param return_url: The return_url of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: str
        """

        self._return_url = return_url

    @property
    def confirmation_url(self):
        """Gets the confirmation_url of this ApplicationChargeCreateResponse.  # noqa: E501

        ショップオーナー様が課金のOK/NGを行う確認画面ページのURLです。 URLには課金IDとsignatureを含んでいます。   # noqa: E501

        :return: The confirmation_url of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_url

    @confirmation_url.setter
    def confirmation_url(self, confirmation_url):
        """Sets the confirmation_url of this ApplicationChargeCreateResponse.

        ショップオーナー様が課金のOK/NGを行う確認画面ページのURLです。 URLには課金IDとsignatureを含んでいます。   # noqa: E501

        :param confirmation_url: The confirmation_url of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: str
        """

        self._confirmation_url = confirmation_url

    @property
    def status(self):
        """Gets the status of this ApplicationChargeCreateResponse.  # noqa: E501

        ステータス  # noqa: E501

        :return: The status of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApplicationChargeCreateResponse.

        ステータス  # noqa: E501

        :param status: The status of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "accepted", "declined", "active", "expired"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def make_date(self):
        """Gets the make_date of this ApplicationChargeCreateResponse.  # noqa: E501

        作成日時  # noqa: E501

        :return: The make_date of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._make_date

    @make_date.setter
    def make_date(self, make_date):
        """Sets the make_date of this ApplicationChargeCreateResponse.

        作成日時  # noqa: E501

        :param make_date: The make_date of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: int
        """

        self._make_date = make_date

    @property
    def update_date(self):
        """Gets the update_date of this ApplicationChargeCreateResponse.  # noqa: E501

        更新日時  # noqa: E501

        :return: The update_date of this ApplicationChargeCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this ApplicationChargeCreateResponse.

        更新日時  # noqa: E501

        :param update_date: The update_date of this ApplicationChargeCreateResponse.  # noqa: E501
        :type: int
        """

        self._update_date = update_date

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
        if not isinstance(other, ApplicationChargeCreateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
