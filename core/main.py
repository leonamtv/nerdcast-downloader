from core.html_downloader import get_content
from core.parser import get_section_by_class, get_href_by_tag, get_section_by_value, get_data_url
from env.environment import url_base, path_download
from datetime import datetime
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
        bash_command = 'wget ' + url_download + ' -P ' + path_download +  ''

        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)

        output, error = process.communicate()    



