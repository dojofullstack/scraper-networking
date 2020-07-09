#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import argparse
import json
import importlib

import detect_tech.cmseekdb.basic as cmseek # All the basic functions
import detect_tech.cmseekdb.core as core
import detect_tech.cmseekdb.createindex as createindex

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def detect_tech(link):
    try:
        cmseek.redirect_conf = '1'
        target = cmseek.process_url(link)
        cua = cmseek.randomua('random')
        data = core.main_proc(target, cua)
        return data.get('name', '')
    except Exception as e:
        return ''
