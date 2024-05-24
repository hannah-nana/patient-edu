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

@st.experimental_dialog("게시물 수정")
def edit_post():
    password_input = st.text_input("비밀번호", type="password", key="edit_password_input")
    if st.button("확인", key="confirm_edit_post"):
        if password_input.strip() == str(row['게시물 비밀번호']).strip():
            new_title = st.text_input("제목", value=row['제목'], key="edit_title")
            new_content = st.text_area("내용", value=row['내용'], key="edit_content")
            new_password = st.text_input("새 비밀번호", type="password", value=str(row['게시물 비밀번호']), key="edit_new_password")
            if st.button("수정", key="edit_confirm_button"):
                sheet.update_cell(post_id + 2, 1, new_title)
                sheet.update_cell(post_id + 2, 2, new_content)
                sheet.update_cell(post_id + 2, 3, new_password)  # 게시물 비밀번호 열 업데이트
                st.success("게시물이 수정되었습니다.")
                st.rerun()
        else:
            st.error("비밀번호가 일치하지 않습니다.")

@st.experimental_dialog("게시물 삭제")
def delete_post():
    password_input = st.text_input("비밀번호", type="password", key="delete_password_input")
    if st.button("확인", key="confirm_delete_post"):
        if password_input.strip() == str(row['게시물 비밀번호']).strip():
            sheet.delete_rows(post_id + 2)
            st.success("게시물이 삭제되었습니다.")
            st.write('<meta http-equiv="refresh" content="0; url=/커뮤니티">', unsafe_allow_html=True)
            st.rerun()
        else:
            st.error("비밀번호가 일치하지 않습니다.")

@st.experimental_dialog("댓글 삭제")
def delete_comment(comment_idx, pw):
    password_input = st.text_input("비밀번호", type="password", key=f"delete_password_input_{comment_idx}")
    if st.button("확인", key=f"confirm_delete_comment_{comment_idx}"):
        if password_input.strip() == pw.strip():
            comments.pop(comment_idx)
            passwords.pop(comment_idx)
            updated_comments = "\n".join(comments)
            updated_passwords = "\n".join(passwords)
            sheet.update_cell(post_id + 2, 4, updated_comments)
            sheet.update_cell(post_id + 2, 5, updated_passwords)
            st.success("댓글이 삭제되었습니다.")
            st.rerun()

@st.experimental_dialog("댓글 작성하기")
def add_comment():
    comment = st.text_input("댓글 내용", placeholder="댓글을 작성하기", key="comment_input")
    comment_password = st.text_input("비밀번호", type="password", key="comment_password_input")
    if st.button("댓글 작성", key="comment_button"):
        if comment and comment_password:
            comments = str(row.get('댓글', ""))
            if comments:
                comments += f"\n{comment}"
            else:
                comments = f"{comment}"
            passwords = str(row.get('댓글 비밀번호', ""))
            if passwords:
                passwords += f"\n{comment_password}"
            else:
                passwords = f"{comment_password}"
            sheet.update_cell(post_id + 2, 4, comments)  # 첫 번째 행은 헤더이므로 post_id + 2
            sheet.update_cell(post_id + 2, 5, passwords)  # 댓글 비밀번호 열 업데이트
            st.success("댓글이 작성되었습니다.")
            st.rerun()  # 페이지 새로고침
        else:
            st.error("댓글 내용 및 비밀번호를 입력하세요.")

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

            # 버튼 생성 및 dialog 호출
            cols = st.columns([3.5, 1, 1])
            with cols[1]:
                if st.button("게시물 수정"):
                    edit_post()
            with cols[2]:
                if st.button("게시물 삭제"):
                    delete_post()

            st.header(row.get('제목', '제목 없음'), divider="violet")
            st.write(row.get('내용', '내용 없음'))

            st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)  # 공간 추가

            # 댓글 표시
            st.subheader("댓글창",divider="orange")
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)  # 공간 추가

            # "댓글 작성하기" 버튼을 댓글창과 댓글 사이에 배치
            cols = st.columns([4, 1])
            with cols[1]:
                if st.button("댓글 작성하기"):
                    add_comment()

            st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)  # 공간 추가

            comments = str(row.get('댓글', "")).split('\n')
            passwords = str(row.get('댓글 비밀번호', "")).split('\n')
            for idx, comment in enumerate(comments):
                if comment.strip():
                    pw = passwords[idx] if idx < len(passwords) else ''
                    with st.container():
                        cols = st.columns([8, 1])
                        with cols[0]:
                            st.write(comment)
                        with cols[1]:
                            if st.button("삭제", key=f"delete_comment_{idx}"):
                                delete_comment(idx, pw)
                    st.markdown("---")

            if st.button("목록으로 돌아가기"):
                st.write('<meta http-equiv="refresh" content="0; url=/커뮤니티">', unsafe_allow_html=True)
                st.rerun()
        else:
            st.error("유효하지 않은 게시물 ID입니다.")
            st.write('<meta http-equiv="refresh" content="0; url=/커뮤니티">', unsafe_allow_html=True)
            st.rerun()
    except IndexError:
        st.error("유효하지 않은 게시물 ID입니다.")
        st.write('<meta http-equiv="refresh" content="0; url=/커뮤니티">', unsafe_allow_html=True)
        st.rerun()
else:
    import streamlit as st
    st.error('왼쪽 사이드 바에서 "커뮤니티"를 클릭해보세요!', icon="👈")
