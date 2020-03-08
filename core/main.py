from core.html_downloader import get_content
from core.parser import *
from core.util import check_day
from env.environment import url_base, path_download
from datetime import date
import sys
import subprocess

sys.path.append('..')

content = get_content(url_base)

sub_tree = get_section_by_class(content, 'section', 'main-highlights wrapper')

link_tag = get_section_by_class(sub_tree.replace('[','').replace(']',''), 'a', 'image')

links = get_href_by_tag(link_tag, 'a')

if len(links) > 0:
    content_nc_page = get_content(links[0])

    link_tag_download = get_section_by_value ( content_nc_page, 'option', 'download-quality-high')

    url_download =  get_data_url(link_tag_download)

    if url_download:

        if check_day( get_date ( sub_tree )):
            bash_command = 'wget ' + url_download + ' -P ' + path_download +  ''

            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)

            output, error = process.communicate()    
        else:
            print('Nerdcast não foi lançado nesta semana')


