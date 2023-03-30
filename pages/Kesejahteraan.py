#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Kondisi Kesejahtaraan Sumatera Barat', page_icon=':bar_chart:', layout='wide')
st.title('Kondisi Kesejahteraan Provinsi Sumatera Barat')


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
sheet_name3 = 'Kesehatan'
sheet_name4 = 'Pendidikan'

# ===== kategori =====
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name1,
                   usecols='A:AH',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name1,
                                usecols='A:AH')
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
                        st.metric("UMP Sumbar Tahun 2023", "2,742,467", "229,928")
                        st.metric("UMP Sumbar Tahun 2022", "2,512,539", "28,498")
                        st.metric("UMP Sumbar Tahun 2021", "2,484,041")

               
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
                c4.subheader("Jumlah Guru, Murid dan Sekolah di Provinsi Sumatera Barat Tahun 2022")
                df = pd.read_excel(excel_file, sheet_name=sheet_name4,
                                        engine="openpyxl", usecols='M:N')

                st._arrow_bar_chart(df, x="Sekolah", y=['Jumlah'])

                
            with c5:
                c5.subheader("Perbandingan Total Pencari Kerja dan Jumlah Lowongan Kerja di tahun 2021")
                st.bar_chart(filtered_kategori_2021, x='Kabupaten_Kota', y=['Total_Pencari_Kerja21', 'Jumlah_Lowongan_Kerja_Terdaftar_2021'])
            with c6:
                c6.subheader("Perbandingan Total Pencari Kerja dan Jumlah Lowongan Kerja di tahun 2022")
                st.bar_chart(filtered_kategori_2021, x="Kabupaten_Kota", y=['Total_Pencari_Kerja22', 'Jumlah_Lowongan_Kerja_Terdaftar_2022'])


            with c7:
                
                c7.subheader("Fasilitas Kesehatan di Sumatera Batat")
                df = pd.read_excel(excel_file, sheet_name=sheet_name3,
                                engine="openpyxl", usecols='M:N')

                st.vega_lite_chart(df, {
                        'mark': {'type': 'bar', 'tooltip': True},
                        'encoding': {
                            'x': {'field': 'K_Kes', 'type': 'ordinal'},
                            'y': {'field': 'Jumlah', 'type': 'quantitative'},
                            'color': {'field': 'K_Kes'},
                        },
                            })
                
            with c8:
                
                c8.subheader("Fasilitas Pendukung Pendidikan di Sumatera Batat")
                df = pd.read_excel(excel_file, sheet_name=sheet_name4,
                                engine="openpyxl", usecols='O:P')

                st.vega_lite_chart(df, {
                        'mark': {'type': 'bar', 'tooltip': True},
                        'encoding': {
                            'x': {'field': 'Tempat', 'type': 'ordinal'},
                            'y': {'field': 'Jumlah2', 'type': 'quantitative'},
                            'color': {'field': 'Tempat'},
                        },
                            })
            

    
