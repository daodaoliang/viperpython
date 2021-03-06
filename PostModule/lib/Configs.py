# -*- coding: utf-8 -*-
# @File  : configs.py
# @Date  : 2019/3/6
# @Desc  :

import os

from django.conf import settings

# 目录信息

MODULE_DATA_DIR = os.path.join(settings.BASE_DIR, 'MODULES_DATA')

HANDLER_OPTION = {'name': '_msgrpc_handler', 'name_tag': '监听', 'type': 'enum', 'desc': '模块需要的监听器',
                  'option_length': 24}

CACHE_HANDLER_OPTION = {'name': 'cacheHandler', 'name_tag': "缓存监听", 'type': 'bool', 'desc': "模块执行成功后,缓存对应监听配置",
                        'default': True, "required": True, }

CREDENTIAL_OPTION = {'name': '_postmodule_credential', 'name_tag': '凭证', 'type': 'enum', 'desc': '模块需要的凭证参数',
                     'option_length': 24}

FILE_OPTION = {'name': '_postmodule_file', 'name_tag': '文件', 'type': 'enum',
               'desc': '模块执行需要的文件,可以通过<数据管理>-<文件>处上传',
               'option_length': 24}


class BROKER(object):
    empty = 'empty'  # 多模块配合
    post_python_job = 'post_python_job'  # 多模块配合
    post_msf_job = 'post_msf_job'  # 后台运行的模块
    bot_msf_job = 'bot_msf_job'  # 后台运行的模块


class TAG2CH(object):
    example = 'example'  # '样例模块',
    internal = 'internal'  # 内部模块(不提供可视化输出,用于内部的模块)

    # 蠕虫模块
    Bot_MSF_Scan = "Bot_MSF_Scan"  # 基于msf的扫描模块
    Bot_MSF_Exp = "Bot_MSF_Exp"  # 基于msf的攻击模块
    Bot_PY_Scan = "Bot_PY_Scan"  # python原生扫描模块
    Bot_PY_Exp = "Bot_PY_Exp"  # python原生攻击模块

    # 内网渗透类模块
    Initial_Access = 'Initial_Access'  # '初始访问'
    Execution = 'Execution'  # '执行'
    Persistence = 'Persistence'  # '持久化',
    Privilege_Escalation = 'Privilege_Escalation'  # '权限提升'
    Defense_Evasion = 'Defense_Evasion'  # '防御绕过'
    Credential_Access = 'Credential_Access'  # '凭证访问'
    Discovery = 'Discovery'  # '信息收集'
    Lateral_Movement = 'Lateral_Movement'  # '横向移动'
    Collection = 'Collection'  # '数据采集'
    Command_and_Control = 'Command_and_Control'  # '命令控制'
    Exfiltration = 'Exfiltration'  # '数据窃取'
    Impact = 'Impact'  # '影响破坏'

    @staticmethod
    def get_moduletype_order(MODULETYPE):
        order_dict = {
            "example": 0,
            "internal": 1,
            "Initial_Access": 10,
            "Execution": 11,
            "Persistence": 12,
            "Privilege_Escalation": 13,
            "Defense_Evasion": 14,
            "Credential_Access": 15,
            "Discovery": 16,
            "Lateral_Movement": 17,
            "Collection": 18,
            "Command_and_Control": 19,
            "Exfiltration": 20,
            "Impact": 21,
        }
        order = order_dict.get(MODULETYPE)
        if order is not None:
            return order
        else:
            return 100
