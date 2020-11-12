#!/usr/bin/env python
from glob import glob

template = '''
<!doctype html>
<html>
  <head>
    <title>Twilio OpenAPI Documentation</title>
    <style>
      ul {
        list-style-type: none;
        display: flex;
        flex-wrap: wrap;
        padding-inline-start: 0;
      }
      li {
        display: block;
        margin: 5px;
        padding: 10px;
        border: 1px solid black;
        border-radius: 20px;
        background: #eef;
      }
      li:hover {
        background: #ccf;
      }
      a {
        text-decoration: none;
        font-size: 110%;
      }
    </style>
  </head>
  <body>
    <h1>Twilio OpenAPI Documentation</h1>
    <ul>

{PRODUCTS}
    </ul>
  </body>
</html>
'''

links = ''
for p in sorted(glob('spec/json/*')):
    product = p.split('/')[-1].split('.')[-2].replace('twilio_', '')
    product, version = product.rsplit('_v', 1)
    links += f'<li><a href=/twilio-oai/redoc.html?product={product}_v{version}>{product.title()} v{version}</a></li>\n'

print(template.strip().replace('{PRODUCTS}', links))
