from bs4 import BeautifulSoup
import re

def get_section_by_class ( html_content: str, tag_type: str, class_name: str, decode: str = 'ascii' ):
    """
    Retorna (caso haja) uma subárvore html que possua
    como raiz uma tag do tipo 'tag_type' e tenha como
    classe o nome 'class_name'. A subárvore é retirada
    do conteúdo passado em 'html_content'. 
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    content = soup.findAll(tag_type, { "class" : class_name })
    content = bytearray(str(content), 'ascii').decode('utf-8')
    return content

def get_section_by_value ( html_content: str, tag_type: str, value_name: str, decode: str = 'ascii' ):
    """
    Retorna (caso haja) uma subárvore html que possua
    como raiz uma tag do tipo 'tag_type' e tenha como
    value o nome 'value_name'. A subárvore é retirada
    do conteúdo passado em 'html_content'. 
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    content = soup.findAll(tag_type, { "value" : value_name })
    content = bytearray(str(content), 'ascii').decode('utf-8')
    return content

def get_href_by_tag ( html_content: str, tag_type: str ):
    """
    Retorna um array com o valor de todos os 'href' en-
    contrados em tags do tipo 'tag_type' no conteúdo da
    string 'html_content'.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    href_values = [ tag['href'] for tag in soup.findAll(tag_type, href=True)]
    return href_values

def get_data_url ( html_content: str ):
    """
    Busca a url do atributo 'data-url' através de uma
    busca em regex.
    """
    result = re.search(r'(?<=data-url=")(.+\.mp3)(?=".+Alta)', html_content)
    return result.group(0) if result else None

