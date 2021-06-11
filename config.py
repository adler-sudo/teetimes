# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:40:15 2021

@author: james
"""

# configuration file for environment variables that we 
# don't want going to github

# import modules
from dotenv import load_dotenv
import os


# load environment variables from .env file
load_dotenv()

# define environment variables
FORETEE_USERNAME = os.environ['FORETEE_USERNAME']
FORETEE_PASSWORD = os.environ['FORETEE_PASSWORD']
CHROMEDRIVER = os.environ['CHROMEDRIVER']
TEETIME_DIRECTORY = os.environ['TEETIME_DIRECTORY']