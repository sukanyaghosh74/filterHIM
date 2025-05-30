# main.py

import os
from filters.image_filter import is_couple_image
from filters.text_filter import detect_couple_keywords
from filters.ocr_filter import extract_text_from_image
from filters.audio_filter import transcribe_audio

# === CONFIG ===
TEST_FOLDER = "dataset"  # Change this to the folder you want to scan

# === MAIN FILTER FUNCTION ===
def scan_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder does not exist: {folder_path}")
        return

    results = {"couple": 0, "non_couple": 0, "skipped": 0}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Only process image files
        if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".webp")):
            results["skipped"] += 1
            continue

        try:
            print(f"\n📷 Scanning: {filename}")

            # === IMAGE FILTER ===
            if is_couple_image(file_path):
                print(f"💔 Result: COUPLE DETECTED — {filename}")
                results["couple"] += 1
            else:
                print(f"💚 Result: NON-COUPLE — {filename}")
                results["non_couple"] += 1

            # === OCR Filter ===
            text = extract_text_from_image(file_path)
            if detect_couple_keywords(text):
                print(f"📝 OCR flagged couple-related text in {filename}")

            # === Caption Filter ===
            caption = get_caption_from_metadata_or_input()  # Placeholder
            if detect_couple_keywords(caption):
                print(f"🗣️ Caption flagged: {caption}")

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")
            results["skipped"] += 1

    # === FINAL SUMMARY ===
    print("\n📊 Final Report:")
    print(f"💔 Couple:      {results['couple']}")
    print(f"💚 Non-Couple:  {results['non_couple']}")
    print(f"⏭️ Skipped:     {results['skipped']}")

# === ENTRY POINT ===
if __name__ == "__main__":
    print("🚀 Running Couple Filter System")
    scan_folder(TEST_FOLDER)
