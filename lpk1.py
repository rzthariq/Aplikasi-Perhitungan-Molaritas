import streamlit as st

st.title('Aplikasi Menghitung Molaritas')

st.latex(r'''
    M =
    \left(\frac{massa}{fp × volume × bm}\right) =
    ''')

massa=st.number_input('massa=')
st.write('massa senyawa=',massa)
fp=st.number_input('fp=')
st.write('fp senyawa=',fp)
volume=st.number_input('volume=')
st.write('volume senyawa=',volume)
bm=st.number_input('bm=')
st.write('bm senyawa=',bm)

Operasi_Molaritas=massa/(fp*volume*bm)
st.write(f'''
        M =
    {massa}/{fp} × {volume} × {bm} = {Operasi_Molaritas}
    ''')