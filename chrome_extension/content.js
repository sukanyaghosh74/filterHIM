let model;

async function loadModel() {
  model = await tf.loadLayersModel(chrome.runtime.getURL("tf_model/model.json"));
  console.log("✅ Model loaded");
}

function isImageCouple(imageTensor) {
  const resized = tf.image.resizeBilinear(imageTensor, [224, 224]);
  const normalized = resized.div(255.0).expandDims(0);
  const prediction = model.predict(normalized);
  return prediction.dataSync()[0] > 0.5;
}

function blurImage(img) {
  img.style.filter = "blur(20px)";
  img.style.transition = "0.3s ease";
}

function processImages() {
  document.querySelectorAll("img").forEach(async (img) => {
    if (!img.complete || img.dataset.checked) return;
    img.dataset.checked = "true";
    try {
      const tfImg = tf.browser.fromPixels(img);
      const isCouple = await isImageCouple(tfImg);
      if (isCouple) {
        blurImage(img);
        console.log("❌ Couple content blocked");
      }
      tfImg.dispose();
    } catch (e) {
      console.warn("Error analyzing image:", e);
    }
  });
}

loadModel().then(() => {
  setInterval(processImages, 2000);
});
