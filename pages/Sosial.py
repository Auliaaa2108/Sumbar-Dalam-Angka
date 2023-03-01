#Libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(page_title='Kondisi Sosial SUmatera Barat', page_icon=':bar_chart:', layout='wide')
st.title("Kasus Kejahatan yang terjadi Di Sumatera Barat Pada Tahun 2020 - 2022")


# Setting'
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Filter 
excel_file = 'Sosial_Kesejahteraan.xlsx'
sheet_name1 = 'Sosial'
sheet_name2 = 'Kejahatan'

# ===== kategori =====
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name1,
                   usecols='A:Z',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name1,
                                usecols='A:Z')
df_participants.dropna(inplace=True)

# ===== Dropdown in Sidebar =====
option = st.sidebar.selectbox(
    'Pilih :',
    ('All', 'Daerah'))

if(option == 'All'):
    # ===== STREAMLIT SELECTION =====
    
    daerah1 = df['Kabupaten_Kota'].unique()
    daerah_selection1 = st.multiselect('Daerah:',
                                        daerah1,
                                        default=daerah1)
    

    # Selected option
    if len(daerah_selection1) == 0 or len(daerah_selection1) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection1):
            filtered_kategori_2021 = df[df['Kabupaten_Kota'].isin(daerah_selection1)]
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            c5, c6 = st.columns(2)
            c7, c8 = st.columns(2)
            c9, c10 = st.columns(2)
            c11, c12 = st.columns(2)
            c13, c14 = st.columns(2)
            c15, c16 = st.columns(2)
            with c1:
                c1.subheader("Kasus Kejahatan Di Sumatera Barat")
                kasus = pd.read_excel(excel_file, sheet_name=sheet_name2, 
                                            engine="openpyxl", usecols='A:D')
                    # st.bar_chart(df, x="Tahun", y="Kejahatan")
                st.bar_chart(kasus, x='Kasus', y=['2020', '2021', '2022'])

            with c2:
                
                # m1, m2 = st.columns((1, 1))
                
                df= pd.read_excel(excel_file, sheet_name=sheet_name2, 
                                            engine="openpyxl", usecols='A:D')            
                # ===== Comparation =====
                total1 = df['2022'].sum()
                st.metric(label ='Total Kasus Kejahatan Sumatera Barat di 2022 ',value = total1,delta="-1.361")
                total2 = df['2021'].sum()
                st.metric(label ='Total Kasus Kejahatan Sumatera Barat di 2021 ',value = total2,delta='-2.183')
                total3 = df['2020'].sum()
                st.metric(label ='Total Kasus Kejahatan Sumatera Barat di 2020 ',value = total3)

                st.sidebar.header("Filter: ")
                tahun = st.sidebar.selectbox(
                    "Pilih tahun: ",
                    ["2020", "2021", "2022"]
                )

                if(tahun == "2020"):
                    
                    with c3:
                        c3.subheader("Kasus Kekerasan Terhadap Anak di Provinsi Sumatera Barat Tahun 2020 ")
                        st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y="KekerasanAnak2020")
                    
                    with c4:
                            c4.subheader("Korban Kekerasan Terhadap Anak di Provinsi Sumatera Barat Tahun 2020")
                            df = pd.read_excel(excel_file, sheet_name=sheet_name1,
                                    engine="openpyxl", usecols='A:S')
                            st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y=["KorbanAnakPR2020","KorbanAnakLK2020"])
                    
                    
                    with c5:
                        c5.subheader("Kasus  Kekerasan Terhadap Perempuan di Provinsi Sumatera Barat Tahun 2020 ") 

                        
                        df = pd.read_excel(excel_file, sheet_name=sheet_name1,
                                engine="openpyxl", usecols='A:S')

                        st.vega_lite_chart(filtered_kategori_2021, {
                        'mark': {'type': 'bar', 'tooltip': True},
                        'encoding': {
                            'x': {'field': 'Kabupaten_Kota', 'type': 'ordinal'},
                            'y': {'field': 'Kekerasan_Perempuan_2020', 'type': 'quantitative'},
                            'color': {'field': 'Kabupaten_Kota'},
                        },
                            })
                         
                        # st.bar_chart(df, x="", y="Kekerasan_Perempuan_2020")
                        
                    with c6:

                        c6.subheader("Persentase Korban Kekerasan Terhadap Perempuan di Provinsi Sumatera Barat Tahun 2020")
                        df = pd.read_excel(excel_file, sheet_name=sheet_name1,
                                    engine="openpyxl", usecols='A:S')

                        fig = px.pie(filtered_kategori_2021, values="Jumlah_Korban_Perempuan_2020", names="Kabupaten_Kota")
                        (fig)

                elif(tahun == "2021"):
                    
                    
                    with c7:
                        c7.subheader("Kasus Kekerasan Terhadap Anak di Provinsi Sumatera Barat Tahun 2021 ")
                        df = pd.read_excel(excel_file, sheet_name=sheet_name1,
                                engine="openpyxl", usecols='A:M')
                        st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y="KekerasanAnak2021")
                    
                    with c8:
                            c8.subheader("Korban Kekerasan Terhadap Anak di Provinsi Sumatera Barat Tahun 2021")
                            df = pd.read_excel(excel_file, sheet_name=sheet_name1,
                                    engine="openpyxl", usecols='A:M')
                            st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y=["KorbanAnakPR2021","KorbanAnakLK2021"])
                    
                    
                    with c9:
                        c9.subheader("Kasus  Kekerasan Terhadap Perempuan di Provinsi Sumatera Barat Tahun 2021 ") 
                        df = pd.read_excel(excel_file, sheet_name=sheet_name1,
                                engine="openpyxl", usecols='A:M')
                         
                        st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y="Kekerasan_Perempuan_2021")
                        
                    with c10:

                        c10.subheader("Persentase Korban Kekerasan Terhadap Perempuan di Provinsi Sumatera Barat Tahun 2021")
                        df = pd.read_excel(excel_file, sheet_name=sheet_name1,
                                    engine="openpyxl", usecols='A:O')

                        fig = px.pie(filtered_kategori_2021, values="Jumlah_Korban_Perempuan_2021", names="Kabupaten_Kota")
                        (fig)
                        
                            
                    

                elif(tahun == "2022"):
                        
                        with c11:
                            c11.subheader("Kasus Kekerasan Terhadap Anak di Provinsi Sumatera Barat Tahun 2022 ")
                            df = pd.read_excel(excel_file, sheet_name=sheet_name2,
                                    engine="openpyxl", usecols='A:S')
                            st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y="KekerasanAnak2022")
                        
                        with c12:
                                c12.subheader("Korban Kekerasan Terhadap Anak di Provinsi Sumatera Barat Tahun 2022")
                                df = pd.read_excel(excel_file, sheet_name=sheet_name2,
                                        engine="openpyxl", usecols='A:S')
                                st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y=["KorbanAnakPR2022","KorbanAnakLK2022"])
                        
                      
                        
                        with c13:
                            c13.subheader("Kasus  Kekerasan Terhadap Perempuan di Provinsi Sumatera Barat Tahun 2022 ") 
                            df = pd.read_excel(excel_file, sheet_name=sheet_name2,
                                    engine="openpyxl", usecols='A:S')
                            
                            st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y="Kekerasan_Perempuan_2022")
                            
                        with c14:

                            c14.subheader("Persentase Korban Kekerasan Terhadap Perempuan di Provinsi Sumatera Barat Tahun 2022")
                            df = pd.read_excel(excel_file, sheet_name=sheet_name2,
                                        engine="openpyxl", usecols='A:S')

                            fig = px.pie(filtered_kategori_2021, values="Jumlah_Korban_Perempuan_2022", names="Kabupaten_Kota")
                            (fig)

