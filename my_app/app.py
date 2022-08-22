import streamlit as st
from streamlit.logger import get_logger
from PIL import Image

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Landing page",
        page_icon="👋",
    )

    st.write("# Welcome to Methane Predictor Page! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )
    
    image = Image.open('https://github.com/Jasley/risk_exposure/blob/main/footprints-in-sand.jpg')
    st.image(image, caption='Enter any caption here')


if __name__ == "__main__":
    run()
