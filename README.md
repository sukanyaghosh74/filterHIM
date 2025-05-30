# 📁 filterHIM — Insta Couple Content Filter

> An AI-powered Chrome extension that auto-detects and blocks couple-related content on Instagram so you can scroll in peace. 🚫💑

---

## 🌟 Features

* 🔍 **Smart Filtering**: Detects and filters out couple content in:

  * 🎞️ Reels (video frames)
  * 🖼️ Images
  * ✍️ Text captions
  * 🔊 Audio clips
* 🧠 **Custom-Trained AI Model**: Uses a CNN-based classifier trained on curated "couple" vs "non-couple" datasets.
* ⚡ **Real-Time OCR & NLP**: Filters content based on text in captions and in-video overlays.
* 🔈 **Audio Sentiment Analysis**: Flags romantic/relationship-themed voice content.
* 🌐 **Seamless Web Experience**: Works while browsing Instagram on Chrome.

---

## 📁 Folder Structure

```
filterHIM/
│
├── assets/
│   └── blocked_keywords.txt      # Keywords related to couple/romantic content
│
├── dataset/
│   ├── couple/                   # Images of couples
│   └── non_couple/              # Non-romantic content
│
├── filters/
│   ├── audio_filter.py          # Filters based on audio content
│   ├── image_filter.py          # Filters based on image classification
│   ├── ocr_filter.py            # Filters based on text inside images
│   └── text_filter.py           # Filters based on captions/hashtags
│
├── models/
│   └── couple_classifier.h5     # Trained image classification model
│
├── config.py                    # Central config for keywords and thresholds
├── main.py                      # Master filter pipeline to evaluate posts
├── scrape_dataset.py           # Scraper to build the dataset
├── train_model.py              # Model training script
└── README.md                   # This file
```

---

## 🧠 How It Works

1. **Image Classifier**: Trained with over 500 images, the model detects couple-centric visual content.
2. **OCR Engine**: Extracts text from reels/posts to detect romantic context (e.g. “my love”, “valentine”).
3. **Text Filter**: Scans post captions, comments, and hashtags using blocked keywords.
4. **Audio Filter**: Uses speech recognition + sentiment analysis to block romantic voice-overs.

If **any filter triggers**, the post is **hidden or blurred** via Chrome content script.

---

## 🚀 Setup & Run Locally

1. **Clone the repo**

   ```bash
   git clone https://github.com/sukanyaghosh74/filterHIM.git
   cd filterHIM
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Train your model (optional if using existing `h5`)**

   ```bash
   python train_model.py
   ```

4. **Run main filter logic**

   ```bash
   python main.py
   ```

5. **Chrome Extension (coming soon)**
   Drag the `extension/` folder into `chrome://extensions` after enabling **Developer Mode**.

---

## 🔍 Tech Stack

* Python (TensorFlow, Keras, OpenCV, Tesseract OCR, SpeechRecognition)
* Chrome Extension (HTML + JS for content blocking)
* iCrawler for dataset scraping

---

## 🙌 Credits

* Built against love 🩷 by [Sukanya Ghosh](https://github.com/sukanyaghosh74)
* Inspired by the need to *filter distractions* and *stay emotionally balanced* online

---

## ⚧ TODOs

* [ ] Add real-time Chrome extension integration
* [ ] Add toggle for blocking level (strict, mild)
* [ ] Cloud-deployable filtering API

---

## 📜 License

MIT License — use freely and modify with care ✨

---

### 💬 “Scroll freely, feel freely.”
