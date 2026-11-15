"""Fetch the six vetted Wikimedia Commons photos and save optimized local WebP files."""
from io import BytesIO
import json
from pathlib import Path
import time

from PIL import Image, ImageOps
import requests

ROOT = Path(__file__).resolve().parents[1]
SESSION = requests.Session()
SESSION.headers['User-Agent'] = 'TheButterflyBook/1.0 (photo preparation)'

for path in sorted((ROOT / 'lib').glob('species-*.json')):
    species = json.loads(path.read_text())
    photo = species['photo']
    destination = ROOT / 'public' / photo['src'].lstrip('/')
    thumb_base = photo['thumbnailUrl'].split('?')[0]
    urls = [
        photo['originalUrl'].split('?')[0],
        thumb_base.replace('/500px-', '/1280px-'),
        photo['thumbnailUrl'],
    ]
    response = None
    for url in urls:
        for attempt in range(2):
            try:
                candidate = SESSION.get(url, timeout=30)
            except requests.RequestException:
                candidate = None
            if candidate and candidate.ok:
                response = candidate
                break
            if candidate and candidate.status_code == 429:
                time.sleep(attempt + 1)
        if response:
            break
    if response is None:
        raise RuntimeError(f'Could not fetch {species["commonName"]} photograph')
    image = ImageOps.exif_transpose(Image.open(BytesIO(response.content))).convert('RGB')
    image.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
    if destination.exists():
        with Image.open(destination) as current:
            if current.width >= image.width:
                print(f'{destination.name}: kept existing {current.size}')
                continue
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, 'WEBP', quality=86, method=6)
    print(destination.name, image.size, destination.stat().st_size)
