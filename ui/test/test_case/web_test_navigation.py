# coding=utf-8

import sys
import os
import time
import unittest
from ui.view.businessview.web.common.login_business import simple_login
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from ui.view.businessview.web.common.stream_topbar_business import *
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path
from ui.view.businessview.web.admin.navigation_business import *
from selenium.common.exceptions import NoSuchElementException

class web_test_navigation(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        self.data = Yaml(web_config_path).read()
        self.env = self.data['env']

    def test_navigation(self):
        self.driver = simple_login()
        navigation_business = Navigation_business(self.driver)
        url = self.data['portal'][self.env] + '/admin'
        self.driver.get(url)

        #navigation menu
        for (key,value) in navigation_business.navigation_menu_dict.items():
            print("尝试点击按钮：", key, value)
            try:
                navigation_business.click_navigation_button(navigation_business.navigation_menu_dict[key])
                navigation_business.tabpage_is_element_present(navigation_business.tabpage_dict[key])
                print("进入"+key+"界面")
            except Exception as ex:
                print("Failed！！！,",format(ex))

        #dropdownlist
        for (key,value) in navigation_business.dropdownlist_dict.items():
            print("尝试点击按钮：",key,value)
            try:
                navigation_business.click_navigation_button(navigation_business.dropdownlist_dict[key])
                print("隐藏菜单:",key)
            except Exception as ex:
                print("隐藏菜单失败:",key,format(ex))

        #Admin settings标签
        print("确认Admin settings标签是否存在")
        try:
            navigation_business.adminsettings_is_element_present()
            print("Admin settings标签存在")
        except Exception as ex:
            print("Admin settings标签不存在",format(ex))


if __name__ == '__main__':
    unittest.main()
