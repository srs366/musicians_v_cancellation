import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import json

js = json.load(open('Artist_data.json', encoding='utf-8'))
selectbox = st.selectbox("Select a musician", [''] + list(js.keys()))
data = pd.read_csv(f'{js[selectbox]["CHARTMETRIC ID"]}_tweets.csv', parse_dates=[0], index_col=0)
# Create some sample text
text = data.Text

wc = WordCloud(background_color="white", colormap="hot", max_words=max_word, max_font_size=max_font, random_state=random)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(image)

    # show
    plt.figure(figsize=(100,100))
    fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
   # axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    
    st.pyplot()