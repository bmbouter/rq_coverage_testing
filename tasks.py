import requests

def count_words_at_url(url):
    import pydevd_pycharm
    pydevd_pycharm.settrace('localhost', port=29437, stdoutToServer=True, stderrToServer=True)
    resp = requests.get(url)
    return len(resp.text.split())

