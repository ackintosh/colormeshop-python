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


class ProductGroup(object):
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
        'expl': 'str',
        'sort': 'int',
        'display_state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'name': 'name',
        'image_url': 'image_url',
        'expl': 'expl',
        'sort': 'sort',
        'display_state': 'display_state'
    }

    def __init__(self, id=None, account_id=None, name=None, image_url=None, expl=None, sort=None, display_state=None):  # noqa: E501
        """ProductGroup - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._account_id = None
        self._name = None
        self._image_url = None
        self._expl = None
        self._sort = None
        self._display_state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if image_url is not None:
            self.image_url = image_url
        if expl is not None:
            self.expl = expl
        if sort is not None:
            self.sort = sort
        if display_state is not None:
            self.display_state = display_state

    @property
    def id(self):
        """Gets the id of this ProductGroup.  # noqa: E501

        商品グループID  # noqa: E501

        :return: The id of this ProductGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductGroup.

        商品グループID  # noqa: E501

        :param id: The id of this ProductGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this ProductGroup.  # noqa: E501

        ショップアカウントID  # noqa: E501

        :return: The account_id of this ProductGroup.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProductGroup.

        ショップアカウントID  # noqa: E501

        :param account_id: The account_id of this ProductGroup.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this ProductGroup.  # noqa: E501

        商品グループ名  # noqa: E501

        :return: The name of this ProductGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductGroup.

        商品グループ名  # noqa: E501

        :param name: The name of this ProductGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image_url(self):
        """Gets the image_url of this ProductGroup.  # noqa: E501

        商品グループ画像URL  # noqa: E501

        :return: The image_url of this ProductGroup.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ProductGroup.

        商品グループ画像URL  # noqa: E501

        :param image_url: The image_url of this ProductGroup.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def expl(self):
        """Gets the expl of this ProductGroup.  # noqa: E501

        商品グループ説明  # noqa: E501

        :return: The expl of this ProductGroup.  # noqa: E501
        :rtype: str
        """
        return self._expl

    @expl.setter
    def expl(self, expl):
        """Sets the expl of this ProductGroup.

        商品グループ説明  # noqa: E501

        :param expl: The expl of this ProductGroup.  # noqa: E501
        :type: str
        """

        self._expl = expl

    @property
    def sort(self):
        """Gets the sort of this ProductGroup.  # noqa: E501

        表示順  # noqa: E501

        :return: The sort of this ProductGroup.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ProductGroup.

        表示順  # noqa: E501

        :param sort: The sort of this ProductGroup.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def display_state(self):
        """Gets the display_state of this ProductGroup.  # noqa: E501

        掲載設定  # noqa: E501

        :return: The display_state of this ProductGroup.  # noqa: E501
        :rtype: str
        """
        return self._display_state

    @display_state.setter
    def display_state(self, display_state):
        """Sets the display_state of this ProductGroup.

        掲載設定  # noqa: E501

        :param display_state: The display_state of this ProductGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["showing", "hidden", "showing_for_members", "sale_for_members"]  # noqa: E501
        if display_state not in allowed_values:
            raise ValueError(
                "Invalid value for `display_state` ({0}), must be one of {1}"  # noqa: E501
                .format(display_state, allowed_values)
            )

        self._display_state = display_state

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
        if not isinstance(other, ProductGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other