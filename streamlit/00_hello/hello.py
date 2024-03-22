import streamlit as st


st.title('text display')
st.write('hello')
st.write('text context...')
st.markdown('#Markdown content')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.title('content')
st.header('first header')
st.code('i for i in range(1,10)')


import pandas as pd

df :pd.DataFrame = pd.DataFrame({'col1:':[1,2,3],
                                 'col2:':['a','b','c']})
st.write(df)
st.table(df)
#st.json(df.to_dict)
st.metric('My metric', 42, 2)

st.video('https://www.youtube.com/watch?v=utGbrubEY2E')
 
