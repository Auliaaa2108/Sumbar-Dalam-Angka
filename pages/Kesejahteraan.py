#Libraries
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Kondisi Kesejahtaraan SUmatera Barat', page_icon=':bar_chart:', layout='wide')
st.title('Data Tenaga Kerja, Upah Minimum Provinsi dan Jumlah Unit Usaha di Provinsi Sumatera Barat')


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
sheet_name1 = 'Kesejahteraan(Pekerjaan)'
sheet_name2 = 'UMP'

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
            with c1:
                # c1.subheader("Upah Minimum Provinsi Sumatera Barat Dari Tahun Ke Tahun")
                # df = pd.read_excel(excel_file, sheet_name=sheet_name2, 
                #                             engine="openpyxl", usecols='A:B')
                #     # st.bar_chart(df, x="Tahun", y="UMP")

                c1.subheader("Upah Minimum Provinsi Sumatera Barat")
                upah = pd.read_excel(excel_file, sheet_name=sheet_name2, 
                                            engine="openpyxl", usecols='A:D')
                    # st.bar_chart(df, x="Tahun", y="Kejahatan")
                st.line_chart(upah, x='Tahun', y=['UMP'])

            with c2:
                        st.metric("UMP Sumbar Tahun 2023", "2.742.467", "229.928")
                        st.metric("UMP Sumbar Tahun 2022", "2.512.539", "28.498")
                        st.metric("UMP Sumbar Tahun 2021", "2.484.041")

               
            with c3:
                c3.subheader("Jumlah Unit Usaha di Provinsi Sumatera Barat Tahun 2022")
                c3.vega_lite_chart(filtered_kategori_2021, {
                    'mark': {'type': 'bar', 'tooltip': True},
                    'encoding': {
                        'x': {'field': 'Kabupaten_Kota', 'type': 'ordinal'},
                        'y': {'field': 'Unit_Usaha22', 'type': 'quantitative'},
                        'color': {'field': 'Kabupaten_Kota'},
                    },
                    })
            with c4:
                c4.subheader("Jumlah Unit Usaha di Provinsi Sumatera Barat Tahun 2022")
                c4.vega_lite_chart(filtered_kategori_2021, {
                    'mark': {'type': 'bar', 'tooltip': True},
                    'encoding': {
                        'x': {'field': 'Kabupaten_Kota', 'type': 'ordinal'},
                        'y': {'field': 'Unit_Usaha21', 'type': 'quantitative'},
                        'color': {'field': 'Kabupaten_Kota'},
                    },
                    })
            with c5:
                c5.subheader("Perbandingan Total Pencari Kerja dan Jumlah Lowongan Kerja di tahun 2021")
                st.bar_chart(filtered_kategori_2021, x='Kabupaten_Kota', y=['Total_Pencari_Kerja21', 'Jumlah_Lowongan_Kerja_Terdaftar_2021'])
            with c6:
                c6.subheader("Perbandingan Total Pencari Kerja dan Jumlah Lowongan Kerja di tahun 2022")
                st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y=['Total_Pencari_Kerja22', 'Jumlah_Lowongan_Kerja_Terdaftar_2022'])

    
elif(option == 'Daerah'):
    st.write('Data Tenaga Kerja Berdasarkan Daerah')
    wilayah = df['Kabupaten_Kota'].unique().tolist()
    wilayah_selection = st.selectbox('Pilih Daerah : ', wilayah)
    m1, m2 = st.columns((1, 1))
    todf = pd.read_excel('Sosial_Kesejahteraan.xlsx', sheet_name='Kesejahteraan(Pekerjaan)')
    to = todf[(todf['Kabupaten_Kota'] == wilayah_selection)]

    # ===== Delta Section =====
    perempuan = int(to['Pencari_Kerja_Terdaftar(P)22']) - int(to['Pencari_Kerja_Terdaftar(P)21'])
    laki2 = int(to['Pencari_Kerja_Terdaftar(L)22']) - int(to['Pencari_Kerja_Terdaftar(L)21'])
   
    # ===== Comparation =====
    totalpr = df['Pencari_Kerja_Terdaftar(P)22'].sum()
    totallk = df['Pencari_Kerja_Terdaftar(L)22'].sum()
    

    
    with m1:

        m1.metric(label ='Jumlah Pencari Kerja Laki-Laki 2022 ',value = int(to['Pencari_Kerja_Terdaftar(L)22']), delta= laki2)
        m1.metric(label ='Jumlah Pencari Kerja Laki-Laki se-Provinsi Sumbar 2022',value = totallk)
    with m2:
         m2.metric(label ='Jumlah Pencari Kerja Perempuan 2022',value = int(to['Pencari_Kerja_Terdaftar(P)22']), delta= perempuan)
         m2.metric(label ='Jumlah Pencari Kerja Perempuan se-Provinsi Sumbar 2022',value = totalpr)
   
    
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
    # st.line_chart(wilayah_kategori,  y='Value', use_container_width=True)



   