#!/usr/bin/env python
# -*- coding: utf-8 -*-

product = "test"  # 项目名称
user = 'test'  # 用户目录
configs = {
    'base_file': "base.log",
    'bbs_path': "/home/www/htdocs/html/bbs.{0}.iccgame.com/".format(product),
    'bak_dir': "/home/{0}/bbs_bak/".format(user),
    'logs_path': "forumdata/logs/{0}/{1}.log",
    'ip_deny_file': '/usr/local/nginx/conf/Configs/deny-ip-bbs.conf',  # 需要在对应网站的配置文件include导入此文件
    'web_server': "service nginxd restart",
    'per': 5,
    'product': product,
    'mail': {
        'host': 'localhost',
        'port': 25,
        'user': 'user',
        'pass': 'password',
        'sender': 'user@exampel.com',
        'receivers': ['receiver@exampel.com'],
        'product': product,
    },
    'weixin': {
        'corpid': 'xxxxxxxxxx', #企业微信id
        'secrect': 'xxxxxxxxxxxxx', #秘钥
        'touser': 'xxxxxxxx', #接收人
        'agentid': 1000002, #应用程序id
    }
}

