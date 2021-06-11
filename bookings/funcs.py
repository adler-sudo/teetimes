# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:42:46 2021

@author: james
"""


# import modules
from selenium import webdriver
from dotenv import load_dotenv

# load environment variables
from config import *


class TeeTime:
    
    def __init__(self):
        
        # set driver location (SHOULD BE ENVIRONMENT VARIABLE)
        self.driver_location = CHROMEDRIVER
        self.driver = webdriver.Chrome(self.driver_location)
        self.driver.maximize_window() # need to maximize window to correctly access elements
        
        # foretees homepage
        self.foretees = 'https://web.foretees.com/v5/servlet/LoginPrompt?cn=cecc'
        

    def signin(self):
        """
        signs in to homepage

        Returns
        -------
        None.

        """
        # connect
        self.driver.get(self.foretees)
        
        # login
        username = self.driver.find_element_by_id('user_name')
        username.send_keys(FORETEE_USERNAME)
        
        password = self.driver.find_element_by_id('password')
        password.send_keys(FORETEE_PASSWORD)
        
        signin = self.driver.find_element_by_class_name('button-primary')
        signin.click()
        
        
    def choose_tee_time(self, day='06/12/2021', teetime='6:56 PM'):
        """
        navigates to teetime page and sets teetime

        Parameters
        ----------
        day : TYPE, optional
            DESCRIPTION. The default is '06/13/2021'.
        teetime : TYPE, optional
            DESCRIPTION. The default is '6:56 PM'.

        Returns
        -------
        None.

        """
        # navigate to day
        teetime_page = 'https://web.foretees.com/v5/cecc_golf_m24/Member_sheet?calDate={}&course=&show_calendar'.format(day)
        self.driver.get(teetime_page)
        
        # click on time slot
        self.driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(teetime)).click()
        
        
    
    def add_others(self, number_players=4):
        """
        reserves additional slots (TBD)

        Parameters
        ----------
        number_players : TYPE, optional
            DESCRIPTION. The default is 3.

        Returns
        -------
        None.

        """
        # reserve spots
        # click on TBD
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[6]/div/div[1]/div[2]/div[2]/ul/li[4]/div').click()
        
        # click X for number of players
        additional_players = number_players - 1 # you are already accounted for
        for i in range(additional_players):
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[6]/div/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/span').click()
        
    
    def submit(self):
        """
        finalizes transaction

        Returns
        -------
        None.

        """
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[6]/div/div[2]/div/div[3]/a[2]').click()
        
        
    
    def close(self):
        """
        ends session

        Returns
        -------
        None.

        """
        self.driver.close()
        
        
        
        
        