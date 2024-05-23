import streamlit as st

st.set_page_config(
    page_title="뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)
st.title("뇌졸중의 증상과 대처방법")




st.header('뇌졸중의 증상', divider='rainbow')
with st.container(border=True):
    st.image('./static/sym1.png')
    st.image('./static/sym2.png')
    st.image('./static/sym3.png')
    st.image('./static/sym4.png')
    st.image('./static/sym5.png')


st.header('뇌졸중 증상이 나타났을 때 대처법', divider='rainbow')
st.markdown(
    """
- 뇌졸중은 치료에 있어서 골든타임이 매우 중요합니다.
- 뇌졸중이 의심되면 전문 치료 병원으로 최대한 빨리 이송하여야 합니다.
    """
)
st.image('./static/sym6.png', caption='뇌졸중 발생 시 프로토콜')
st.image('./static/sym7.png', caption='뇌졸중 증상이 사라졌는데요?')

st.header('의식장애 시 행동요령', divider='rainbow')

st.markdown("### 🟢이렇게 해주세요!🟢")
st.image('./static/sym8.png',width=500)
st.markdown(
    """
- 조이는 옷을 느슨하게 해주세요.
- 기도가 막히지 않도록 환자를 편하게 해주세요.
- 구토하는 경우, 기도로 음식물이 들어갈 수 있으므로 얼굴을 옆으로 돌려주시고 입 안을 닦아주세요.
    """
)


st.markdown("### ❌이렇게 하면 안돼요!❌")
st.image('./static/sym9.png',width=500)
st.markdown(
    """
- 정신 차리게 하려고 찬물을 끼얹거나 뺨을 때리면 안됩니다.
- 뇌졸중이 발생한 사람의 손끝을 따거나 침을 놓으면 안됩니다.
- 의식이 뚜렷하지 않은 환자에게 물이나 약을 먹이면 안됩니다.
    """
)
