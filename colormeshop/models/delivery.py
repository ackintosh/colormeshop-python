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


class Delivery(object):
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
        'name': 'str',
        'image_url': 'str',
        'charge_free_type': 'str',
        'charge_free_limit': 'int',
        'charge_type': 'str',
        'charge': 'object',
        'tax_included': 'bool',
        'slip_number_use': 'bool',
        'slip_number_url': 'str',
        'memo': 'str',
        'memo2': 'str',
        'sort': 'int',
        'display_state': 'str',
        'preferred_date_use': 'bool',
        'preferred_period_use': 'bool',
        'make_date': 'int',
        'update_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'name': 'name',
        'image_url': 'image_url',
        'charge_free_type': 'charge_free_type',
        'charge_free_limit': 'charge_free_limit',
        'charge_type': 'charge_type',
        'charge': 'charge',
        'tax_included': 'tax_included',
        'slip_number_use': 'slip_number_use',
        'slip_number_url': 'slip_number_url',
        'memo': 'memo',
        'memo2': 'memo2',
        'sort': 'sort',
        'display_state': 'display_state',
        'preferred_date_use': 'preferred_date_use',
        'preferred_period_use': 'preferred_period_use',
        'make_date': 'make_date',
        'update_date': 'update_date'
    }

    def __init__(self, id=None, account_id=None, name=None, image_url=None, charge_free_type=None, charge_free_limit=None, charge_type=None, charge=None, tax_included=None, slip_number_use=None, slip_number_url=None, memo=None, memo2=None, sort=None, display_state=None, preferred_date_use=None, preferred_period_use=None, make_date=None, update_date=None):  # noqa: E501
        """Delivery - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._account_id = None
        self._name = None
        self._image_url = None
        self._charge_free_type = None
        self._charge_free_limit = None
        self._charge_type = None
        self._charge = None
        self._tax_included = None
        self._slip_number_use = None
        self._slip_number_url = None
        self._memo = None
        self._memo2 = None
        self._sort = None
        self._display_state = None
        self._preferred_date_use = None
        self._preferred_period_use = None
        self._make_date = None
        self._update_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if image_url is not None:
            self.image_url = image_url
        if charge_free_type is not None:
            self.charge_free_type = charge_free_type
        if charge_free_limit is not None:
            self.charge_free_limit = charge_free_limit
        if charge_type is not None:
            self.charge_type = charge_type
        if charge is not None:
            self.charge = charge
        if tax_included is not None:
            self.tax_included = tax_included
        if slip_number_use is not None:
            self.slip_number_use = slip_number_use
        if slip_number_url is not None:
            self.slip_number_url = slip_number_url
        if memo is not None:
            self.memo = memo
        if memo2 is not None:
            self.memo2 = memo2
        if sort is not None:
            self.sort = sort
        if display_state is not None:
            self.display_state = display_state
        if preferred_date_use is not None:
            self.preferred_date_use = preferred_date_use
        if preferred_period_use is not None:
            self.preferred_period_use = preferred_period_use
        if make_date is not None:
            self.make_date = make_date
        if update_date is not None:
            self.update_date = update_date

    @property
    def id(self):
        """Gets the id of this Delivery.  # noqa: E501

        配送方法ID  # noqa: E501

        :return: The id of this Delivery.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Delivery.

        配送方法ID  # noqa: E501

        :param id: The id of this Delivery.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this Delivery.  # noqa: E501

        ショップアカウントID  # noqa: E501

        :return: The account_id of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Delivery.

        ショップアカウントID  # noqa: E501

        :param account_id: The account_id of this Delivery.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this Delivery.  # noqa: E501

        配送方法名  # noqa: E501

        :return: The name of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Delivery.

        配送方法名  # noqa: E501

        :param name: The name of this Delivery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image_url(self):
        """Gets the image_url of this Delivery.  # noqa: E501

        配送方法画像URL  # noqa: E501

        :return: The image_url of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Delivery.

        配送方法画像URL  # noqa: E501

        :param image_url: The image_url of this Delivery.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def charge_free_type(self):
        """Gets the charge_free_type of this Delivery.  # noqa: E501

        配送料が無料になる基準  - `not_free`: 有料 - `free`: 無料 - `free_to_limit`: 注文金額が一定以上の場合は無料   # noqa: E501

        :return: The charge_free_type of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._charge_free_type

    @charge_free_type.setter
    def charge_free_type(self, charge_free_type):
        """Sets the charge_free_type of this Delivery.

        配送料が無料になる基準  - `not_free`: 有料 - `free`: 無料 - `free_to_limit`: 注文金額が一定以上の場合は無料   # noqa: E501

        :param charge_free_type: The charge_free_type of this Delivery.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_free", "free", "free_to_limit"]  # noqa: E501
        if charge_free_type not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_free_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_free_type, allowed_values)
            )

        self._charge_free_type = charge_free_type

    @property
    def charge_free_limit(self):
        """Gets the charge_free_limit of this Delivery.  # noqa: E501

        配送料が無料になる金額。`charge_free_type`が`free_to_limit`の場合のみ意味を持つ  # noqa: E501

        :return: The charge_free_limit of this Delivery.  # noqa: E501
        :rtype: int
        """
        return self._charge_free_limit

    @charge_free_limit.setter
    def charge_free_limit(self, charge_free_limit):
        """Sets the charge_free_limit of this Delivery.

        配送料が無料になる金額。`charge_free_type`が`free_to_limit`の場合のみ意味を持つ  # noqa: E501

        :param charge_free_limit: The charge_free_limit of this Delivery.  # noqa: E501
        :type: int
        """

        self._charge_free_limit = charge_free_limit

    @property
    def charge_type(self):
        """Gets the charge_type of this Delivery.  # noqa: E501

        配送料の計算方法  - `fixed`: 固定額 - `by_price`: 注文金額によって決定 - `by_area`: 配送先都道府県によって決定 - `by_weight`: 商品重量によって決定   # noqa: E501

        :return: The charge_type of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this Delivery.

        配送料の計算方法  - `fixed`: 固定額 - `by_price`: 注文金額によって決定 - `by_area`: 配送先都道府県によって決定 - `by_weight`: 商品重量によって決定   # noqa: E501

        :param charge_type: The charge_type of this Delivery.  # noqa: E501
        :type: str
        """
        allowed_values = ["fixed", "by_price", "by_area", "by_weight"]  # noqa: E501
        if charge_type not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def charge(self):
        """Gets the charge of this Delivery.  # noqa: E501

        配送料設定の詳細。上記の`charge_free_type`や`charge_type`に基づいて、この中から配送料が決定される  # noqa: E501

        :return: The charge of this Delivery.  # noqa: E501
        :rtype: object
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this Delivery.

        配送料設定の詳細。上記の`charge_free_type`や`charge_type`に基づいて、この中から配送料が決定される  # noqa: E501

        :param charge: The charge of this Delivery.  # noqa: E501
        :type: object
        """

        self._charge = charge

    @property
    def tax_included(self):
        """Gets the tax_included of this Delivery.  # noqa: E501

        送料が税込み料金であるか否か  # noqa: E501

        :return: The tax_included of this Delivery.  # noqa: E501
        :rtype: bool
        """
        return self._tax_included

    @tax_included.setter
    def tax_included(self, tax_included):
        """Sets the tax_included of this Delivery.

        送料が税込み料金であるか否か  # noqa: E501

        :param tax_included: The tax_included of this Delivery.  # noqa: E501
        :type: bool
        """

        self._tax_included = tax_included

    @property
    def slip_number_use(self):
        """Gets the slip_number_use of this Delivery.  # noqa: E501

        配送伝票番号設定を使用するか否か  # noqa: E501

        :return: The slip_number_use of this Delivery.  # noqa: E501
        :rtype: bool
        """
        return self._slip_number_use

    @slip_number_use.setter
    def slip_number_use(self, slip_number_use):
        """Sets the slip_number_use of this Delivery.

        配送伝票番号設定を使用するか否か  # noqa: E501

        :param slip_number_use: The slip_number_use of this Delivery.  # noqa: E501
        :type: bool
        """

        self._slip_number_use = slip_number_use

    @property
    def slip_number_url(self):
        """Gets the slip_number_url of this Delivery.  # noqa: E501

        配送伝票番号確認URL  # noqa: E501

        :return: The slip_number_url of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._slip_number_url

    @slip_number_url.setter
    def slip_number_url(self, slip_number_url):
        """Sets the slip_number_url of this Delivery.

        配送伝票番号確認URL  # noqa: E501

        :param slip_number_url: The slip_number_url of this Delivery.  # noqa: E501
        :type: str
        """

        self._slip_number_url = slip_number_url

    @property
    def memo(self):
        """Gets the memo of this Delivery.  # noqa: E501

        配送方法の説明  # noqa: E501

        :return: The memo of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this Delivery.

        配送方法の説明  # noqa: E501

        :param memo: The memo of this Delivery.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def memo2(self):
        """Gets the memo2 of this Delivery.  # noqa: E501

        フィーチャーフォン向けショップ用の配送方法説明  # noqa: E501

        :return: The memo2 of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._memo2

    @memo2.setter
    def memo2(self, memo2):
        """Sets the memo2 of this Delivery.

        フィーチャーフォン向けショップ用の配送方法説明  # noqa: E501

        :param memo2: The memo2 of this Delivery.  # noqa: E501
        :type: str
        """

        self._memo2 = memo2

    @property
    def sort(self):
        """Gets the sort of this Delivery.  # noqa: E501

        表示順  # noqa: E501

        :return: The sort of this Delivery.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this Delivery.

        表示順  # noqa: E501

        :param sort: The sort of this Delivery.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def display_state(self):
        """Gets the display_state of this Delivery.  # noqa: E501

        表示状態  # noqa: E501

        :return: The display_state of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._display_state

    @display_state.setter
    def display_state(self, display_state):
        """Sets the display_state of this Delivery.

        表示状態  # noqa: E501

        :param display_state: The display_state of this Delivery.  # noqa: E501
        :type: str
        """
        allowed_values = ["showing", "hidden"]  # noqa: E501
        if display_state not in allowed_values:
            raise ValueError(
                "Invalid value for `display_state` ({0}), must be one of {1}"  # noqa: E501
                .format(display_state, allowed_values)
            )

        self._display_state = display_state

    @property
    def preferred_date_use(self):
        """Gets the preferred_date_use of this Delivery.  # noqa: E501

        配送希望日を指定可能か  # noqa: E501

        :return: The preferred_date_use of this Delivery.  # noqa: E501
        :rtype: bool
        """
        return self._preferred_date_use

    @preferred_date_use.setter
    def preferred_date_use(self, preferred_date_use):
        """Sets the preferred_date_use of this Delivery.

        配送希望日を指定可能か  # noqa: E501

        :param preferred_date_use: The preferred_date_use of this Delivery.  # noqa: E501
        :type: bool
        """

        self._preferred_date_use = preferred_date_use

    @property
    def preferred_period_use(self):
        """Gets the preferred_period_use of this Delivery.  # noqa: E501

        配送時間帯を指定可能か  # noqa: E501

        :return: The preferred_period_use of this Delivery.  # noqa: E501
        :rtype: bool
        """
        return self._preferred_period_use

    @preferred_period_use.setter
    def preferred_period_use(self, preferred_period_use):
        """Sets the preferred_period_use of this Delivery.

        配送時間帯を指定可能か  # noqa: E501

        :param preferred_period_use: The preferred_period_use of this Delivery.  # noqa: E501
        :type: bool
        """

        self._preferred_period_use = preferred_period_use

    @property
    def make_date(self):
        """Gets the make_date of this Delivery.  # noqa: E501

        配送方法作成日時  # noqa: E501

        :return: The make_date of this Delivery.  # noqa: E501
        :rtype: int
        """
        return self._make_date

    @make_date.setter
    def make_date(self, make_date):
        """Sets the make_date of this Delivery.

        配送方法作成日時  # noqa: E501

        :param make_date: The make_date of this Delivery.  # noqa: E501
        :type: int
        """

        self._make_date = make_date

    @property
    def update_date(self):
        """Gets the update_date of this Delivery.  # noqa: E501

        配送方法更新日時  # noqa: E501

        :return: The update_date of this Delivery.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this Delivery.

        配送方法更新日時  # noqa: E501

        :param update_date: The update_date of this Delivery.  # noqa: E501
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
        if not isinstance(other, Delivery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
