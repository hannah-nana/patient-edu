import streamlit as st

st.set_page_config(
    page_title="더 많은 정보 | 뇌졸중 바로알기",
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


st.title("더 많은 정보")

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)  # 공간 추가

st.header("정보 얻을 수 있는 곳",divider="violet")

# 다른 페이지 내용
st.write("다양한 기관에서 뇌졸중과 관련된 정보를 얻으실 수 있습니다.")

st.divider()  # 👈 Draws a horizontal rule

# 버튼을 생성하고, 버튼이 눌렸을 때 링크로 이동
if st.button('대한당뇨병학회 자료실', key=1, use_container_width=True):
    st.markdown(
        """
        <meta http-equiv="refresh" content="0; url=https://www.diabetes.or.kr/general/pds/health_info.php">
        """,
        unsafe_allow_html=True
    )
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)  # 공간 추가


if st.button('대한고혈압학회 고혈압 자가관리 자료',  key=2, use_container_width=True):
    st.markdown(
        """
        <meta http-equiv="refresh" content="0; url=https://www.koreanhypertension.org/sense/self">
        """,
        unsafe_allow_html=True
    )
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)  # 공간 추가

if st.button('금연길라잡이 홈페이지',  key=3, use_container_width=True):
    st.markdown(
        """
        <meta http-equiv="refresh" content="0; url=https://www.nosmokeguide.go.kr/index.do">
        """,
        unsafe_allow_html=True
    )
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)  # 공간 추가
button_code = """
<button onclick="copyToClipboard('15449030')">Copy "15449030" to Clipboard</button>
"""
st.button('금연상담전화: 15449030', key=4, use_container_width=True)

