
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  INCOGNITO/main.py
#  
#  Copyright 2023 by N3S3 
#  < em41l:     'dasnevesnestler' + 
#               '(aT)' + 
#               'gm41l' + 
#               '(d0t)' +
#               'c0m' >
#  
#  This program is a PoC made with prompt-engineering 
#  and was tested on Parrot-OS(Linux - Debian 11 Bullseye).
# 
#  It is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this. If not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  !!!For educational purposes only!!!
#
#
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QComboBox, QPushButton, QTextBrowser, QLineEdit, QApplication, QWidget, QTextEdit, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from bs4 import BeautifulSoup
import random, re, requests, time


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    """
        Initializes the user interface by creating and setting up GUI elements.
        Parameters:
            None
        Returns:
            None
    """

    def initUI(self):
        # Create GUI elements
        self.layout = QVBoxLayout()
        self.proxy_provider_combo = QComboBox()
        self.textbox = QTextEdit()
        self.fetch_button = QPushButton("exploit(provider)")
        
        self.logo = QLabel(self)
        pixmap = QPixmap( 'logo-xss_resized.png')
        self.logo.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio)) 
        self.layout.addWidget(self.logo, alignment=Qt.AlignCenter)
        
        # Set up configuration
        self.config = AppConfiguration()
        self.fetcher = ProxyFetcher(self.config.user_agents)

        # Add items to combo box
        for provider in self.config.proxy_providers:
            self.proxy_provider_combo.addItem(provider)

        # Connect signals and slots
        self.fetch_button.clicked.connect(self.fetch_proxies)

        # Add elements to layout
        self.layout.addWidget(QLabel("select a proxy provider:"))
        self.layout.addWidget(self.proxy_provider_combo)
        self.layout.addWidget(self.fetch_button)
        self.layout.addWidget(QLabel("tested proxies [IP:PORT]: "))
        self.layout.addWidget(self.textbox)

        self.setLayout(self.layout)
        self.setWindowTitle('INCOGNITO by N3S3')
        self.setGeometry(300, 300, 400, 300)
        
        self.setStyleSheet("""
    QWidget {                                 
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(90, 90, 90, 255));                                 
        color: #E0E0E0;                                 
        border-radius: 5px;                             
        font-family: "Arial", sans-serif;
    }

    QLabel {                                 
        color: #FFF;                                 
        font-size: 16px;                             
    }

    QPushButton {                                 
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255), stop:1 rgba(110, 110, 110, 255));                                 
        border: 2px solid #555555;                                 
        padding: 5px;                                 
        font-weight: bold;                             
    }

    QPushButton:hover {                                 
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 90, 90, 255), stop:1 rgba(130, 130, 130, 255));                             
    }

    QPushButton:pressed {                                 
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(90, 90, 90, 255));                             
    }

    QComboBox {                                 
        background-color: rgba(70, 70, 70, 255);                                 
        border: 2px solid #555555;                                 
        padding: 5px;                             
    }

    QComboBox:hover {
        background-color: rgba(90, 90, 90, 255);
    }

    QComboBox::drop-down {
        border: none;
    }

    QComboBox::down-arrow {
        image: url('/home/logout/Downloads/Python_Scripts/32x32.png');
    }

    QTextBrowser {                                 
        background-color: rgba(60, 60, 60, 255);                                 
        border: 2px solid #555555;                             
    }
""")
        self.show()
    
    """
        Fetches proxies from the specified provider and displays the results in the textbox.
        Parameters:
            None
        Returns:
            None
    """

    def fetch_proxies(self):
        provider = self.proxy_provider_combo.currentText()
        ip_with_ports, ips_without_ports, ports = self.fetcher.fetch_generic_proxies(provider)

        # Display the results
        self.textbox.clear()
        for ip in ip_with_ports:
            self.textbox.append(ip)
        for ip, port in zip(ips_without_ports, ports):
            self.textbox.append(f"{ip}:{port}")

