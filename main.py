import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# writeでもデータフレーム表示できる
st.write(df)

# dataframeで表を表示させると、表の幅高さpx指定、ハイライト表示ができる。
st.dataframe(df.style.highlight_max(axis=0), width=400)

# tableの場合はソートできない静的な表が表示される
st.table(df.style.highlight_max(axis=0))

# マジックコマンド

"""
# title 1
## title 2
### title 3
"""

"""
```python
import streamlit as st
import pandas as pd
```
"""

# グラフ

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.dataframe(df2)

st.write('折れ線グラフ')
st.line_chart(df2)

st.write('エリアグラフ')
st.area_chart(df2)

st.write('棒グラフ')
st.bar_chart(df2)


# マップ

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)

st.write('マップ')
st.map(df3)


# イメージ
from PIL import Image
st.write('イメージ画像の表示')
img = Image.open('bunny.jpg')
st.image(img, caption='Ducky & Bunny', use_column_width=True)


st.title('インタラクティブウィジェット')
# チェックボックス
st.write('チェックボックスで表示／非表示')

if st.checkbox('画像表示'):
    img = Image.open('bunny.jpg')
    st.image(img, caption='Ducky & Bunny', use_column_width=True)
    
# セレクトボックス    
st.write('セレクトボックス')
option = st.selectbox(
    'あなたの好きな数字を教えてください。',
    list(range(1, 11)),
)
st.write('あなたの好きな数字は', option, 'です。')

#テキストボックス
st.write('テキストボックス')
text = st.text_input('あなたの趣味は？')
'あなたの趣味は', text, 'です。'

# スライダー
st.write('スライダー')
condition = st.slider('本日のコンディションは？', 0, 100, 50)
'本日のあなたのコンディションは、', condition, 'です。'

# サイドバー
st.sidebar.selectbox(
    '今日のごきげんは？',
    ['ごきげん', 'ごきげんななめ']
    )

# エキスパンダー
st.write('よくあるご質問')
expander1 = st.expander('暑い日はどうすればよいのですか？')
expander1.write('水を飲めばよいのです。')
expander2 = st.expander('寒い日はどうすればよいのですか？')
expander2.write('たくさん服を着ればよいのです。')