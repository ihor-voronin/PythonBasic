# Install Beautiful Soup
Using pip
```bash
pip install beautifulsoup4
```
Using pipenv
```bash
pipenv install beautifulsoup4
```

# Install HttpX
Using pip
```bash
pip install httpx
```
Using pipenv
```bash
pipenv install httpx
```


# Howto use HttpX
```python
>>> import httpx
>>> r = httpx.get('https://www.example.org/')
>>> r
<Response [200 OK]>
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```