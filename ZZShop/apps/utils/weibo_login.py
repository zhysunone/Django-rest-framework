# _*_ coding:utf-8  _*_

__author__ = 'zhy'
__date__ = '2018/5/24 16:12'

def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://127.0.0.1:8000/complete/weibo/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_url={re_url}".format(client_id=3328267843, re_url=redirect_url)

    print(auth_url)


if __name__ == '__main__':
    get_auth_url()