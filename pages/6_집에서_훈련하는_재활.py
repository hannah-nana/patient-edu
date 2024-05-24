import streamlit as st


st.set_page_config(
    page_title="집에서 훈련하는 재활 | 뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)

# 커스텀 사이드 바
st.sidebar.title("무엇이 궁금하세요?")
st.sidebar.markdown("## ")
st.sidebar.page_link("app.py", label="🏠 홈페이지")
st.sidebar.page_link("pages/1_위험요인.py", label="1️⃣ 위험요인")
st.sidebar.page_link("pages/2_증상과_대처방법.py", label="2️⃣ 증상 & 대처방법")
st.sidebar.page_link("pages/3_치료방법.py", label="3️⃣ 치료방법")
st.sidebar.page_link("pages/4_퇴원_후_자가관리.py", label="4️⃣ 퇴원 후 자가관리")
st.sidebar.page_link("pages/5_생활습관_관리.py", label="5️⃣ 생활습관 관리")
st.sidebar.page_link("pages/6_집에서_훈련하는_재활.py", label="6️⃣ 집에서 훈련하는 재활")
st.sidebar.page_link("pages/7_자주_묻는_질문들.py", label="7️⃣ 자주 묻는 질문")
st.sidebar.page_link("pages/9_더_많은_정보.py", label="8️⃣ 더 많은 정보")
st.sidebar.page_link("pages/8_질문_있어요!.py", label="😎 제가 답해드릴게요!")
st.sidebar.page_link("pages/10_커뮤니티.py", label="🌍 커뮤니티")

st.title("집에서 훈련하는 재활")

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)  # 공간 추가

st.header('옷 입기 & 옷 벗기', divider='violet')
VIDEO_URL_1 = "https://youtu.be/z2-XmK39lKI"
st.video(VIDEO_URL_1)

st.divider()  # 👈 Draws a horizontal rule

st.header('자세변경하기, 이동하기', divider='violet')
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

st.header('사킴장애 시 식사 훈련', divider='violet')

VIDEO_URL_7 = "https://youtu.be/73fT4XjLgaU"
st.video(VIDEO_URL_7)

