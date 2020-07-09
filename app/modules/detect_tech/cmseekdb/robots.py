#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 - 2020 Tuhinshubhra

# Detect cms using robots.txt
# Rev 1
import re
import detect_tech.cmseekdb.basic as cmseek
def check(url, ua):
    robots = url + '/robots.txt'
    robots_source = cmseek.getsource(robots, ua)
    # print(robots_source[1])
    if robots_source[0] == '1' and robots_source[1] != '':
        # Check begins here
        robots_txt_content = robots_source[1]
        #### START DETECTION FROM HERE
        ## || <- if either of it matches cms detected
        ## :::: <- all the strings has to match (implemented to decrease false positives)
        robots_txt_detection_keys = [
        'If the Joomla site is installed::::Disallow: /administrator/:-joom',
        'Allow: /core/*.css$||Disallow: /index.php/user/login/||Disallow: /web.config:-dru',
        'Disallow: /wp-admin/||Allow: /wp-admin/admin-ajax.php:-wp',
        'Disallow: /kernel/::::Disallow: /language/::::Disallow: /templates_c/:-xoops',
        'Disallow: /textpattern:-tpc',
        'Disallow: /sitecore||Disallow: /sitecore_files||Disallow: /sitecore modules:-score',
        'Disallow: /phpcms||robots.txt for PHPCMS:-phpc',
        'Disallow: /*mt-content*||Disallow: /mt-includes/:-moto',
        'Disallow: /jcmsplugin/:-jcms',
        'Disallow: /ip_cms/||ip_backend_frames.php||ip_backend_worker.php:-impage',
        'Disallow: /flex/tmp/||flex/Logs/:-flex',
        'Disallow: /e107_admin/||e107_handlers||e107_files/cache:-e107',
        'Disallow: /plus/ad_js.php||Disallow: /plus/erraddsave.php||Disallow: /plus/posttocar.php||Disallow: /plus/disdls.php||Disallow: /plus/mytag_js.php||Disallow: /plus/stow.php:-dede',
        'modules/contentbox/themes/:-cbox',
        'Disallow: /contao/:-contao',
        'Disallow: /concrete:-con5',
        'Disallow: /auth/cas::::Disallow: /auth/cas/callback:-dscrs',
        'uc_client::::uc_server::::forum.php?mod=redirect*:-discuz',
        'Disallow: /AfterbuySrcProxy.aspx||Disallow: /afterbuy.asmx||Disallow: /afterbuySrc.asmx:-abuy',
        'Disallow: /craft/:-craft',    # Chances of it being a falsepositive are higher than the chances of me doing something good with my life ;__;
        'Disallow: /app/::::Disallow: /store_closed.html:-csc',
        'Disallow: /*?cartcmd=*:-dweb',
        'Disallow: /epages/Site.admin/||Disallow: /epages/*:-epgs',
        'Disallow: /Mediatheque/:-ezpub',
        'robots.txt automaticaly generated by PrestaShop:-presta',
        'demandware.store||demandware.static||demandware.net:-sfcc',
        'robots.txt for Umbraco||Disallow: /umbraco||Disallow: /umbraco_client:-umbraco',
        'we use Shopify:-shopify',
        'diskuse::::wysiwyg::::dotaz::::hodnoceni:-shoptet',
        'Disallow: /broker::::Disallow: /broker/orders:-smartstore',
        'gestion_e_commerce:-solusquare',
        'spree/products/:-spree',
        '/admin::::/_admin::::offset=0::::_print_version:-amiro',
        'Disallow: /ajax::::Disallow: /apps:-weebly',
        'Disallow: /_backup/::::Disallow: /_mygallery/::::Disallow: /_temp/::::Disallow: /_tempalbums/::::Disallow: /_tmpfileop/::::Disallow: /dbboon/:-godaddywb'
        ]
        for detection_key in robots_txt_detection_keys:
            if ':-' in detection_key:
                detection_array = detection_key.split(':-')
                if '||' in detection_array[0]:
                    detection_strings = detection_array[0].split('||')
                    for detection_string in detection_strings:
                        if detection_string in robots_txt_content and detection_array[1] not in cmseek.ignore_cms:
                            if cmseek.strict_cms == [] or detection_array[1] in cmseek.strict_cms:
                                return ['1', detection_array[1]]
                elif '::::' in detection_array[0]:
                    match_status = '0' # 0 = neutral, 1 = passed, 2 = failed
                    match_strings = detection_array[0].split('::::')
                    for match_string in match_strings:
                        if match_status == '0' or match_status == '1':
                            if match_string in robots_txt_content:
                                match_status = '1'
                            else:
                                match_status = '2'
                        else:
                            match_status = '2'
                    if match_status == '1' and detection_array[1] not in cmseek.ignore_cms:
                        if cmseek.strict_cms == [] or detection_array[1] in cmseek.strict_cms:
                            return ['1', detection_array[1]]
                else:
                    if detection_array[0] in robots_txt_content and detection_array[1] not in cmseek.ignore_cms:
                        if cmseek.strict_cms == [] or detection_array[1] in cmseek.strict_cms:
                            return ['1', detection_array[1]]

        t3_regex = re.search(r'Sitemap: http(.*?)\?type=', robots_txt_content)
        if t3_regex != None and 'tp3' not in cmseek.ignore_cms:
            if cmseek.strict_cms == [] or 'tp3' in cmseek.strict_cms:
                return ['1', 'tp3']

        return ['0','']
    else:
        # cmseek.error('robots.txt not found or empty!')
        return ['0','']
