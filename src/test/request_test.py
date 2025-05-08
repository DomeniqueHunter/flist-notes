import requests

_session = None
_proxies = {}


def send_request(url:str, proxies:dict={}):
    global _session, _proxies
    
    if not _session:
        _session = requests.Session()
    
    if not _proxies:
        _proxies = proxies
        
    _session.proxies = _proxies
    
    response = _session.get(url, timeout=10)
    
    return response.json()


def test():
    url = "https://api.ipify.org?format=json"
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }
    
    resp = send_request(url, proxies=proxies)
    print(resp)
    
    resp = send_request(url)
    print(resp)
    
    
    
    
if __name__ == "__main__":
    test()
    
