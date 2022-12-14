from textwrap import fill
import streamlit as st
import pandas as pd
import json
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import pathlib
from PIL import Image

#set page config
st.set_page_config(page_title="Streamlit Dashboard", page_icon=":tada:", layout="wide", initial_sidebar_state="expanded")

#create a title and center it
st.title("Musicians vs Cancel Culture")

st.markdown(
"""
<style>
.st-fo {
    width:400px;
    position: center
}
</style>
""",
unsafe_allow_html=True
)


design1 = st.select_slider('', options=['Individual Artist', 'Compare Artists'])

if design1 == 'Individual Artist':
    url = 'https://raw.githubusercontent.com/srs366/musicians_v_cancellation/master/scripts/streamlit/Artist_data.json'

    response = requests.get(url)

    js = json.loads(response.text)

    st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
    selected_gender = st.radio('', ['All','Male', 'Female'],index=0)
    js_gender = {}
    if selected_gender == "All":
        js_gender = js
    else:
        for key in js.keys():
            if js[key]["Gender"] == selected_gender:
                js_gender[key] = js[key]

    #reason for cancellation selectbox
    js = {}
    selected_reason = st.selectbox('Reason for Cancellation:', ['All', 'Covid related', 'Political', 'Hate crime', 'Assault', 'Race related','Negligence','Sex crime','Negligence'], index = 0)
    if selected_reason == "All":
        js = js_gender
    else:
        for key in js_gender.keys():
            if js_gender[key]["cancellation category"] == selected_reason:
                js[key] = js_gender[key]

    #create a selectbox
    selectbox1 = st.selectbox("Select a musician", [''] + sorted(list(js.keys())))
    if selectbox1 != '':
        prof_pic=js[selectbox1]["Image"] #show image
        #show the details
        text= f'''&emsp;&emsp;&emsp;<b>Name:</b> &ensp;{selectbox1}
        <br>&emsp;&emsp;&emsp;<b>Gender:</b> &ensp;{js[selectbox1]["Gender"]}
        <br>&emsp;&emsp;&emsp;<b>Race:</b> &ensp;{js[selectbox1]["Race"]}
        <br>&emsp;&emsp;&emsp;<b>Age:</b> &ensp;{(int(js[selectbox1]['Age']))}
        <br>&emsp;&emsp;&emsp;<b>Nationality:</b> &ensp;{js[selectbox1]['Nationality']}
        <br>&emsp;&emsp;&emsp;<b>Debut Year:</b> &ensp;{js[selectbox1]['Debut year']}
        <br>&emsp;&emsp;&emsp;<b>Genre:</b> &ensp;{js[selectbox1]['Genre']}
        <br>&emsp;&emsp;&emsp;<b>Cancellation Date:</b> <br>&emsp;&emsp;&emsp;{datetime.strptime(js[selectbox1]['Date of Cancellation'], '%Y-%m-%d').strftime('%d %B %Y')}
        <br>&emsp;&emsp;&emsp;<b>Category:</b> &ensp;{js[selectbox1]["cancellation category"]}'''

        st.markdown(
        """
        <style>
        .container {
            display: flex;
            margin: auto;
            width: 50%;
            /*background-color: red;*/
        }
        .reason {
            display: flex;
            margin: auto;
            height: 100px;
            /*background-color: red;*/
        }
        .logo-text {
            font-size:18px
        }
        .logo-img {
            float:right;
            height:275px
        }
        </style>
        """,
        unsafe_allow_html=True
        )

        st.markdown(
        f"""
        <div class="container">
            <img class="logo-img" src="{prof_pic}">
            <p class="logo-text">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
        )

        reason = f'<b>Reason for Cancellation:</b> &ensp;{js[selectbox1]["Reason for cancellation"]}'
        st.markdown(f'''
        <div class="reason">
            <p class="logo-text">{reason}</p>
        </div>
        ''',
        unsafe_allow_html=True)

        #PLOTLY
        base_path = pathlib.Path(__file__).resolve().parent
        artist_path = f'{js[selectbox1]["CHARTMETRIC ID"]}_merged_data.csv'
        full_path = base_path.joinpath(base_path, "streamlit_data", artist_path)
        data = pd.read_csv(full_path, parse_dates=[0], index_col=0)
        data_album = data[data["New_Music"]==1]
        data_tv = data[data["TV_Show"]==1]
        fig_spot =make_subplots(specs=[[{"secondary_y":True}]],column_widths=[600],subplot_titles=[f"{selectbox1}'s Cancellation Data"])
        fig_spot.add_trace(go.Scatter(x=data.index, y=data.monthly_listeners, mode='lines',line=dict(color='green',width=2),name='Spotify'),secondary_y=False)
        fig_spot.add_trace(go.Scatter(x=data.index, y=data.TweetSentiment_Negative, mode='none',line=dict(color='red',width=1),name='Negative Tweet',fill='tonexty'),secondary_y=True)
        #radio line
        fig_spot.add_trace(go.Scatter(x=data.index, y=data.monthly_spins, mode='lines',line=dict(color='#1599eb',width=1),name='Radio'),secondary_y=False)
        fig_spot.add_trace(go.Scatter(x=data_album.index, y=data_album.monthly_listeners, mode='markers',marker_size=7,marker_line_color="midnight blue",marker_color="lightskyblue",marker_line_width=2,name='Music Release'),secondary_y=False)
        fig_spot.add_trace(go.Scatter(x=data_tv.index, y=data_tv.monthly_listeners, mode='markers',marker_symbol="x",marker_size=7,marker_line_color="midnight blue",marker_color="red",marker_line_width=2,name='Tv Appearence'),secondary_y=False)

        fig_spot.add_vline(x=datetime.strptime(js[selectbox1]["Date of Cancellation"],"%Y-%m-%d"), line_width=2, line_color="red")
        fig_spot.update_xaxes(showgrid=False)
        fig_spot.update_yaxes(title_text="Monthly listen",secondary_y=False,showgrid=False)
        fig_spot.update_yaxes(title_text="Negative tweet",secondary_y=True,showgrid=False)
        fig_spot.update_layout(plot_bgcolor = "#FFF4F3")
        st.plotly_chart(fig_spot, use_container_width=True,print_grid=False)

        #opening the image
        image_path = f'{js[selectbox1]["CHARTMETRIC ID"]}_masked.png'
        full_path = base_path.joinpath(base_path, "Images", image_path)
        image = Image.open(full_path)

        #displaying the image on streamlit app
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.image(image, caption=f"{selectbox1}'s", width=500)

        with col3:
            st.write(' ')

if design1=='Compare Artists':

    #create dropdown menu in 2 columns
    col1, col2 = st.columns(2)

    with col1:

        url = 'https://raw.githubusercontent.com/srs366/musicians_v_cancellation/master/scripts/streamlit/Artist_data.json'
        response = requests.get(url)
        js = json.loads(response.text)

        st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
        selected_gender = st.radio('', ['All','Male', 'Female'],index=0)
        js_gender = {}
        if selected_gender == "All":
            js_gender = js
        else:
            for key in js.keys():
                if js[key]["Gender"] == selected_gender:
                    js_gender[key] = js[key]

        #reason for cancellation selectbox
        js = {}
        selected_reason = st.selectbox('Reason for Cancellation:', ['All', 'Covid related', 'Political', 'Hate crime', 'Assault', 'Race related','Negligence','Sex crime','Negligence'], index = 0)
        if selected_reason == "All":
            js = js_gender
        else:
            for key in js_gender.keys():
                if js_gender[key]["cancellation category"] == selected_reason:
                    js[key] = js_gender[key]

        #create a selectbox
        selectbox1 = st.selectbox("Select a musician", [''] + sorted(list(js.keys())))
        if selectbox1 != '':
            prof_pic=js[selectbox1]["Image"] #show image
            #show the details
            text= f'''&emsp;&emsp;&emsp;<b>Name:</b> &ensp;{selectbox1}
            <br>&emsp;&emsp;&emsp;<b>Gender:</b> &ensp;{js[selectbox1]["Gender"]}
            <br>&emsp;&emsp;&emsp;<b>Race:</b> &ensp;{js[selectbox1]["Race"]}
            <br>&emsp;&emsp;&emsp;<b>Age:</b> &ensp;{(int(js[selectbox1]['Age']))}
            <br>&emsp;&emsp;&emsp;<b>Nationality:</b> &ensp;{js[selectbox1]['Nationality']}
            <br>&emsp;&emsp;&emsp;<b>Debut Year:</b> &ensp;{js[selectbox1]['Debut year']}
            <br>&emsp;&emsp;&emsp;<b>Genre:</b> &ensp;{js[selectbox1]['Genre']}
            <br>&emsp;&emsp;&emsp;<b>Cancellation Date:</b> <br>&emsp;&emsp;&emsp;{datetime.strptime(js[selectbox1]['Date of Cancellation'], '%Y-%m-%d').strftime('%d %B %Y')}
            <br>&emsp;&emsp;&emsp;<b>Category:</b> &ensp;{js[selectbox1]["cancellation category"]}'''

            st.markdown(
            """
            <style>
            .container {
                display: flex;
                /*background-color: red;*/
            }
            .reason {
                display: flex;
                height: 150px;
                /*background-color: red;*/
            }
            .logo-text {
                font-size:18px
            }
            .logo-img {
                float:right;
                height:275px
            }
            </style>
            """,
            unsafe_allow_html=True
            )

            st.markdown(
            f"""
            <div class="container">
                <img class="logo-img" src="{prof_pic}">
                <p class="logo-text">{text}</p>
            </div>
            """,
            unsafe_allow_html=True
            )

            reason = f'<b>Reason for Cancellation:</b> &ensp;{js[selectbox1]["Reason for cancellation"]}'

            st.markdown(f'''
            <div class='reason'>
                <p class="logo-text">{reason}</p>
            </div>
            ''',
            unsafe_allow_html=True)

            #PLOTLY
            base_path = pathlib.Path(__file__).resolve().parent
            artist_path = f'{js[selectbox1]["CHARTMETRIC ID"]}_merged_data.csv'
            full_path = base_path.joinpath(base_path, "streamlit_data", artist_path)
            data = pd.read_csv(full_path, parse_dates=[0], index_col=0)
            data_album = data[data["New_Music"]==1]
            data_tv = data[data["TV_Show"]==1]
            fig_col1_spot =make_subplots(specs=[[{"secondary_y":True}]],column_widths=[600],subplot_titles=[f"{selectbox1}'s Cancellation Data"])
            fig_col1_spot.add_trace(go.Scatter(x=data.index, y=data.monthly_listeners, mode='lines',line=dict(color='green',width=2),name='Spotify'),secondary_y=False)
            fig_col1_spot.add_trace(go.Scatter(x=data.index, y=data.TweetSentiment_Negative, mode='none',line=dict(color='red',width=1),name='Negative Tweet',fill='tonexty'),secondary_y=True)
            #radio line
            fig_col1_spot.add_trace(go.Scatter(x=data.index, y=data.monthly_spins, mode='lines',line=dict(color='#1599eb',width=1),name='Radio'),secondary_y=False)
            fig_col1_spot.add_trace(go.Scatter(x=data_album.index, y=data_album.monthly_listeners, mode='markers',marker_size=7,marker_line_color="midnight blue",marker_color="lightskyblue",marker_line_width=2,name='Music Release'),secondary_y=False)
            fig_col1_spot.add_trace(go.Scatter(x=data_tv.index, y=data_tv.monthly_listeners, mode='markers',marker_symbol="x",marker_size=10,marker_line_color="midnight blue",marker_color="red",marker_line_width=2,name='Tv Appearence'),secondary_y=False)

            fig_col1_spot.add_vline(x=datetime.strptime(js[selectbox1]["Date of Cancellation"],"%Y-%m-%d"), line_width=2, line_color="red")
            fig_col1_spot.update_xaxes(showgrid=False)
            fig_col1_spot.update_yaxes(title_text="Monthly listen",secondary_y=False,showgrid=False)
            fig_col1_spot.update_yaxes(title_text="Negative tweet",secondary_y=True,showgrid=False)
            fig_col1_spot.update_layout(plot_bgcolor = "#FFF4F3")
            col1.plotly_chart(fig_col1_spot, use_container_width=False,print_grid=False)

            image_path = f'{js[selectbox1]["CHARTMETRIC ID"]}_masked.png'
            full_path = base_path.joinpath(base_path, "Images", image_path)
            image = Image.open(full_path)

            #displaying the image on streamlit app
            st.image(image, caption=f"{selectbox1}'s", width=500)

    with col2:

        url = 'https://raw.githubusercontent.com/srs366/musicians_v_cancellation/master/scripts/streamlit/Artist_data.json'
        response = requests.get(url)
        js = json.loads(response.text)

        st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
        second_gender = st.radio(' ', ['All','Male', 'Female'],index=0)
        js_gender = {}
        if second_gender == "All":
            js_gender = js
        else:
            for key in js.keys():
                if js[key]["Gender"] == second_gender:
                    js_gender[key] = js[key]

        #reason for cancellation selectbox
        js = {}
        selected_reason2 = st.selectbox('Reason for Cancellation: ', ['All', 'Covid related', 'Political', 'Hate crime', 'Assault', 'Race related','Negligence','Sex crime','Negligence'], index = 0)
        if selected_reason2 == "All":
            js = js_gender
        else:
            for key in js_gender.keys():
                if js_gender[key]["cancellation category"] == selected_reason2:
                    js[key] = js_gender[key]

        #create a selectbox
        selectbox2 = st.selectbox("Select a musician", [''] + sorted(list(js.keys())),key = "one")
        if selectbox2 != '':
            prof_pic=js[selectbox2]["Image"]

            #show the full name
            #st.image(prof_pic,width=200)
            text= f'''&emsp;&emsp;&emsp;<b>Name:</b> &ensp;{selectbox2}
            <br>&emsp;&emsp;&emsp;<b>Gender:</b> &ensp;{js[selectbox2]["Gender"]}
            <br>&emsp;&emsp;&emsp;<b>Race:</b> &ensp;{js[selectbox2]["Race"]}
            <br>&emsp;&emsp;&emsp;<b>Age:</b> &ensp;{(int(js[selectbox2]['Age']))}
            <br>&emsp;&emsp;&emsp;<b>Nationality:</b> &ensp;{js[selectbox2]["Nationality"]}
            <br>&emsp;&emsp;&emsp;<b>Debut Year:</b> &ensp;{js[selectbox2]["Debut year"]}
            <br>&emsp;&emsp;&emsp;<b>Genre:</b> &ensp;{js[selectbox2]["Genre"]}
            <br>&emsp;&emsp;&emsp;<b>Cancellation Date:</b> <br>&emsp;&emsp;&emsp;{datetime.strptime(js[selectbox2]['Date of Cancellation'], '%Y-%m-%d').strftime('%d %B %Y')}
            <br>&emsp;&emsp;&emsp;<b>Category:</b> &ensp;{js[selectbox2]["cancellation category"]}'''

            st.markdown(
            """
            <style>
            .container {
                display: flex;
                /*background-color: red;*/
            }
            .reason {
                display: flex;
                height: 150px;
                /*background-color: red;*/
            }
            .logo-text {
                font-size:18px
            }
            .logo-img {
                float:right;
                height:275px
            }
            </style>
            """,
            unsafe_allow_html=True
            )

            st.markdown(
            f"""
            <div class="container">
                <img class="logo-img" src="{prof_pic}">
                <p class="logo-text">{text}</p>
            </div>
            """,
            unsafe_allow_html=True
            )

            reason = f'<b>Reason for Cancellation:</b> &ensp;{js[selectbox2]["Reason for cancellation"]}'
            st.markdown(f'''
            <div class='reason'>
                <p class="logo-text">{reason}</p>
            </div>
            ''',
            unsafe_allow_html=True)

            base_path = pathlib.Path(__file__).resolve().parent
            artist_path = f'{js[selectbox2]["CHARTMETRIC ID"]}_merged_data.csv'
            full_path = base_path.joinpath(base_path, "streamlit_data", artist_path)
            data = pd.read_csv(full_path, parse_dates=[0], index_col=0)

            # data = pd.read_csv(f'{js[selectbox2]["CHARTMETRIC ID"]}_merged_data.csv', parse_dates=[0], index_col=0)
            data_album = data[data["New_Music"]==1]
            data_tv = data[data["TV_Show"]==1]
            fig_col2_spot =make_subplots(specs=[[{"secondary_y":True}]],column_widths=[600],subplot_titles=[f"{selectbox2}'s Cancellation Data"])

            fig_col2_spot.add_trace(go.Scatter(x=data.index, y=data.monthly_listeners, mode='lines',line=dict(color='green',width=2),name='Spotify'),secondary_y=False)
            fig_col2_spot.add_trace(go.Scatter(x=data.index, y=data.TweetSentiment_Negative, mode='none',line=dict(color='red',width=1),name='Negative Tweet',fill='tonexty'),secondary_y=True)
            # radio line
            fig_col2_spot.add_trace(go.Scatter(x=data.index, y=data.monthly_spins, mode='lines',line=dict(color='#1599eb',width=1),name='Radio'),secondary_y=False)
            fig_col2_spot.add_trace(go.Scatter(x=data_album.index, y=data_album.monthly_listeners, mode='markers',marker_size=7,marker_line_color="midnight blue",marker_color="lightskyblue",marker_line_width=2,name='Music Release'),secondary_y=False)
            fig_col2_spot.add_trace(go.Scatter(x=data_tv.index, y=data_tv.monthly_listeners, mode='markers',marker_symbol="x",marker_size=7,marker_line_color="midnight blue",marker_color="red",marker_line_width=2,name='Tv Appearence'),secondary_y=False)


            fig_col2_spot.add_vline(x=datetime.strptime(js[selectbox2]["Date of Cancellation"],"%Y-%m-%d"), line_width=3, line_color="red")
            fig_col2_spot.update_xaxes(showgrid=False)
            fig_col2_spot.update_yaxes(title_text="Monthly listen",secondary_y=False,showgrid=False)
            fig_col2_spot.update_yaxes(title_text="Negative tweet",secondary_y=True,showgrid=False)
            fig_col2_spot.update_layout(plot_bgcolor = "#FFF4F3")
            col2.plotly_chart(fig_col2_spot, use_container_width=False)

            image_path = f'{js[selectbox2]["CHARTMETRIC ID"]}_masked.png'
            full_path = base_path.joinpath(base_path, "Images", image_path)
            image = Image.open(full_path)

            #displaying the image on streamlit app
            st.image(image, caption=f"{selectbox2}'s", width=500)
