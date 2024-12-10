import streamlit as st

# Extended dataset with color names and hex codes
data = {
    "Skin Color Type": ["Light", "Medium", "Dark"],
    "Colour Pattern": [
        "Bright and pastel shades",
        "Warm and earthy tones",
        "Rich and bold colors"
    ],
    "Single Colour": [
        [("Lavender", "#E6E6FA"), ("Mint", "#98FF98"), ("Sky Blue", "#87CEEB"), ("Peach", "#FFDAB9"), ("Powder Pink", "#FFC0CB"), ("Soft Yellow", "#FFFACD"), ("Ivory", "#FFFFF0")],
        [("Olive", "#808000"), ("Coral", "#FF7F50"), ("Beige", "#F5F5DC"), ("Burnt Orange", "#CC5500"), ("Mustard Yellow", "#FFDB58"), ("Turquoise", "#40E0D0"), ("Cinnamon Brown", "#7B3F00")],
        [("Maroon", "#800000"), ("Navy Blue", "#000080"), ("Emerald Green", "#50C878"), ("Gold", "#FFD700"), ("Deep Purple", "#673AB7"), ("Ruby Red", "#9B111E"), ("Charcoal Gray", "#36454F")]
    ],
    "Dual Colour": [
        [("Lavender + Mint", ["#E6E6FA", "#98FF98"]), ("Sky Blue + Peach", ["#87CEEB", "#FFDAB9"]), ("Soft Yellow + Powder Pink", ["#FFFACD", "#FFC0CB"])],
        [("Olive + Coral", ["#808000", "#FF7F50"]), ("Beige + Burnt Orange", ["#F5F5DC", "#CC5500"]), ("Turquoise + Mustard Yellow", ["#40E0D0", "#FFDB58"])],
        [("Maroon + Navy Blue", ["#800000", "#000080"]), ("Emerald Green + Gold", ["#50C878", "#FFD700"]), ("Deep Purple + Ruby Red", ["#673AB7", "#9B111E"])]
    ],
    "Multicolour": [
        [("Lavender + Mint + Sky Blue", ["#E6E6FA", "#98FF98", "#87CEEB"])],
        [("Olive + Coral + Beige", ["#808000", "#FF7F50", "#F5F5DC"])],
        [("Maroon + Navy Blue + Emerald Green", ["#800000", "#000080", "#50C878"])]
    ]
}

# Function to render colors as blocks
def render_colors(color_data):
    for name, colors in color_data:
        if isinstance(colors, list):  # For dual or multicolor palettes
            st.write(f"**{name}:**")
            cols = st.columns(len(colors))
            for idx, color in enumerate(colors):
                cols[idx].markdown(f'<div style="width: 50px; height: 25px; background-color: {color};"></div>', unsafe_allow_html=True)
        else:  # For single colors
            st.write(f"**{name}:**")
            st.markdown(f'<div style="width: 50px; height: 25px; background-color: {colors};"></div>', unsafe_allow_html=True)

# Simulated skin tone prediction
def predict_skin_tone(image_path):
    # Replace with your actual prediction logic
    return "Medium"

# Streamlit application
st.title("Skin Tone Color Analysis")

# Upload an image
uploaded_image = st.file_uploader("Upload an image to predict skin tone:", type=["jpg", "jpeg", "png"])

# Placeholder for predicted skin tone
predicted_skin_tone = None

if uploaded_image:
    # Simulate prediction
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    predicted_skin_tone = predict_skin_tone(uploaded_image.name)
    st.write(f"**Predicted Skin Tone:** {predicted_skin_tone}")

# Display color recommendations based on the predicted skin tone
if predicted_skin_tone and st.button("Best Colors for the Skin Tone"):
    # Retrieve the corresponding color data for the predicted skin tone
    index = data["Skin Color Type"].index(predicted_skin_tone)
    
    st.write(f"### Best Colors for {predicted_skin_tone} Skin Tone")
    st.write(f"**Colour Pattern:** {data['Colour Pattern'][index]}")
    
    # Single Colours
    st.write("### Single Colours")
    render_colors(data["Single Colour"][index])
    
    # Dual Colours
    st.write("### Dual Colours")
    render_colors(data["Dual Colour"][index])
    
    # Multicolours
    st.write("### Multicolours")
    render_colors(data["Multicolour"][index])