class AppConfiguration:
    def __init__(self):
        # list of user agents
        self.user_agents = [
    'AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: unblock4myspace)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: tunisproxy)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-in-rs)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-ba-k)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: moelonepyaeshan)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: mirrorrr)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: mapremiereapplication)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: longbows-hideout)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: eduas23)',
    'AppEngine-Google; (+http://code.google.com/appengine; appid: craigserver)',
    'AppEngine-Google; ( http://code.google.com/appengine; appid: proxy-ba-k)',
    'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; bingbot/2.0 +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',
    'Googlebot/2.1 (+http://www.google.com/bot.html)',
    'Googlebot-Image/1.0',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)',
    'YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)',
    'W3C-checklink/4.5 [4.160] libwww-perl/5.823',
    'W3C-checklink/4.5 [4.154] libwww-perl/5.823',
    'W3C-checklink/4.3 [4.42] libwww-perl/5.820',
    'W3C-checklink/4.3 [4.42] libwww-perl/5.808',
    'W3C-checklink/4.3 [4.42] libwww-perl/5.805',
    'Microsoft URL Control - 6.01.9782'
    ]
        
        # List of proxy providers
        self.proxy_providers = ["sslproxies.org", 
                                "free-proxy-list.net", 
                                "proxyscrape.com",
                                "proxyscrape.com/free-proxy-list",
                                "proxy-list.download/",
                                "hidemy.name/en/proxy-list/",
                                "us-proxy.org/", 
                                "proxynova.com/proxy-server-list/"]


class ProxyFetcher:
    def __init__(self, user_agents):
        self.user_agents = user_agents
    
    """
        Fetches generic proxies from a given provider.
        :param provider: The provider to fetch proxies from.
        :type provider: str
        :return: A tuple containing lists of IP addresses with ports, IP addresses without ports, and ports.
        :rtype: tuple(list[str], list[str], list[int])
    """

    def fetch_generic_proxies(self, provider):
        headers = {
            "User-Agent": random.choice(self.user_agents)
        }
        try:
            response = requests.get(f"http://www.{provider}", headers=headers)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return [], [], []
        except Exception as err:
            print(f"An error occurred: {err}")
            return [], [], []

        soup = BeautifulSoup(response.content, 'html.parser')

        ip_port_pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d{1,5})?\b")
        ip_pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
        port_pattern = re.compile(r'^(?:[1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$')

        # Extract data using regex
        ports = [string for string in soup.stripped_strings if re.match(port_pattern, string)]
        ip_with_ports = [string for string in soup.stripped_strings if re.match(ip_port_pattern, string)]
        ips_without_ports = [string for string in soup.stripped_strings if re.match(ip_pattern, string)]

        return ip_with_ports, ips_without_ports, ports
    
    """
        Generates a list of IP addresses and corresponding ports.
        Args:
            ips_without_ports (List[str]): A list of IP addresses without ports.
            ports (List[int]): A list of port numbers.
        Returns:
            List[str]: A list of IP addresses with ports in the format "ip:port".
    """
    
    def ip_port_list(self, ips_without_ports, ports):
        return [f"{ip}:{port}" for ip, port in zip(ips_without_ports, ports)]
    
    """
        Collects inputs from the user and performs some actions based on those inputs.
    """
    
    def collect_inputs(self):
        proxy_provider = self.proxy_provider_combo.currentText()
        self.results_display.append(f"Proxy Provider: {proxy_provider}")

        proxies = self.fetch_generic_proxies(proxy_provider)
    
    # Test each proxy and display if valid
        for proxy in proxies:
            if self.test_proxy(proxy):
                self.results_display.append(proxy)
    
    """
        Test the given proxy by sending a GET request to "http://www.google.com" using the proxy.
        
        Parameters:
            proxy (str): The proxy to be tested.
        
        Returns:
            bool: True if the GET request is successful and the response status code is 200, False otherwise.
    """

    def test_proxy(self, proxy):
        proxies = {
            "http": proxy,
            "https": proxy
            }
        try:
            response = requests.get("http://www.google.com", proxies=proxies, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
