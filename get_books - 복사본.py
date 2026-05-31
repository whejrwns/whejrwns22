import urllib.request
import re
import ssl
import urllib.parse

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

queries = [
    ('이방인 민음사', 'book_1.jpg'),
    ('변신 프란츠 카프카 민음사', 'book_2.jpg')
]

for query, filename in queries:
    try:
        url = 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=' + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            html = response.read().decode('utf-8', errors='ignore')
            # Look for aladin cover image
            match = re.search(r'https://image.aladin.co.kr/product/[^\"]+cover[^\"]+', html)
            if match:
                img_url = match.group(0)
                # replace 'cover' or 'coversum' with 'cover500' for higher quality if possible
                img_url = img_url.replace('coversum', 'cover500')
                with urllib.request.urlopen(img_url, context=ctx) as img_resp:
                    with open(filename, 'wb') as f:
                        f.write(img_resp.read())
                print('Saved', filename)
            else:
                print('No image found for', query)
    except Exception as e:
        print('Error on', query, e)
