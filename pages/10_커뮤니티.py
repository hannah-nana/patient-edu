import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import base64

st.set_page_config(
    page_title="커뮤니티 | 뇌졸중 바로알기",
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


# Base64로 인코딩된 JSON 키 파일을 secrets에서 가져오기
json_str = st.secrets["general"]["GOOGLE_CREDENTIALS"]
json_data = json.loads(base64.b64decode(json_str))

# Google Sheets API 및 Google Drive API 설정
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/spreadsheets.readonly", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_data, scope)
client = gspread.authorize(creds)

# Google Sheets 연결
sheet = client.open('patientEdu').sheet1

# 데이터 로드
try:
    data = sheet.get_all_records()
except gspread.exceptions.GSpreadException:
    data = []

# Streamlit 애플리케이션
st.title("커뮤니티")

# 게시물 작성하기 버튼을 오른쪽으로 이동
_, button_col = st.columns([3, 1])
with button_col:
    st.button("게시물 작성하기", on_click=lambda: setattr(st.session_state, 'show_form', True), type='primary')

if 'show_form' not in st.session_state:
    st.session_state.show_form = False

if st.session_state.show_form:
    st.write("")
    with st.form(key='new_post_form', clear_on_submit=True):
        st.header("새 게시물 작성")
        title = st.text_input("제목")
        content = st.text_area("내용")
        password = st.text_input("게시물 비밀번호", type="password")
        submit_button, cancel_button = st.columns(2)
        with submit_button:
            submit = st.form_submit_button("게시물 작성", type='primary')
        with cancel_button:
            cancel = st.form_submit_button("취소")

        if submit:
            if title and content and password:
                sheet.append_row([title, content, password])
                st.success("게시물이 작성되었습니다.")
                st.session_state.show_form = False
                st.rerun()
            else:
                st.error("제목, 내용 및 비밀번호를 모두 입력하세요.")
        if cancel:
            st.session_state.show_form = False

st.markdown("---")

# 게시물 표시 및 수정/삭제 기능 추가
st.subheader("게시물 목록", divider="rainbow")

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)  # 공간 추가

for i, row in enumerate(data):
    cols = st.columns([8, 2])
    with cols[0]:
        st.markdown(f"##### {row.get('제목', '제목 없음')}")
    with cols[1]:
        if st.button("내용 보기", key=f"view_button_{i}"):
            st.write(f'<meta http-equiv="refresh" content="0; url=/post?post_id={i}">', unsafe_allow_html=True)
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)  # 각 게시물 사이에 공간 추가
    st.markdown("---")