elif(option == 'Daerah'):
    st.title('Data Tenaga Kerja Berdasarkan Daerah')
    wilayah = df['Kabupaten_Kota'].unique().tolist()
    wilayah_selection = st.selectbox('Pilih Daerah : ', wilayah)
    m1, m2 = st.columns((1, 1))
    m3, m4 ,m5 = st.columns((1, 1, 1))
    m5, m6 = st.columns((1, 1))
    m7, m8 = st.columns((1, 1))
    m9, m10 = st.columns((1,1))
    todf = pd.read_excel('Sosial_Kesejahteraan.xlsx', sheet_name='Kesejahteraan(Pekerjaan)')
    to = todf[(todf['Kabupaten_Kota'] == wilayah_selection)]

    # ===== Delta Section =====
    perempuan = int(to['Pencari_Kerja_Terdaftar(P)22']) - int(to['Pencari_Kerja_Terdaftar(P)21'])
    laki2 = int(to['Pencari_Kerja_Terdaftar(L)22']) - int(to['Pencari_Kerja_Terdaftar(L)21'])

    s_Negeri = int(to['Sekolah_Negeri'])
    sn = "{:,}".format(s_Negeri)
    s_Swasta = int(to['Sekolah_Swasta'])
    ss = "{:,}".format(s_Swasta)
    g_negeri = int(to['Guru_Negeri'])
    gn = "{:,}".format(g_negeri)
    g_swasta = int(to['Guru_Swasta'])
    gs = "{:,}".format(g_swasta)
    m_negeri = int(to['Murid_Negeri'])
    mn = "{:,}".format(m_negeri)
    m_swasta = int(to['Murid_Swasta'])
    ms = "{:,}".format(m_swasta)

    sd = int(to['SD'])
    sdt = "{:,}".format(sd)
    smp = int(to['SMP'])
    smpt = "{:,}".format(smp)
    sma = int(to['SMA'])
    smat = "{:,}".format(sma)
    smk = int(to['SMK'])
    smkt = "{:,}".format(smk)
    pt = int(to['PT'])
    ptt = "{:,}".format(pt)
    t = int(to['PAUD'])
    tt = "{:,}".format(t)



   
    # ===== Comparation =====
    totalpr = df['Pencari_Kerja_Terdaftar(P)22'].sum()
    totalprm = "{:,}".format(totalpr)
    totallk = df['Pencari_Kerja_Terdaftar(L)22'].sum()
    totallk2 = "{:,}".format(totallk)
    

    
    with m1:

        m1.metric(label ='Jumlah Pencari Kerja Laki-Laki 2022 ',value = int(to['Pencari_Kerja_Terdaftar(L)22']), delta= laki2)
        m1.metric(label ='Jumlah Pencari Kerja Laki-Laki se-Provinsi Sumbar 2022',value = totallk2)
    with m2:
         m2.metric(label ='Jumlah Pencari Kerja Perempuan 2022',value = int(to['Pencari_Kerja_Terdaftar(P)22']), delta= perempuan)
         m2.metric(label ='Jumlah Pencari Kerja Perempuan se-Provinsi Sumbar 2022',value = totalprm)

    st.title('Pendidikan')
    col1, col2, col3 = st.columns(3)
    col1.metric(label ='Sekolah Negeri',value = sn)
    col2.metric(label ='Guru Negeri',value = gn)
    col3.metric(label ='Murid Negeri',value = mn)

    col4, col5, col6 = st.columns(3)
    col4.metric(label ='Sekolah Swasta',value = ss)
    col5.metric(label ='Guru Swasta',value = gs)
    col6.metric(label ='Murid Swasta',value = ms)

    col7, col8, col9 = st.columns(3)
    col7.metric(label ='SD',value = sdt)
    col8.metric(label ='SMP',value = smpt)
    col9.metric(label ='SMA',value = smat)

    col10, col11, col12 = st.columns(3)
    col10.metric(label ='SMK',value = smkt)
    col11.metric(label ='PT',value = ptt)
    col12.metric(label =' PAUD ',value = tt)


    st.title('Kesehatan')
    col1, col2, col3 = st.columns(3)
    col1.metric(label ='Dokter',value = "{:,}".format(int(to['Dokter'])))
    col2.metric(label ='Psikolog',value = "{:,}".format(int(to['Psikolog'])))
    col3.metric(label ='Perawat',value = "{:,}".format(int(to['Perawat'])))

    col4, col5, col6 = st.columns(3)
    col4.metric(label ='Bidan',value = "{:,}".format(int(to['Bidan'])))
    col5.metric(label ='Farmasian',value = "{:,}".format(int(to['Farmasian'])))
    col6.metric(label ='Tenaga Kesehatan Lain',value = "{:,}".format(int(to['Tenaga_Kesmas'])))

    col7, col8, col9 = st.columns(3)
    col7.metric(label ='Rumah Sakit',value = "{:,}".format (int(to['Rumah_Sakit'])))
    col8.metric(label ='Poliklinik',value = "{:,}".format(int(to['Poliklinik'])))
    col9.metric(label ='Puskesmas',value = "{:,}".format(int(to['Puskesmas'])))

    
   


    # m3.subheader("Kondisi Pendidikan") 
    # with m5:
    #      m5.metric(label ='Penduduk Beragama Islam',value = int(to['Islam']))
    # with m6:
    #      m6.metric(label ='Penduduk Beragama Kristen Protestan',value = int(to['Protestan']))
    # with m7:
    #      m7.metric(label ='Penduduk Beragama Kristen Katolik',value = int(to['Katolik']))
    # with m8:
    #      m8.metric(label ='Penduduk Beragama Budha',value = int(to['Budha']))
    # with m9:
    #      m9.metric(label ='Penduduk Beragama Hindu',value = int(to['Hindu']))
    # with m10:
    #      m10.metric(label ='Penduduk Beragama Konghucu',value = int(to['Konghucu']))
   
    
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



   