elif(option == 'Daerah'):
    wilayah = df['Kabupaten_Kota'].unique().tolist()
    wilayah_selection = st.selectbox('Pilih Daerah : ', wilayah)
    m1, m2 = st.columns((1, 1))
    todf = pd.read_excel('Sosial_Kesejahteraan.xlsx', sheet_name='Sosial')
    to = todf[(todf['Kabupaten_Kota'] == wilayah_selection)]

    # ===== Delta Section =====
    anak = int(to['KekerasanAnak2022']) - int(to['KekerasanAnak2021'])
    perempuan = int(to['Kekerasan_Perempuan_2022']) - int(to['Kekerasan_Perempuan_2021'])
   
    # ===== Comparation =====
    totalanak = df['KekerasanAnak2022'].sum()
    totalperempuan = df['Kekerasan_Perempuan_2022'].sum()
    

    with m1:
        m1.metric(label ='Jumlah Kekerasan Anak Tahun 2022 ',value = int(to['KekerasanAnak2022']), delta= anak)
        m1.metric(label ='Jumlah Kekerasan Anak se-Provinsi Sumbar 2022',value = totalanak)
    with m2:
         m2.metric(label ='Jumlah Kekerasan Terhadap Perempuan 2022',value = int(to['Kekerasan_Perempuan_2022']), delta= perempuan)
         m2.metric(label ='Jumlah Kekerasan Terhadap Perempuan se-Provinsi Sumbar 2022',value = totalperempuan)
   

            
                
    # # ----- MANIPULATION for Man -----
    # # ===== List for Values =====
    # single_row_df = to[0:1]
    # listValueskategori = []
    # list_from_df_fungsional2 = single_row_df.values.tolist()[0]
    # for i in range(2, 4):
    #     listValueskategori.append(list_from_df_fungsional2[i])
    # # ----- END OF MANIPULATION -----
    # # ===== Show Bar Chart =====
    # wilayah_kategori = pd.DataFrame({
    #     'Value': listValueskategori
    # }, index=['2021', '2022'])
    # st.subheader("Perubahan Laki-Laki")
    # st.line_chart(wilayah_kategori,  y='Value', use_container_width=True)
    #   # ----- MANIPULATION for Man -----
    # # ===== List for Values =====
    # single_row_df = to[0:1]
    # listValueskategori = []
    # list_from_df_fungsional2 = single_row_df.values.tolist()[0]
    # for i in range(5, 7):
    #     listValueskategori.append(list_from_df_fungsional2[i])
    # # ----- END OF MANIPULATION -----
    # # ===== Show Bar Chart =====
    # wilayah_kategori = pd.DataFrame({
    #     'Value': listValueskategori
    # }, index=['2021', '2022'])
    # st.subheader("Perubahan Perempuan")
    # st.bar_chart(wilayah_kategori,  y='Value', use_container_width=True)