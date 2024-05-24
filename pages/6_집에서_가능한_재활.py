import streamlit as st


st.set_page_config(
    page_title="뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)
st.title("집에서 훈련하는 재활")

st.header('옷 입기 & 옷 벗기', divider='rainbow')
VIDEO_URL_1 = "https://youtu.be/z2-XmK39lKI"
st.video(VIDEO_URL_1)

st.divider()  # 👈 Draws a horizontal rule

st.header('자세변경하기, 이동하기', divider='rainbow')
VIDEO_URL_2 = "https://youtu.be/vKXSNsBqfX8"
st.video(VIDEO_URL_2)

VIDEO_URL_3 = "https://youtu.be/pgpo9JhQdqU"
st.video(VIDEO_URL_3)

VIDEO_URL_4 = "https://youtu.be/VGpa2o18xCE"
st.video(VIDEO_URL_4)

VIDEO_URL_5 = "https://youtu.be/nM2BAB8BHGM"
st.video(VIDEO_URL_5)

VIDEO_URL_6 = "https://youtu.be/Nwf9mFWuDao"
st.video(VIDEO_URL_6)

st.divider()  # 👈 Draws a horizontal rule

st.header('사킴장애 시 식사 훈련', divider='rainbow')

VIDEO_URL_7 = "https://youtu.be/73fT4XjLgaU"
st.video(VIDEO_URL_7)

