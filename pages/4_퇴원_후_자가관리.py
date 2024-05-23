import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)
st.title("퇴원 후 자가관리")

st.header('정맥 내 혈전용해제', divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - 뇌경색이 한 번 발생한 사람은 뇌혈관에 손상 흔적이 남아, 뇌경색이 재발할 확률이 높습니다.
        - 급성기 치료가 끝나면 혈전 생성을 억제하는 항응고제나 항혈전제를 평생 복용해야 합니다.
        - 뇌경색의 위험요인인 고혈압, 당뇨병, 이상지질혈증이 동반된 환자들은 이를 치료하게 위해 약물을 복용합니다.
        """
    )


st.subheader('뇌졸중 약물의 종류', divider='blue')
st.image('./static/self1.png', caption='약물의 종류')
st.image('./static/self2.png', caption='약물 주의사항')

st.divider()  # 👈 Draws a horizontal rule

st.subheader('항혈소판제', divider='blue')
with st.container(border=True):
    st.write(
        """
        - 항혈소판의 응집 작용을 방해하여 혈관에 혈전이 생기는 것을 막아줍니다.
        - 항혈소판제를 복용함으로써 뇌경색의 재발과 심혈관 질환 발생을 예방할 수 있습니다.
        """
    )
st.image('./static/self3.png')
st.image('./static/self4.png', caption='항혈소판제 복용 시 주의사항')

st.divider()  # 👈 Draws a horizontal rule

st.subheader('항응고제', divider='blue')
with st.container(border=True):
    st.write(
        """
        - 혈액응고인자의 작용을 억제하여 피를 묽게 유지하고, 혈전이 생기지 않도록 하는 약물입니다.
        - 특히, 심방세동에 의한 뇌경색인 경우 항응고제를 지속적으로 복용하여 혈전이 생기는 것을 방지해야 합니다.
        - 항응고제는 와파린과 직접경구항응고제로 구분됩니다.
        """
    )
st.image('./static/self5.png',caption="올바른 와파린 복용법")
st.image('./static/self6.png', caption='와파린 복용 시 주의사항')
st.image('./static/self7.png', caption='비-비타민K 길항제')


st.header('휴유증과 재활', divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - 뇌졸중의 발생 부위에 따라 다양한 후유증이 남을 수 있습니다.
        - 뇌졸중 환자의 73%는 재활이 필요하며, 9%는 사망하고 18%는 완전히 회복합니다.
        """
    )

st.subheader('뇌졸중 후유증', divider='blue')
st.image('./static/self8.png',caption="뇌졸중의 후유증")
with st.container(border=True):
    st.write(
        """
        - 뇌졸중 이후에 발생하는 후유증은 약물치료, 재활치료, 보조기 등으로 상당부분 극복할 수 있습니다.
        - 뇌졸중의 후유증은 수 년에 걸쳐 호전되는 경우가 많습니다.
        - 포기하지 말고 적절한 치료를 계속하여야 합니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.subheader('뇌졸중 재활', divider='blue')
with st.container(border=True):
    st.write(
        """
        - :red[뇌졸중으로 인한 장애를 최소화하고 신체기능을 회복하여 가족과 사회로 복귀하고 삶의 질을 향상시키기 위한 재활치료입니다.]
        - 뇌졸중 재활은 재활의학과 전문의, 신경과 전문의, 재활간호사, 물리치료사, 작업치료사, 언어재활사, 사회복지사 등 다양한 분야의 전문가들이 함께 합니다.
        """
    )
st.image('./static/self10.png',caption="뇌졸중의 재활치료")

st.header('합병증 예방', divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - 뇌졸중 이후 욕창, 낙상, 관절 구축 등 다양한 합병증이 생길 수 있습니다.
        - 체계적인 관리를 통해 합병증의 발생을 예방함으로써, 기능 회복이 제한되는 것을 방지할 수 있습니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.subheader('뇌졸중 합병증별 예방법', divider='blue')
st.image('./static/after1.png')

st.image('./static/self11.png',caption="욕창")
with st.container(border=True):
    st.write(
        """
        - 적어도 2시간마다 환자의 자세 변경과 함께 등마사지를 시행합니다. 
        - 이어 매트리스를 사용합니다.
        - 피부는 건조하고 청결하게 유지해야 합니다.
        - 충분한 영양섭취를 해야 합니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.image('./static/after2.png')

st.image('./static/self12.png',caption="낙상")
with st.container(border=True):
    st.write(
        """
        - 보행 시 서두르지 않고, 주변을 살피는 습관을 가져야 합니다.
        - 발에 잘 맞는 운동화를 착용하고, 지팡이 등 보조기구를 사용합니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.image('./static/after3.png')

st.image('./static/self13.png',caption="관절 구축")
with st.container(border=True):
    st.write(
        """
        - 올바른 자세를 유지하고 매일 수 차례 관절운동을 시행해야 합니다.
        - 관절부위에 통증이나 부종이 발생 시 재활의학과를 방문해야 합니다.
        """
    )

st.divider()  # 👈 Draws a horizontal rule

st.image('./static/after4.png')

st.image('./static/self14.png',caption="배죠 장애")
with st.container(border=True):
    st.write(
        """
        - 규칙적으로 세 끼 식사를 하고, 물을 자주 마십니다. 
        - 섬유소가 많은 사과, 샐러드, 양배추 등을 충분히 섭취합니다.
        - 복부마사지를 시행합니다.
        """
    )