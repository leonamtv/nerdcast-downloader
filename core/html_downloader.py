from urllib.request import urlopen, Request
from env.environment import headers

def get_content ( url: str ):
    """
    Busca a página HTML relacionada à url
    passada por parâmetro e retorna uma 
    string com seu conteúdo.
    """
    request = Request(url=url, headers=headers)
    html = urlopen(request).read()
    return str(html)