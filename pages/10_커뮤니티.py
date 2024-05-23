import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import base64

# Base64로 인코딩된 JSON 키 파일을 secrets에서 가져오기
json_str = st.secrets["general"]["GOOGLE_CREDENTIALS"]
json_data = json.loads(base64.b64decode(json_str))

# Google Sheets API 및 Google Drive API 설정
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
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



# 게시물 작성하기 버튼
if 'show_form' not in st.session_state:
    st.session_state.show_form = False

def show_form_callback():
    st.session_state.show_form = True

def hide_form_callback():
    st.session_state.show_form = False

st.button("게시물 작성하기", on_click=show_form_callback)

if st.session_state.show_form:
    st.header("새 게시물 작성")
    title = st.text_input("제목")
    content = st.text_area("내용")
    if st.button("게시물 작성"):
        if title and content:
            sheet.append_row([title, content, ""])
            st.success("게시물이 작성되었습니다.")
            hide_form_callback()  # Hide form after submission
            st.rerun()  # Query params 초기화하여 새로고침
        else:
            st.error("제목과 내용을 모두 입력하세요.")
    if st.button("취소", on_click=hide_form_callback):
        st.session_state.show_form = False

st.divider()  # 👈 Draws a horizontal rule

# 게시물 표시
for i, row in enumerate(data):
    cols = st.columns([8, 2])
    with cols[0]:
        st.write(row.get('제목', '제목 없음'))
    with cols[1]:
        if st.button("내용 보기", key=f"view_button_{i}"):
            st.session_state['post_id'] = str(i) # 쿼리 매개변수를 설정하여 리디렉션
            st.query_params["post_id"]=str(i)
            st.write(f'<meta http-equiv="refresh" content="0; url=/post?post_id={i}">', unsafe_allow_html=True)
    st.markdown("---")  # 구분선 추가