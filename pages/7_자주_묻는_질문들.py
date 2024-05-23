import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(
    page_title="뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)

st.title("자주 묻는 질문들")

# FAQ 항목 1
with st.expander(expanded=True,label=":blue[Q. 뇌졸중은 호전될 수 있는 병인가요? (팔다리를 다시 움직일 수 있을까요?)]"):
    st.write("""
     A. 손상된 뇌조직을 회복시킬 수는 없습니다. 하지만 손상된 부위의 역할을 이전에는 사용하지 않던  다른 부분의 뇌에서 대신하게 할 수 있습니다. 뇌의 회복력은 뇌졸중 발병 후 처음 3개월에서 6개월까지 가장 활발하게 일어나기 때문에 꾸준히 재활 치료를 하는 것이 중요합니다. 일반적으로 뇌졸중 환자 중 40~65%는 6개월쯤에 독립적인 생활이 가능합니다.
    """)

# FAQ 항목 2
with st.expander(expanded=True,label=":blue[Q.치료에는 시간이 어느 정도 걸리나요?]"):
    st.write("""
    A. 일반적으로 뇌졸중 환자는 급성기를 무사히 지나고 나서 서서히 회복되어 가는 경과를 보입니다. 재활 치료는 환자의 증상마다 다르지만 보통 6개월 정도 소요됩니다. 환자의 노력과 지속적인 재활 치료를 통하여 수 년 후까지도 신체 기능이 회복될 수도 있습니다.
    """)

# FAQ 항목 3
with st.expander(expanded=True,label=":blue[Q.뇌졸중이 재발할 수 있나요?]"):
    st.write("""
    A.네, 그렇습니다. 전체 뇌졸중 환자 중 약 25%에서 뇌졸중이 재발하며, 여성보다 남성에게서 재발이 더 많습니다.
    """)

# FAQ 항목 4
with st.expander(expanded=True,label=":blue[Q.뇌졸중 발생 시 할 수 있는 응급조치는 무엇인가요?]"):
    st.write("""
    A.집에서 할 수 있는 응급조치는 없습니다. 가능한 한 빨리 119에 연락하여 뇌졸중 전문 치료 병원으로 이송하는 것이 가장 정확하고 확실한 응급조치입니다.
    """)

# FAQ 항목 5
with st.expander(expanded=True,label=":blue[Q.뇌졸중 후 운전할 수 있나요?]"):
    st.write("""
    A. 뇌졸중 치료 후 후유증에 따라 다릅니다. 본인의 건강 상태와 후유증에 따라 운전 가능 여부가 다를 수 있으므로 운전하기 전 담당 의사와 상의해야 합니다.
    """)

# FAQ 항목 6
with st.expander(expanded=True,label=":blue[Q.뇌졸중 환자는 고기를 먹으면 안 되나요?]"):
    st.write("""
    A. 뇌졸중 환자가 피해야 할 음식은 없습니다. 단, 고기 섭취 시 기름 부위는 제거하고 살코기 위주로 드시는 것이 좋습니다.
    """)

# FAQ 항목 7
with st.expander(expanded=True,label=":blue[Q.짜게 먹으면 뇌졸중에 잘 걸리나요?]"):
    st.write("""
    A. 그렇습니다. 음식을 짜게 먹으면 고혈압을 유발할 수 있어 결국 뇌졸중 발병 확률이 높아집니다.
    """)

# FAQ 항목 8
with st.expander(expanded=True,label=":blue[Q.뇌졸중 환자가 커피를 마셔도 되나요?]"):
    st.write("""
    A. 커피와 뇌졸중 발생의 관계는 특별히 알려진 바가 없기 때문에 뇌졸중 환자라 하더라도 하루 1~2잔 정도의 커피는 드셔도 괜찮습니다. 다만 고지혈증이나 당뇨가 있는 경우, 설탕과 지방이 포함된 믹스커피보다 블랙커피를 마시는 것이 좋습니다.
    """)

