import streamlit as st

st.set_page_config(
    page_title="뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)
st.title("뇌졸중의 위험요인🫡")
import streamlit as st


st.markdown(
    """
- 뇌경색 위험요인은 크게 조절할 수 없는 위험요인과 조절할 수 있는 위험요인으로 구분할 수 있습니다.

- 조절할 수 있는 위험요인을 찾아 생활습관을 개선하고 약물을 규칙적으로 복용하며 
꾸준히 관리하면 뇌경색을 예방할 수 있습니다.
    """
)

st.image('./static/risk_1.png', caption='뇌졸중의 위험요인')


st.header('교정 불가능한 요인', divider='rainbow')
st.markdown(
    """
    #### 연령
    - 연령이 높을수록 혈관벽이 손상되어 동맥경화가 생기므로 뇌졸중에 걸릴 확률이 높아집니다.
    """
)
st.divider()  # 👈 Draws a horizontal rule
st.markdown(
    """
    #### 가족력
    - 혈연관계에 있는 가족, 친지가 뇌졸중을 앓은 경우, 뇌졸중에 걸릴 유전적 확률이 높아집니다.
    """
)


st.header('교정 가능한 요인', divider='rainbow')
st.markdown("#### 고혈압")
with st.container(border=True):
    st.write(
        """
        :red[뇌졸중 환자의 50~70%가 고혈압 환자입니다.]  
        """
    )
st.markdown(":blue[권장혈압:120/80mmHg 이하]")
    
st.image('./static/mosanKrvFM.png', caption='고혈압과 뇌졸중의 관련성')

st.divider()  # 👈 Draws a horizontal rule

st.markdown("#### 당뇨병")
with st.container(border=True):
    st.write(":red[당뇨병 환자는 정상인보다 2-3배 정도 뇌졸중에 잘 걸립니다.] ")
st.markdown("- 당뇨병이 있는 뇌졸중 환자는 다른 뇌졸중 환자에 비해 사망률이 높고, 뇌졸중 증상의 회복이 느리며 재발이 더 잘 됩니다.")

st.image('./static/diabetes.png', caption='당뇨병이 심혈관에 미치는 영향')

st.divider()  # 👈 Draws a horizontal rule


st.markdown("#### 고지혈증")
with st.container(border=True):
    st.write(":red[고지혈증은 동맥경화, 특히 심장병(관상동맥질환)을 일으키는 주요 원인이 됩니다.] ")


with st.container(border=True):
    st.write(
        """
        :blue[고지혈증 : 우리 몸의 혈액에 지방질이 너무 많은 형태]  
        *지방질이란? 콜레스테롤, 중성지방, 유리지방산 등의 지방성 물질
        """
    )
st.markdown(
    """
    -  동맥경화에서 중요하게 여기는 것은 특히 콜레스테롤입니다. 뇌졸중도 뇌혈관의 동맥경화에 의해 생기므로 고지혈증은 동맥경화에 의한 뇌경색의 위험요인이 됩니다.
    """
)
st.divider()  # 👈 Draws a horizontal rule

st.markdown("#### 심장병")
with st.container(border=True):
    st.write(":red[심장질환은 뇌경색의 주요 원인입니다.]")
st.image('./static/mosaVfij3r.png', caption='심장질환에서의 혈전')

st.divider()  # 👈 Draws a horizontal rule

st.markdown(
    """
    #### 뇌졸중의 기타 위험 요인
    """
)
st.image('./static/mosaiHffG2.png', caption='기타 위험 요인')