import re
import requests
from bs4 import BeautifulSoup

url = "https://game.co.uk"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

# Regex patterns
patterns= {
    'jQuery': r'(?:<script[^>]*\bsrc=["\'][^"\']*jquery[^"\']*["\'][^>]*>|<[^>]*\bid=["\'][^"\']*jquery[^"\']*["\'][^>]*>)',
    'React.js': r'<script[^>]*\bsrc=["\'][^"\']*react[^"\']*["\'][^>]*>',
    'WooCommerce': r'<script[^>]*\bsrc=["\'][^"\']*woocommerce[^"\']*["\'][^>]*>',
    'Bootstrap': r'<link[^>]*\bhref=["\'][^"\']*bootstrap[^"\']*["\'][^>]*>',
    'Shopify': r'<script[^>]*\bsrc=["\'][^"\']*shopify[^"\']*["\'][^>]*>',
    'Next.js': r'<script[^>]*\bsrc=["\'][^"\']*next\.js[^"\']*["\'][^>]*>',
    'Materialize CSS': r'<link[^>]*href=["\'][^>]*materialize[^>]*["\'][^>]*>|<script[^>]*src=["\'][^>]*materialize[^>]*["\'][^>]*>',
    'Python': r'<script[^>]*>\s*var pythonScript',
    'Google Maps': r'<script[^>]*\bsrc=["\'][^"\']*maps\.googleapis\.com[^"\']*["\'][^>]*>'
}

for technology, pattern in patterns.items():
    matches = re.findall(pattern, str(soup))
    if matches:
        print(f"Found {technology} on the website.")






