import streamlit as st
from app_pages.template import template_page

# Define a dictionary of pages
pages = {
    "template": template_page,
}
st.markdown(
"""    <style>
img[data-testid="stLogo"] {
            height: 8rem;
}
</style>""", unsafe_allow_html=True)

SIDEBAR = "images/Slide2.png"

st.logo(SIDEBAR, icon_image=SIDEBAR)

# Create a sidebar for navigation
st.sidebar.title("Navigatie")
selection = st.sidebar.radio("Ga naar", list(pages.keys()))

# Display the selected page
page = pages["template"]
page()

