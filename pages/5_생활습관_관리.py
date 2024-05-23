import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)
st.title("뇌졸중 환자의 생활습관 관리")


with st.container(border=True):
    st.write(
        """
        :red[뇌졸중은 재발이 흔한 질환이므로, 이를 예방하는 것이 중요합니다!]
        """
    )

st.image('./static/life1.png', caption='뇌졸중 재발률')

with st.container(border=True):
    st.write(
        """
        - 재발한 뇌졸중은 처음 발생한 경우보다 심한 후유증이 남고 더 치명적입니다.
        - 꾸준히 치료를 받으면서 처방받은 약물을 복용하고, 생활습관을 개선하면 뇌졸중 재발을 예방할 수 있습니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.header('고혈압, 당뇨병, 이상지질혈증 관리', divider='blue')
with st.container(border=True):
    st.write(
        """
        - 이러한 병력이 있는 경우, 정기적으로 병원을 방문하여 혈압, 혈당, 콜레스테롤 수치를 측정하고 약물 조절을 해야 합니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.subheader('고혈압 관리', divider='blue')
with st.container(border=True):
    st.write(
        """
        - 고혈압을 치료하지 않고 방치하면 혈관벽이 두꺼워지고 혈관이 점차 좁아지다가 막히는 죽상동맥경화증이 발생합니다.
        - 고혈압 예방과 치료를 위해 식이요법(저염식, 저지방식이), 운동요법이 권고되며 필요한 경우 약물치료를 병행해야 합니다.
        """
    )

st.image('./static/life2.png', caption='정상 혈압 범위')

st.divider()  # 👈 Draws a horizontal rule

st.subheader('당뇨병 관리', divider='blue')
with st.container(border=True):
    st.write(
        """
        - 뇌졸중 재발을 예방하기 위해서는 반드시 조절 목표에 맞게 혈당을 조절해야 합니다.
        - 담당 의사와 혈당 조절 목표를 정한 후 생활습관을 개선하고 필요 시 약물치료를 꾸준히 시행해야 합니다.
        """
    )
st.image('./static/life3.jpeg')
st.image('./static/life4.png', caption='정상 혈당 범위')

st.divider()  # 👈 Draws a horizontal rule

st.subheader('이상지질혈증 관리', divider='blue')
with st.container(border=True):
    st.write(
        """
        - 총콜레스테롤과 LDL(저밀도 지단백)-콜레스테롤이 높은 채로 치료하지 않으면 콜레스테롤이 혈관벽에 쌓여 뇌졸중이 재발될 수 있습니다.
        - 담당의사와 상의하여 콜레스테롤 조절 목표와 치료 계획을 세우고 꾸준히 관리하여야 합니다.
        """
    )
st.image('./static/life5.png')

st.divider()  # 👈 Draws a horizontal rule

st.header('체중관리', divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - 비만과 복무비만은 고혈압과 당뇨병, 이상지질혈증의 위험을 증가시켜 뇌졸중 재발위험을 높입니다.
        - 자신의 체질량지수와 허리둘레, 비만의 기준을 정확히 알고 목표를 세워 관리해야 합니다.
        - 적정 제충과 적정 허리둘레를 유지해야 합니다.
        - 규칙적인 식사와 함께 매일 30분 이상의 운동이 좋습니다.
        """
    )

st.subheader('비만과 복부비만의 기준', divider='blue')
st.image('./static/life6.png')
st.image('./static/life7.png')


st.divider()  # 👈 Draws a horizontal rule

st.header('규칙적인 운동', divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - 규칙적인 운동은 혈압 강하, 체중 감량, 콜레스테롤 감소 등을 통해 뇌졸중 재발 위험을 낮춰줍니다.
        - 뇌졸중 환자는 힘을 주는 운동보다는 걷기, 달리기, 자전거 타기, 수영 등 지속적인 운동이 도움이 됩니다.
        """
    )
st.image('./static/life8.png')
st.image('./static/life9.png',caption="운동별 적정 시간")
st.image('./static/life10.png')

st.divider()  # 👈 Draws a horizontal rule

st.subheader('뇌졸중 환자 운동 시 주의사항', divider='blue')
st.image('./static/life11.png')
st.image('./static/life12.png')

st.divider()  # 👈 Draws a horizontal rule

st.header('식이요법',divider='rainbow')
st.subheader('뇌졸중 환자를 위한 식사지침',divider='blue')
st.image('./static/life13.png')

st.divider()  # 👈 Draws a horizontal rule

st.subheader('소금섭취 줄이기',divider='blue')
with st.container(border=True):
    st.write(
        """
        - 소금은 더 많은 수분을 혈액 안으로 끌어들여 심장에 부담을 줍니다.
        - 하루 소금섭취량을 5g(나트륨 2,000mg)이하로 제한하여야 합니다.
        """
    )
st.image('./static/life14.png')
st.image('./static/life15.png')

st.divider()  # 👈 Draws a horizontal rule

st.subheader('콜레스테롤 낮추는 식사방법',divider='blue')

st.image('./static/life16.png')
st.image('./static/life17.png')

st.divider()  # 👈 Draws a horizontal rule

st.header('금연',divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - :red[담배는 뇌졸중의 강력한 위험요인입니다.]
        - 담배의 니코틴은 말초혈관을 수축하고 심박수를 증가시켜 혈압을 상승시킵니다.
        - 혈관 손상을 유발하여 죽상동맥경화증과 혈전(핏덩이)형성을 촉진해서 뇌졸중 발생 위험이 높아집니다.
        - 뇌졸중 재발을 방지하기 위해서는 반드시 담배를 끊어야 하며, 간접흡연 역시 뇌졸중의 위험요인이므로 반드시 피해야 합니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.subheader('금연을 위한 올바른 행동습관',divider='blue')

st.image('./static/life18.png')

with st.container(border=True):
    st.write(
        """
        :blue[기관의 도움 받기]

        흡연은 니코틴 중독이므로 혼자서 금연에 성공하기는 어렵습니다. 금연 클리닉이나 병원을 방문하면 전문가의 도움을 받을 수 있습니다.
        """
    )

st.image('./static/life19.png')


st.divider()  # 👈 Draws a horizontal rule

st.header('스트레스 관리', divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - 과도한 스트레스는 혈압을 상승시키고 과음, 흡연으로 이러져 뇌졸중 재발 위험을 높이므로 스트레스를 잘 관리해야 합니다.
        - 뇌졸중 후에는 신체적 손상과 삶의 변화로 불안, 우울, 분노 등 감정변화를 경험할 수 있습니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.subheader('뇌졸중 후 불안, 우욱 극복하는 법', divider='blue')
st.image('./static/life20.png')
st.image('./static/life21.png')
