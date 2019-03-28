import config
import telepot


def set_telepot_socks_proxy(url, username=None, password=None):
    from urllib3.contrib.socks import SOCKSProxyManager
    from telepot.api import _default_pool_params, _onetime_pool_params
    telepot.api._onetime_pool_spec = (SOCKSProxyManager, dict(proxy_url=url, username=username, password=password, **_onetime_pool_params))
    telepot.api._pools['default'] = SOCKSProxyManager(url, username=username, password=password, **_default_pool_params)


def main():
    print('start')
    print(config.token)

    set_telepot_socks_proxy('socks5://sr.spry.fail:1080')
    print('set_telepot_socks_proxy')

    basic_auth = ('', '')

    bot = telepot.Bot(config.token)
    
    print(bot.getMe())

    print('finish')
    

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
