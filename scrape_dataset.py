# scrape_dataset.py

import os
import logging
from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader
from urllib.parse import urlparse

# === Suppress noisy logs ===
logging.getLogger("icrawler").setLevel(logging.WARNING)

# === CONFIG ===
dataset_dir = "dataset"
categories = {
    "couple": [
        "romantic couple", "couples kissing", "cute couple aesthetic", "valentine couple", "love couple"
    ],
    "non_couple": [
        "solo person portrait", "funny memes", "cats", "dogs", "food photography", "nature scenery"
    ]
}
images_per_category = 250  # Total images per label

# === Custom Safe Downloader ===
class SafeDownloader(ImageDownloader):
    def download(self, task, default_ext, timeout=5, **kwargs):
        url = task['file_url']
        parsed = urlparse(url)
        if not parsed.scheme.startswith("http") or '.' not in parsed.netloc:
            print(f"❌ Skipped invalid URL: {url}")
            return
        try:
            super().download(task, default_ext, timeout, **kwargs)
        except Exception as e:
            print(f"⚠️  Download error for {url}: {e}")

# === Create folders ===
def create_dirs():
    for cat in categories:
        path = os.path.join(dataset_dir, cat)
        os.makedirs(path, exist_ok=True)

# === Scrape Images ===
def scrape_images():
    for label, queries in categories.items():
        save_dir = os.path.join(dataset_dir, label)
        print(f"\n🌀 Scraping images for category: {label}")
        crawler = GoogleImageCrawler(storage={'root_dir': save_dir}, downloader_cls=SafeDownloader)
        for q in queries:
            print(f"🔍 Searching: {q}")
            crawler.crawl(
                keyword=q,
                max_num=images_per_category // len(queries),
                file_idx_offset='auto'
            )

if __name__ == "__main__":
    create_dirs()
    scrape_images()
    print("\n✅ Dataset scraping complete. Check the 'dataset/' folder.")
