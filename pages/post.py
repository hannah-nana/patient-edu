import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import base64

# Base64로 인코딩된 JSON 키 파일을 secrets에서 가져오기
json_str = st.secrets["GOOGLE_CREDENTIALS"]
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



query_params = st._get_query_params()
if 'post_id' in query_params:
    try:
        post_id = int(query_params['post_id'][0])
        if post_id < len(data):
            row = data[post_id]

            st.header(row.get('제목', '제목 없음'), divider="rainbow")

            st.write(row.get('내용', '내용 없음'))


            st.subheader("댓글 작성하기", divider="blue")

            # 댓글 작성
            comment = st.text_input("",placeholder="댓글을 작성하기", key="comment_input")
            if st.button("댓글 작성", key="comment_button"):
                if comment:
                    comments = row.get('댓글', "")
                    comments = comments + f"\n{comment}"
                    sheet.update_cell(post_id + 2, 3, comments)  # 첫 번째 행은 헤더이므로 i + 2
                    st.success("댓글이 작성되었습니다.")
                    st.rerun()  # 페이지 새로고침
                else:
                    st.error("댓글 내용을 입력하세요.")

            st.subheader("댓글창", divider="blue")

            # 댓글 표시
            comments = row.get('댓글', "").split('\n')
            for comment in comments:
                if comment.strip():  # 빈 문자열이 아닌 경우에만 출력
                    st.write(comment)
                    st.divider()

            if st.button("목록으로 돌아가기"):
                del st.session_state['post_id']  # 세션 상태에서 post_id 삭제
                st.rerun()
        else:
            st.error("유효하지 않은 게시물 ID입니다.")
    except IndexError:
        st.error("유효하지 않은 게시물 ID입니다.")
else:
    st.error("게시물을 찾을 수 없습니다.")