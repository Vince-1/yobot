from aiocqhttp.api import Api
from typing import Any, Dict, List, Optional, Tuple, Union
import asyncio
import logging
import os
import random
import re
import time

class RBQ:
    Passive = True
    Active = False
    Request = False
    
    Commands = {
        '创建rbq管理处':1,
        '查看':2,
        '成为':3,
        '退出':4,
        '翻牌':5,
    }
    
    def __init__(self,glo_setting: Dict[str,Any],
    bot_api:Api,*args,**kwargs):
    self.setting = glo_setting
    self.api = bot_api
    self.rbqPool = glo_setting['rbq']

    #log
    if not os.path.exists(os.path.join(glo_setting['dirname'],'log')):
        os.mkdir(os.path.join(glo_setting['dirname'],'log'))

    formater = logging.Formatter(
        '[%(asctime)s] %(levelname)s: %(message)s')
            filehandler = logging.FileHandler(
            os.path.join(glo_setting['dirname'], 'log', 'rbq.log'),
            encoding='utf-8',
        )
        filehandler.setFormatter(formater)
        consolehandler = logging.StreamHandler()
        consolehandler.setFormatter(formater)
        _logger.addHandler(filehandler)
        _logger.addHandler(consolehandler)
        _logger.setLevel(logging.INFO)
    
            # super-admin initialize
        User.update({User.authority_group: 100}).where(
            User.authority_group == 1
        ).execute()
        User.update({User.authority_group: 1}).where(
            User.qqid.in_(self.setting['super-admin'])
        ).execute()