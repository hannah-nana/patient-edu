import streamlit as st

st.set_page_config(
    page_title="뇌졸중 바로알기",
    page_icon="./static/thumbnail.jpg"
)
st.title("뇌졸중 치료방법")

with st.container(border=True):
    st.write(
        """
        - 뇌경색 치료에서 가장 중요한 것은 최대한 빨리 병원에 도착하는 것입니다.
        - 뇌경색 초급성기에는 뇌혈관을 막고 있는 혈전을 약물로 녹이는 치료가 필요한데, 이 치료는 시간이 많이 지나면 시행할 수 없습니다.  
        """
    )


st.header('정맥 내 혈전용해제', divider='rainbow')
with st.container(border=True):
    st.write(":blue[증상 발생 후 3~4.5시간 이내에 시행!]")
with st.container(border=True):
    st.write(
        """
        - 정맥 혈관을 통해 혈전 용해제를 투여합니다.
        - :red["약물로 뇌혈관을 막고 있는 혈전(핏덩이)를 녹여 막힌 혈관을 뚫어줍니다."]
        - 간단하게 투여할 수 있지만, 뇌혈관 혈전 외의 다른 곳에서 작용하여 출혈이 발생할 수 있고, 혈관의 재개통 여부를 즉각적으로 확인하기 어렵습니다. 
        """
    )
st.image('./static/cure1.jpeg', caption='혈전용해제')

st.divider()  # 👈 Draws a horizontal rule

st.header('동맥 내 혈전용해술', divider='rainbow')
with st.container(border=True):
    st.write(":blue[증상 발생 후 6~24시간 이내에 시행!]")
with st.container(border=True):
    st.write(
        """
        - :red["뇌혈관조영술을 통해 막힌 뇌혈관ㅇ르 직접 확인한 후, 그 부위에 도관을 삽입하여 혈전용해제를 투여하거나, 혈전 제거용 도관을 이용해 혈전을 밖으로 꺼내는 치료방법 입니다."]
        - 막힌 혈관을 직접 눈으로 확인하면서 약물을 투여하거나 시술을 진행하여, 혈관 개통여부를 바로 확인할 수 있습니다.
        - 뇌 영상에서 막힌 혈관이 보이지 않거나, 뇌경색의 크기가 큰 경우에는 출혈 위험이 있어서 시행하지 않습니다.
        """
    )
st.image('./static/cure2.png', caption='동맥 내 혈전용해술')
st.image('./static/cure3.png', caption='증상 발생 후 24시간이 지났어요')

st.divider()  # 👈 Draws a horizontal rule

st.header('뇌혈관 치료', divider='rainbow')
st.image('./static/cure4.png', caption='뇌혈관 수술 종류')

st.divider()  # 👈 Draws a horizontal rule

st.header('목동맥(경동맥) 협착증 치료', divider='rainbow')
with st.container(border=True):
    st.write(
        """
        - 아래 치료들은 목동맥(경동맥)이 좁아진 환자들에게 시행합니다.
        - 혈관의 좁아진 정도, 증상 여부에 따라 치료 방법을 결정합니다.
        """
    )
st.image('./static/cure5.png', caption='경동맥 수술 종류')

