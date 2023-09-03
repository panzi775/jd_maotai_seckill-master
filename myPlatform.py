from enum import Enum


class PlatformName(Enum):
    JD = 1
    HUAWEI = 2
    T_MALL = 3


class PlatformParams:
    def __init__(self, _platform, _url, _login, _order, _target, _submit=None, _login_way=None):
        self.url = _url
        self.login = _login
        self.loginWay = _login_way
        self.order = _order
        self.submit = _submit
        self.target = _target
        self.platform = _platform


class PlatformParamsFactory:
    @staticmethod
    def create_params(platform):
        if platform == PlatformName.JD:
            return PlatformParams(platform, "https://www.jd.com", "你好，请登录", _order="去结算",
                                  _submit="order-submit", _target="驿路惊鸿",
                                  _login_way="扫码登录", )
        elif platform == PlatformName.HUAWEI:
            return PlatformParams(platform, "https://www.vmall.com/product/10086009079805.html", "请登录",
                                  "立即下单", _target="187",
                                  _submit="checkoutSubmit")
        elif platform == PlatformName.T_MALL:
            return PlatformParams(platform, "https://www.vmall.com/product/10086009079805.html", "请登录", "立即下单",
                                  "187")
        else:
            raise ValueError(f"Unsupported platform: {platform}")
