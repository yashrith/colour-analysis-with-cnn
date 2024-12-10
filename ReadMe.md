# **Skin Tone Color Analysis Using Deep Learning**

### **Overview of the Project**

This project is a **Deep Learning-based Skin Tone Analysis and Color Recommendation System** that uses advanced machine learning models and computer vision techniques to predict a person’s skin tone and suggest suitable color palettes for their styling preferences.

This project leverages **Computer Vision** and **Deep Learning** techniques to:

1. Detect faces in images.
2. Predict the skin tone (Light, Medium, Dark) using a pre-trained **ResNet-18** model.
3. Recommend personalized color palettes for clothing, makeup, or styling based on the detected skin tone.

The model uses **dlib's CNN face detector** to extract face regions and a fine-tuned ResNet-18 model to classify the skin tone. The application is built using **Streamlit**, providing an interactive web-based interface.

---

### **Features**

- 🌟 **Face Detection**: Locates and extracts faces from uploaded images.
- 🎨 **Skin Tone Prediction**: Accurately classifies skin tones into three categories:
  - `Light`
  - `Medium`
  - `Dark`
- 🌈 **Color Recommendations**:
  - **Single Colors**: Simple yet effective combinations.
  - **Dual Colors**: Coordinated two-tone palettes.
  - **Multicolor Palettes**: Vibrant multi-hued recommendations.
- 🖼️ **Interactive UI**: Upload images, view predictions, and explore tailored color recommendations.

---

### **Intended Use Cases**

* **Fashion** : Suggest clothing colors based on skin tone.
* **Makeup** : Recommend shades that complement skin tones.
* **E-commerce** : Help users choose products that match their skin tone.

built using **Streamlit**, providing an interactive web-based interface.

---

### **Why ResNet-18?**

* **ResNet-18** is chosen due to its lightweight architecture and robust performance for image classification tasks.
* The main goal of the project is to analyze how accurately ResNet-18 can predict skin tones when fine-tuned on a specific dataset.
