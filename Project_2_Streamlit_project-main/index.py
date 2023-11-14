from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="my webpage", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def local_css(file_name):
    with open(file_name) as D:
        st.markdown(f"<style>{D.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
lottie_coding = load_lottieurl("https://lottie.host/7734ba71-c5bc-4cd3-a6e7-496d02c2ba7d/hpFnv2rUsP.json")
img_contact_form=Image.open("D:\streamlit_project_1\images\yt_contact_form.jpeg")
img_lottie_animation=Image.open("D:\streamlit_project_1\images\yt_lottie_animation.jpeg")
with st.container():
    st.subheader("Hi, Iam sven :wave:")
    st.title("A data analysts from germany")
    st.write("Iam passionate about finding ways to use python and VBA to be more efficent and effective in business settings.")
    st.write("[Learn more](https://pythonandvba.com)") 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write(
            """
             my YouTube channel I am creating tutorials for people who:
             - are looking for a way to leverage the power of Python in their day-to-day work.
             - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBN
             - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
             - are working with Excel and found themselves thinking - "there has to be a better way."
             If this sounds interesting to you, consider subscribing and turning on the notifications.
             """
        )
        st.write(" [YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
with st.container():
    st.write("---")
    st.header("my projects")
    st.write("##")
    image_column, text_column=st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate lottie animation inside your streamkit app")
        st.write(
            """
            Learn how to use lottie files in streamlit!
            animation make our web app more engaging and fun, and lottie files are the easiest way to do
            in this turotrial, I'll show you exactly how to do it
            """
        )
        st.markdown("[watch video...](https://youtu.be/TXSOitGoINE)")
    with st.container():
        st.write("---")
        st.header("my projects")
        st.write("##")
    image_column, text_column=st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate lottie animation inside your streamkit app")
        st.write(
            """
            want to add acontant form to your streamlit website?
            In this video, I'm going to show you how to implement a contact form in your streamlit app using
            """
        )
        st.markdown("[watch video...](https://youtu.be/FOULV9Xij_8)")
with st.container():
    st.write("---")
    st.header("get in touch with me!")
    st.write("##")
    contact_form="""
    <form action="https://formsubmit.co/codingisfun.user@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email"placeholder="your mail" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column=st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()


        

        
