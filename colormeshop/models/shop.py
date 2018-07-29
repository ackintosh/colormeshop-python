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


class Shop(object):
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
        'id': 'str',
        'state': 'str',
        'domain_plan': 'str',
        'contract_plan': 'str',
        'contract_start_date': 'int',
        'contract_end_date': 'int',
        'contract_term': 'int',
        'last_login_date': 'int',
        'setup_date': 'int',
        'make_date': 'int',
        'url': 'str',
        'open_state': 'str',
        'mobile_open_state': 'str',
        'login_id': 'str',
        'name1': 'str',
        'name2': 'str',
        'name1_kana': 'str',
        'name2_kana': 'str',
        'hojin': 'str',
        'hojin_kana': 'str',
        'user_mail': 'str',
        'tel': 'str',
        'fax': 'str',
        'postal': 'str',
        'pref_id': 'int',
        'pref_name': 'str',
        'address1': 'str',
        'address2': 'str',
        'title': 'str',
        'title_short': 'str',
        'shop_mail_1': 'str',
        'shop_mail_2': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'domain_plan': 'domain_plan',
        'contract_plan': 'contract_plan',
        'contract_start_date': 'contract_start_date',
        'contract_end_date': 'contract_end_date',
        'contract_term': 'contract_term',
        'last_login_date': 'last_login_date',
        'setup_date': 'setup_date',
        'make_date': 'make_date',
        'url': 'url',
        'open_state': 'open_state',
        'mobile_open_state': 'mobile_open_state',
        'login_id': 'login_id',
        'name1': 'name1',
        'name2': 'name2',
        'name1_kana': 'name1_kana',
        'name2_kana': 'name2_kana',
        'hojin': 'hojin',
        'hojin_kana': 'hojin_kana',
        'user_mail': 'user_mail',
        'tel': 'tel',
        'fax': 'fax',
        'postal': 'postal',
        'pref_id': 'pref_id',
        'pref_name': 'pref_name',
        'address1': 'address1',
        'address2': 'address2',
        'title': 'title',
        'title_short': 'title_short',
        'shop_mail_1': 'shop_mail_1',
        'shop_mail_2': 'shop_mail_2'
    }

    def __init__(self, id=None, state=None, domain_plan=None, contract_plan=None, contract_start_date=None, contract_end_date=None, contract_term=None, last_login_date=None, setup_date=None, make_date=None, url=None, open_state=None, mobile_open_state=None, login_id=None, name1=None, name2=None, name1_kana=None, name2_kana=None, hojin=None, hojin_kana=None, user_mail=None, tel=None, fax=None, postal=None, pref_id=None, pref_name=None, address1=None, address2=None, title=None, title_short=None, shop_mail_1=None, shop_mail_2=None):  # noqa: E501
        """Shop - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._state = None
        self._domain_plan = None
        self._contract_plan = None
        self._contract_start_date = None
        self._contract_end_date = None
        self._contract_term = None
        self._last_login_date = None
        self._setup_date = None
        self._make_date = None
        self._url = None
        self._open_state = None
        self._mobile_open_state = None
        self._login_id = None
        self._name1 = None
        self._name2 = None
        self._name1_kana = None
        self._name2_kana = None
        self._hojin = None
        self._hojin_kana = None
        self._user_mail = None
        self._tel = None
        self._fax = None
        self._postal = None
        self._pref_id = None
        self._pref_name = None
        self._address1 = None
        self._address2 = None
        self._title = None
        self._title_short = None
        self._shop_mail_1 = None
        self._shop_mail_2 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if domain_plan is not None:
            self.domain_plan = domain_plan
        if contract_plan is not None:
            self.contract_plan = contract_plan
        if contract_start_date is not None:
            self.contract_start_date = contract_start_date
        if contract_end_date is not None:
            self.contract_end_date = contract_end_date
        if contract_term is not None:
            self.contract_term = contract_term
        if last_login_date is not None:
            self.last_login_date = last_login_date
        if setup_date is not None:
            self.setup_date = setup_date
        if make_date is not None:
            self.make_date = make_date
        if url is not None:
            self.url = url
        if open_state is not None:
            self.open_state = open_state
        if mobile_open_state is not None:
            self.mobile_open_state = mobile_open_state
        if login_id is not None:
            self.login_id = login_id
        if name1 is not None:
            self.name1 = name1
        if name2 is not None:
            self.name2 = name2
        if name1_kana is not None:
            self.name1_kana = name1_kana
        if name2_kana is not None:
            self.name2_kana = name2_kana
        if hojin is not None:
            self.hojin = hojin
        if hojin_kana is not None:
            self.hojin_kana = hojin_kana
        if user_mail is not None:
            self.user_mail = user_mail
        if tel is not None:
            self.tel = tel
        if fax is not None:
            self.fax = fax
        if postal is not None:
            self.postal = postal
        if pref_id is not None:
            self.pref_id = pref_id
        if pref_name is not None:
            self.pref_name = pref_name
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if title is not None:
            self.title = title
        if title_short is not None:
            self.title_short = title_short
        if shop_mail_1 is not None:
            self.shop_mail_1 = shop_mail_1
        if shop_mail_2 is not None:
            self.shop_mail_2 = shop_mail_2

    @property
    def id(self):
        """Gets the id of this Shop.  # noqa: E501

        ショップアカウントID  # noqa: E501

        :return: The id of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Shop.

        ショップアカウントID  # noqa: E501

        :param id: The id of this Shop.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this Shop.  # noqa: E501

        アカウント状態  # noqa: E501

        :return: The state of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Shop.

        アカウント状態  # noqa: E501

        :param state: The state of this Shop.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "suspended", "unsigned"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def domain_plan(self):
        """Gets the domain_plan of this Shop.  # noqa: E501

        ドメインプラン  # noqa: E501

        :return: The domain_plan of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._domain_plan

    @domain_plan.setter
    def domain_plan(self, domain_plan):
        """Sets the domain_plan of this Shop.

        ドメインプラン  # noqa: E501

        :param domain_plan: The domain_plan of this Shop.  # noqa: E501
        :type: str
        """
        allowed_values = ["cmsp_sub_domain", "own_domain", "own_sub_domain"]  # noqa: E501
        if domain_plan not in allowed_values:
            raise ValueError(
                "Invalid value for `domain_plan` ({0}), must be one of {1}"  # noqa: E501
                .format(domain_plan, allowed_values)
            )

        self._domain_plan = domain_plan

    @property
    def contract_plan(self):
        """Gets the contract_plan of this Shop.  # noqa: E501

        契約プラン  # noqa: E501

        :return: The contract_plan of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._contract_plan

    @contract_plan.setter
    def contract_plan(self, contract_plan):
        """Sets the contract_plan of this Shop.

        契約プラン  # noqa: E501

        :param contract_plan: The contract_plan of this Shop.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "economy", "small", "regular", "lolipop", "heteml", "platinum", "goope", "large"]  # noqa: E501
        if contract_plan not in allowed_values:
            raise ValueError(
                "Invalid value for `contract_plan` ({0}), must be one of {1}"  # noqa: E501
                .format(contract_plan, allowed_values)
            )

        self._contract_plan = contract_plan

    @property
    def contract_start_date(self):
        """Gets the contract_start_date of this Shop.  # noqa: E501

        契約開始日時  # noqa: E501

        :return: The contract_start_date of this Shop.  # noqa: E501
        :rtype: int
        """
        return self._contract_start_date

    @contract_start_date.setter
    def contract_start_date(self, contract_start_date):
        """Sets the contract_start_date of this Shop.

        契約開始日時  # noqa: E501

        :param contract_start_date: The contract_start_date of this Shop.  # noqa: E501
        :type: int
        """

        self._contract_start_date = contract_start_date

    @property
    def contract_end_date(self):
        """Gets the contract_end_date of this Shop.  # noqa: E501

        契約終了日時  # noqa: E501

        :return: The contract_end_date of this Shop.  # noqa: E501
        :rtype: int
        """
        return self._contract_end_date

    @contract_end_date.setter
    def contract_end_date(self, contract_end_date):
        """Sets the contract_end_date of this Shop.

        契約終了日時  # noqa: E501

        :param contract_end_date: The contract_end_date of this Shop.  # noqa: E501
        :type: int
        """

        self._contract_end_date = contract_end_date

    @property
    def contract_term(self):
        """Gets the contract_term of this Shop.  # noqa: E501

        契約期間  # noqa: E501

        :return: The contract_term of this Shop.  # noqa: E501
        :rtype: int
        """
        return self._contract_term

    @contract_term.setter
    def contract_term(self, contract_term):
        """Sets the contract_term of this Shop.

        契約期間  # noqa: E501

        :param contract_term: The contract_term of this Shop.  # noqa: E501
        :type: int
        """

        self._contract_term = contract_term

    @property
    def last_login_date(self):
        """Gets the last_login_date of this Shop.  # noqa: E501

        最終ログイン日時  # noqa: E501

        :return: The last_login_date of this Shop.  # noqa: E501
        :rtype: int
        """
        return self._last_login_date

    @last_login_date.setter
    def last_login_date(self, last_login_date):
        """Sets the last_login_date of this Shop.

        最終ログイン日時  # noqa: E501

        :param last_login_date: The last_login_date of this Shop.  # noqa: E501
        :type: int
        """

        self._last_login_date = last_login_date

    @property
    def setup_date(self):
        """Gets the setup_date of this Shop.  # noqa: E501

        申し込み完了日時  # noqa: E501

        :return: The setup_date of this Shop.  # noqa: E501
        :rtype: int
        """
        return self._setup_date

    @setup_date.setter
    def setup_date(self, setup_date):
        """Sets the setup_date of this Shop.

        申し込み完了日時  # noqa: E501

        :param setup_date: The setup_date of this Shop.  # noqa: E501
        :type: int
        """

        self._setup_date = setup_date

    @property
    def make_date(self):
        """Gets the make_date of this Shop.  # noqa: E501

        アカウント作成日時  # noqa: E501

        :return: The make_date of this Shop.  # noqa: E501
        :rtype: int
        """
        return self._make_date

    @make_date.setter
    def make_date(self, make_date):
        """Sets the make_date of this Shop.

        アカウント作成日時  # noqa: E501

        :param make_date: The make_date of this Shop.  # noqa: E501
        :type: int
        """

        self._make_date = make_date

    @property
    def url(self):
        """Gets the url of this Shop.  # noqa: E501

        ショップURL  # noqa: E501

        :return: The url of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Shop.

        ショップURL  # noqa: E501

        :param url: The url of this Shop.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def open_state(self):
        """Gets the open_state of this Shop.  # noqa: E501

        開店状態  # noqa: E501

        :return: The open_state of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._open_state

    @open_state.setter
    def open_state(self, open_state):
        """Sets the open_state of this Shop.

        開店状態  # noqa: E501

        :param open_state: The open_state of this Shop.  # noqa: E501
        :type: str
        """
        allowed_values = ["opened", "closed", "prepare", "paused"]  # noqa: E501
        if open_state not in allowed_values:
            raise ValueError(
                "Invalid value for `open_state` ({0}), must be one of {1}"  # noqa: E501
                .format(open_state, allowed_values)
            )

        self._open_state = open_state

    @property
    def mobile_open_state(self):
        """Gets the mobile_open_state of this Shop.  # noqa: E501

        モバイルショップ開店状態  # noqa: E501

        :return: The mobile_open_state of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._mobile_open_state

    @mobile_open_state.setter
    def mobile_open_state(self, mobile_open_state):
        """Sets the mobile_open_state of this Shop.

        モバイルショップ開店状態  # noqa: E501

        :param mobile_open_state: The mobile_open_state of this Shop.  # noqa: E501
        :type: str
        """
        allowed_values = ["opened", "closed", "prepare", "paused"]  # noqa: E501
        if mobile_open_state not in allowed_values:
            raise ValueError(
                "Invalid value for `mobile_open_state` ({0}), must be one of {1}"  # noqa: E501
                .format(mobile_open_state, allowed_values)
            )

        self._mobile_open_state = mobile_open_state

    @property
    def login_id(self):
        """Gets the login_id of this Shop.  # noqa: E501

        ログインID  # noqa: E501

        :return: The login_id of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        """Sets the login_id of this Shop.

        ログインID  # noqa: E501

        :param login_id: The login_id of this Shop.  # noqa: E501
        :type: str
        """

        self._login_id = login_id

    @property
    def name1(self):
        """Gets the name1 of this Shop.  # noqa: E501

        登録者氏名（姓）  # noqa: E501

        :return: The name1 of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._name1

    @name1.setter
    def name1(self, name1):
        """Sets the name1 of this Shop.

        登録者氏名（姓）  # noqa: E501

        :param name1: The name1 of this Shop.  # noqa: E501
        :type: str
        """

        self._name1 = name1

    @property
    def name2(self):
        """Gets the name2 of this Shop.  # noqa: E501

        登録者氏名（名）  # noqa: E501

        :return: The name2 of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._name2

    @name2.setter
    def name2(self, name2):
        """Sets the name2 of this Shop.

        登録者氏名（名）  # noqa: E501

        :param name2: The name2 of this Shop.  # noqa: E501
        :type: str
        """

        self._name2 = name2

    @property
    def name1_kana(self):
        """Gets the name1_kana of this Shop.  # noqa: E501

        登録者氏名カナ（姓）  # noqa: E501

        :return: The name1_kana of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._name1_kana

    @name1_kana.setter
    def name1_kana(self, name1_kana):
        """Sets the name1_kana of this Shop.

        登録者氏名カナ（姓）  # noqa: E501

        :param name1_kana: The name1_kana of this Shop.  # noqa: E501
        :type: str
        """

        self._name1_kana = name1_kana

    @property
    def name2_kana(self):
        """Gets the name2_kana of this Shop.  # noqa: E501

        登録者氏名カナ（名）  # noqa: E501

        :return: The name2_kana of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._name2_kana

    @name2_kana.setter
    def name2_kana(self, name2_kana):
        """Sets the name2_kana of this Shop.

        登録者氏名カナ（名）  # noqa: E501

        :param name2_kana: The name2_kana of this Shop.  # noqa: E501
        :type: str
        """

        self._name2_kana = name2_kana

    @property
    def hojin(self):
        """Gets the hojin of this Shop.  # noqa: E501

        法人名  # noqa: E501

        :return: The hojin of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._hojin

    @hojin.setter
    def hojin(self, hojin):
        """Sets the hojin of this Shop.

        法人名  # noqa: E501

        :param hojin: The hojin of this Shop.  # noqa: E501
        :type: str
        """

        self._hojin = hojin

    @property
    def hojin_kana(self):
        """Gets the hojin_kana of this Shop.  # noqa: E501

        法人名カナ  # noqa: E501

        :return: The hojin_kana of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._hojin_kana

    @hojin_kana.setter
    def hojin_kana(self, hojin_kana):
        """Sets the hojin_kana of this Shop.

        法人名カナ  # noqa: E501

        :param hojin_kana: The hojin_kana of this Shop.  # noqa: E501
        :type: str
        """

        self._hojin_kana = hojin_kana

    @property
    def user_mail(self):
        """Gets the user_mail of this Shop.  # noqa: E501

        登録者メールアドレス  # noqa: E501

        :return: The user_mail of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._user_mail

    @user_mail.setter
    def user_mail(self, user_mail):
        """Sets the user_mail of this Shop.

        登録者メールアドレス  # noqa: E501

        :param user_mail: The user_mail of this Shop.  # noqa: E501
        :type: str
        """

        self._user_mail = user_mail

    @property
    def tel(self):
        """Gets the tel of this Shop.  # noqa: E501

        登録者電話番号  # noqa: E501

        :return: The tel of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._tel

    @tel.setter
    def tel(self, tel):
        """Sets the tel of this Shop.

        登録者電話番号  # noqa: E501

        :param tel: The tel of this Shop.  # noqa: E501
        :type: str
        """

        self._tel = tel

    @property
    def fax(self):
        """Gets the fax of this Shop.  # noqa: E501

        登録者FAX番号  # noqa: E501

        :return: The fax of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this Shop.

        登録者FAX番号  # noqa: E501

        :param fax: The fax of this Shop.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def postal(self):
        """Gets the postal of this Shop.  # noqa: E501

        郵便番号  # noqa: E501

        :return: The postal of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._postal

    @postal.setter
    def postal(self, postal):
        """Sets the postal of this Shop.

        郵便番号  # noqa: E501

        :param postal: The postal of this Shop.  # noqa: E501
        :type: str
        """

        self._postal = postal

    @property
    def pref_id(self):
        """Gets the pref_id of this Shop.  # noqa: E501

        都道府県ID  # noqa: E501

        :return: The pref_id of this Shop.  # noqa: E501
        :rtype: int
        """
        return self._pref_id

    @pref_id.setter
    def pref_id(self, pref_id):
        """Sets the pref_id of this Shop.

        都道府県ID  # noqa: E501

        :param pref_id: The pref_id of this Shop.  # noqa: E501
        :type: int
        """

        self._pref_id = pref_id

    @property
    def pref_name(self):
        """Gets the pref_name of this Shop.  # noqa: E501

        都道府県名  # noqa: E501

        :return: The pref_name of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._pref_name

    @pref_name.setter
    def pref_name(self, pref_name):
        """Sets the pref_name of this Shop.

        都道府県名  # noqa: E501

        :param pref_name: The pref_name of this Shop.  # noqa: E501
        :type: str
        """

        self._pref_name = pref_name

    @property
    def address1(self):
        """Gets the address1 of this Shop.  # noqa: E501

        住所1  # noqa: E501

        :return: The address1 of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Shop.

        住所1  # noqa: E501

        :param address1: The address1 of this Shop.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Shop.  # noqa: E501

        住所2  # noqa: E501

        :return: The address2 of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Shop.

        住所2  # noqa: E501

        :param address2: The address2 of this Shop.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def title(self):
        """Gets the title of this Shop.  # noqa: E501

        ショップ名  # noqa: E501

        :return: The title of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Shop.

        ショップ名  # noqa: E501

        :param title: The title of this Shop.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def title_short(self):
        """Gets the title_short of this Shop.  # noqa: E501

        メールタイトル用ショップ名  # noqa: E501

        :return: The title_short of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._title_short

    @title_short.setter
    def title_short(self, title_short):
        """Sets the title_short of this Shop.

        メールタイトル用ショップ名  # noqa: E501

        :param title_short: The title_short of this Shop.  # noqa: E501
        :type: str
        """

        self._title_short = title_short

    @property
    def shop_mail_1(self):
        """Gets the shop_mail_1 of this Shop.  # noqa: E501

        管理者メールアドレス  # noqa: E501

        :return: The shop_mail_1 of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._shop_mail_1

    @shop_mail_1.setter
    def shop_mail_1(self, shop_mail_1):
        """Sets the shop_mail_1 of this Shop.

        管理者メールアドレス  # noqa: E501

        :param shop_mail_1: The shop_mail_1 of this Shop.  # noqa: E501
        :type: str
        """

        self._shop_mail_1 = shop_mail_1

    @property
    def shop_mail_2(self):
        """Gets the shop_mail_2 of this Shop.  # noqa: E501

        管理者携帯メールアドレス  # noqa: E501

        :return: The shop_mail_2 of this Shop.  # noqa: E501
        :rtype: str
        """
        return self._shop_mail_2

    @shop_mail_2.setter
    def shop_mail_2(self, shop_mail_2):
        """Sets the shop_mail_2 of this Shop.

        管理者携帯メールアドレス  # noqa: E501

        :param shop_mail_2: The shop_mail_2 of this Shop.  # noqa: E501
        :type: str
        """

        self._shop_mail_2 = shop_mail_2

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
        if not isinstance(other, Shop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
