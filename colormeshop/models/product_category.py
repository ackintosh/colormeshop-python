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


class ProductCategory(object):
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
        'id_big': 'int',
        'id_small': 'int',
        'account_id': 'str',
        'name': 'str',
        'image_url': 'str',
        'expl': 'str',
        'sort': 'int',
        'display_state': 'str',
        'make_date': 'int',
        'update_date': 'int',
        'children': 'list[ProductCategory]'
    }

    attribute_map = {
        'id_big': 'id_big',
        'id_small': 'id_small',
        'account_id': 'account_id',
        'name': 'name',
        'image_url': 'image_url',
        'expl': 'expl',
        'sort': 'sort',
        'display_state': 'display_state',
        'make_date': 'make_date',
        'update_date': 'update_date',
        'children': 'children'
    }

    def __init__(self, id_big=None, id_small=None, account_id=None, name=None, image_url=None, expl=None, sort=None, display_state=None, make_date=None, update_date=None, children=None):  # noqa: E501
        """ProductCategory - a model defined in OpenAPI"""  # noqa: E501

        self._id_big = None
        self._id_small = None
        self._account_id = None
        self._name = None
        self._image_url = None
        self._expl = None
        self._sort = None
        self._display_state = None
        self._make_date = None
        self._update_date = None
        self._children = None
        self.discriminator = None

        if id_big is not None:
            self.id_big = id_big
        if id_small is not None:
            self.id_small = id_small
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
        if make_date is not None:
            self.make_date = make_date
        if update_date is not None:
            self.update_date = update_date
        if children is not None:
            self.children = children

    @property
    def id_big(self):
        """Gets the id_big of this ProductCategory.  # noqa: E501

        大カテゴリーID  # noqa: E501

        :return: The id_big of this ProductCategory.  # noqa: E501
        :rtype: int
        """
        return self._id_big

    @id_big.setter
    def id_big(self, id_big):
        """Sets the id_big of this ProductCategory.

        大カテゴリーID  # noqa: E501

        :param id_big: The id_big of this ProductCategory.  # noqa: E501
        :type: int
        """

        self._id_big = id_big

    @property
    def id_small(self):
        """Gets the id_small of this ProductCategory.  # noqa: E501

        小カテゴリーID。大カテゴリーのことを表している場合は0  # noqa: E501

        :return: The id_small of this ProductCategory.  # noqa: E501
        :rtype: int
        """
        return self._id_small

    @id_small.setter
    def id_small(self, id_small):
        """Sets the id_small of this ProductCategory.

        小カテゴリーID。大カテゴリーのことを表している場合は0  # noqa: E501

        :param id_small: The id_small of this ProductCategory.  # noqa: E501
        :type: int
        """

        self._id_small = id_small

    @property
    def account_id(self):
        """Gets the account_id of this ProductCategory.  # noqa: E501

        ショップアカウントID  # noqa: E501

        :return: The account_id of this ProductCategory.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProductCategory.

        ショップアカウントID  # noqa: E501

        :param account_id: The account_id of this ProductCategory.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this ProductCategory.  # noqa: E501

        商品カテゴリー名  # noqa: E501

        :return: The name of this ProductCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductCategory.

        商品カテゴリー名  # noqa: E501

        :param name: The name of this ProductCategory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image_url(self):
        """Gets the image_url of this ProductCategory.  # noqa: E501

        商品カテゴリー画像URL  # noqa: E501

        :return: The image_url of this ProductCategory.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ProductCategory.

        商品カテゴリー画像URL  # noqa: E501

        :param image_url: The image_url of this ProductCategory.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def expl(self):
        """Gets the expl of this ProductCategory.  # noqa: E501

        商品カテゴリー説明  # noqa: E501

        :return: The expl of this ProductCategory.  # noqa: E501
        :rtype: str
        """
        return self._expl

    @expl.setter
    def expl(self, expl):
        """Sets the expl of this ProductCategory.

        商品カテゴリー説明  # noqa: E501

        :param expl: The expl of this ProductCategory.  # noqa: E501
        :type: str
        """

        self._expl = expl

    @property
    def sort(self):
        """Gets the sort of this ProductCategory.  # noqa: E501

        表示順  # noqa: E501

        :return: The sort of this ProductCategory.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ProductCategory.

        表示順  # noqa: E501

        :param sort: The sort of this ProductCategory.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def display_state(self):
        """Gets the display_state of this ProductCategory.  # noqa: E501

        掲載設定  # noqa: E501

        :return: The display_state of this ProductCategory.  # noqa: E501
        :rtype: str
        """
        return self._display_state

    @display_state.setter
    def display_state(self, display_state):
        """Sets the display_state of this ProductCategory.

        掲載設定  # noqa: E501

        :param display_state: The display_state of this ProductCategory.  # noqa: E501
        :type: str
        """
        allowed_values = ["showing", "hidden", "showing_for_members", "sale_for_members"]  # noqa: E501
        if display_state not in allowed_values:
            raise ValueError(
                "Invalid value for `display_state` ({0}), must be one of {1}"  # noqa: E501
                .format(display_state, allowed_values)
            )

        self._display_state = display_state

    @property
    def make_date(self):
        """Gets the make_date of this ProductCategory.  # noqa: E501

        商品カテゴリー作成日時  # noqa: E501

        :return: The make_date of this ProductCategory.  # noqa: E501
        :rtype: int
        """
        return self._make_date

    @make_date.setter
    def make_date(self, make_date):
        """Sets the make_date of this ProductCategory.

        商品カテゴリー作成日時  # noqa: E501

        :param make_date: The make_date of this ProductCategory.  # noqa: E501
        :type: int
        """

        self._make_date = make_date

    @property
    def update_date(self):
        """Gets the update_date of this ProductCategory.  # noqa: E501

        商品カテゴリー更新日時  # noqa: E501

        :return: The update_date of this ProductCategory.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this ProductCategory.

        商品カテゴリー更新日時  # noqa: E501

        :param update_date: The update_date of this ProductCategory.  # noqa: E501
        :type: int
        """

        self._update_date = update_date

    @property
    def children(self):
        """Gets the children of this ProductCategory.  # noqa: E501

        子カテゴリー情報。子カテゴリーのことを表している場合はこのキーはレスポンスに含まれない  # noqa: E501

        :return: The children of this ProductCategory.  # noqa: E501
        :rtype: list[ProductCategory]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ProductCategory.

        子カテゴリー情報。子カテゴリーのことを表している場合はこのキーはレスポンスに含まれない  # noqa: E501

        :param children: The children of this ProductCategory.  # noqa: E501
        :type: list[ProductCategory]
        """

        self._children = children

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
        if not isinstance(other, ProductCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other