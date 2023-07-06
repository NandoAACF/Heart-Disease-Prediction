import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def load_data():
    # Menampilkan data
    df = pd.read_csv('data.csv')
    df['HeartDisease'] = df['HeartDisease'].replace({0:'No', 1:'Yes'})

    return df

df = load_data()

def show_insight():
    st.title('Heart Disease Insight')

    st.markdown("### **1. Berapa persentase orang yang menderita penyakit jantung?**")
    plt.figure(figsize = (4,4))
    heart_disease_counts = df['HeartDisease'].value_counts()

    plt.pie(heart_disease_counts, labels=heart_disease_counts.index, autopct='%1.1f%%')

    plt.title('Heart Disease Distribution')
    st.pyplot(plt)
    st.write('Tampak bahwa distribusi keduanya seimbang (balance)')




    st.markdown("### **2. Umur berapa yang paling rawan menderita penyakit jantung?**")
    # Lakukan binning untuk age
    bins = [20, 30, 40, 50, 60, 70]
    labels = ['21-30', '31-40', '41-50', '51-60', '61-70']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(9, 5))
    ax = sns.countplot(data=df, x='Age Group', hue='HeartDisease')

    # Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Umur')
    st.pyplot(plt)
    st.write('Tampak bahwa rentang umur 51 tahun ke atas cukup rawan terkena penyakit jantung. Semakin bertambahnya umur, maka peluang terkena penyakit jantung semakin besar.')
    



    st.markdown("### **3. Berapa batas maximum heart rate yang rawan penyakit jantung?**")
    plt.figure(figsize=(10, 5))
    ax = sns.histplot(data=df, x='MaxHR', hue='HeartDisease')

    plt.title('Heart Disease Berdasarkan Maximum Heart Rate')
    st.pyplot(plt)
    st.write('Terlihat jelas bahwa sebagian besar orang yang menderita penyakit jantung memiliki maximum heart rate di bawah 130. Dari grafik tersebut tampak bahwa peluang menderita penyakit jantung semakin besar jika maximum heart ratenya semakin rendah.')




    st.markdown("### **4. Apakah jenis kelamin berpengaruh pada peluang menderita penyakit jantung?**")
    plt.figure(figsize=(6, 5))
    ax = sns.countplot(data=df, x='Sex', hue='HeartDisease')

    #  Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Jenis Kelamin')
    st.pyplot(plt)
    st.write('Ya, tampak ada perbedaan yang sangat signifikan mengenai penderita penyakit jantung berdasarkan jenis kelamin.')
    st.write('Laki-laki lebih rawan menderita penyakit jantung dibandingkan perempuan.')




    st.markdown("### **5. Jenis chestpain apa yang rawan memicu penyakit jantung?**")
    plt.figure(figsize=(6, 5))
    ax = sns.countplot(data=df, x='ChestPainType', hue='HeartDisease')

    #  Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Tipe Chest Pain')
    st.pyplot(plt)
    st.write('Chestpain asymptomatic adalah jenis chestpain yang paling rawan memicu penyakit jantung.')
    st.write('Hal tersebut tampak pada grafik di atas dengan perbedaan yang sangat signifikan dibanding ketiga jenis chestpain yang lain.')




    st.markdown("### **6. Apakah besar tekanan darah dapat mengindikasikan penyakit jantung?**")
    df['RestingBP'].replace(0, df['RestingBP'].median(),inplace=True)
    plt.figure(figsize=(10, 5))
    ax = sns.histplot(data=df, x='RestingBP', hue='HeartDisease')

    plt.title('Heart Disease Berdasarkan Tekanan Darah')
    st.pyplot(plt)
    st.write('Tidak terlalu tampak perbedaan yang signifikan pada grafik di atas.')
    st.write('Namun, tampak bahwa sebagian besar orang yang tidak menderita penyakit jantung memiliki tekanan darah antara 120-130 mm Hg.')




    st.markdown("### **7. Berapa tingkat kolesterol yang rawan memicu penyakit jantung?**")
    # Lakukan binning untuk kolesterol
    bins = [100, 150, 200, 250, 300, 350, 400, 450, 600]
    labels = ['101-150', '151-200', '201-250', '251-300', '301-350', '351-400', '401-450', '451-600']
    df['Cholesterol Group'] = pd.cut(df['Cholesterol'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(10, 5))
    ax = sns.countplot(data=df, x='Cholesterol Group', hue='HeartDisease')

    # Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Tingkat Kolesterol')
    st.pyplot(plt)
    st.write('Tampak bahwa orang dengan tingkat kolesterol di atas 251 mm/dL menderita penyakit jantung. Maka, lebih baik menjaga tingkat kolesterol antara 151-250 mm/dL agar terhindar dari penyakit jantung.')




    st.markdown("### **8. Apakah kadar gula darah mempengaruhi munculnya penyakit jantung?**")
    plt.figure(figsize=(6, 5))
    ax = sns.countplot(data=df, x='FastingBS', hue='HeartDisease')

    #  Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Fasting Blood Sugar')
    st.pyplot(plt)
    st.write('Keterangan:')
    st.write('0 = Kadar gula darah < 120 mg/dL')
    st.write('1 = Kadar gula darah > 120 mg/dL')
    st.write('Ya. Tampak bahwa sebagian besar orang yang memiliki kadar gula darah di atas 120 mg/dL memiliki penyakit jantung.')
    st.write('Hal tersebut masuk akal karena tingginya kadar gula darah dapat merusak pembuluh darah dan menyebabkan komplikasi penyakit jantung serius.')



    st.markdown("### **9. Bagaimana relasi resting electrocardiogram terhadap penyakit jantung?**")
    plt.figure(figsize=(6, 5))
    ax = sns.countplot(data=df, x='RestingECG', hue='HeartDisease')

    #  Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Resting Electrocardiogram ')
    st.pyplot(plt)
    st.write('Tampak bahwa tidak ada perbedaan yang signifikan antara ketiga hasil dari resting electrocardiogram terhadap penyakit jantung.')



    st.markdown("### **10. Bagaimana pengaruh tingkat depresi segmen ST terhadap penyakit jantung?**")
    plt.figure(figsize=(10, 5))
    ax = sns.histplot(data=df, x='Oldpeak', hue='HeartDisease')

    plt.title('Heart Disease Berdasarkan Tingkat Depresi Segmen ST')
    st.pyplot(plt)
    st.write('Tampak bahwa orang yang memiliki hasil tes depresi segmen ST di atas 1 menderita penyakit jantung.')
    st.write('Dengan kata lain, semakin besar tingkat depresi segmen ST, maka semakin besar pula kemungkinan menderita penyakit jantung.')




    st.markdown("### **11. Apakah angina akibat olahraga dapat mengindikasikan seseorang menderita penyakit jantung?**")
    plt.figure(figsize=(6, 5))
    ax = sns.countplot(data=df, x='ExerciseAngina', hue='HeartDisease')

    #  Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Angina Akibat Olahraga')
    st.pyplot(plt)
    st.write('Ya, munculnya angina setelah berolahraga dapat menjadi indikator bahwa seseorang menderita penyakit jantung.')
    st.write('Tampak perbedaan yang sangat signifikan pada grafik di atas bahwa sebagian besar orang yang mengalami angina setelah olahraga ternyata menderita penyakit jantung.')





    st.markdown("### **12. Apakah tingkat kemiringan segmen ST dapat mengindikasikan penyakit jantung?**")
    plt.figure(figsize=(6, 5))
    ax = sns.countplot(data=df, x='ST_Slope', hue='HeartDisease')

    #  Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Heart Disease Berdasarkan Kemiringan Segmen ST')
    st.pyplot(plt)
    st.write('Ya, kemiringan segmen ST dapat menjadi indikasi apakah seseorang menderita penyakit jantung atau tidak.')
    st.write('Tampak bahwa sebagian besar orang yang memiliki kemiringan segmen ST datar dan menurun ternyata menderita penyakit jantung.')
    st.write('Jika hasil tes ST seseorang menunjukkan bahwa segmen ST-nya datar atau menurun, maka orang tersebut memiliki kemungkinan besar menderita penyakit jantung.')




    st.markdown("## **Kesimpulan**")
    st.write('**Ciri-ciri orang menderita penyakit jantung:**')
    st.write('1. Detak jantung maksimal di bawah 130 bpm')
    st.write('2. Memiliki sakit dada asymptomatic')
    st.write('3. Memiliki kadar gula darah di atas 120 mg/dL')
    st.write('4. Memiliki kolesterol di atas 251 mm/dL')
    st.write('5. Memiliki hasil tes depresi segmen ST di atas 1')
    st.write('6. Mengalami angina setelah berolahraga')
    st.write('7. Hasil tes kemiringan segmen ST datar atau menurun')
    st.write('8. Laki-laki dan orang yang berusia di atas 51 memiliki kemungkinan lebih besar menderita penyakit jantung')

