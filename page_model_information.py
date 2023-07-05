import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

def show_model_information():
    st.title('Model Information')
    st.caption('Awalnya, saya menggunakan 5 model untuk memprediksi penyakit jantung, yaitu:')
    st.caption('1. Logistic Regression')
    st.caption('2. Gradient Boosting Classifier')
    st.caption('3. CatBoost Classifier')
    st.caption('4. Naive Bayes')
    st.caption('5. XGBoost Classifier')
    st.subheader('Berikut adalah akurasi dari setiap model')


    nama_model = ['Logistic Regression', 'Gradient Boosting', 'CatBoost', 'Naive Bayes', 'XGBoost']
    scoreTrainArr = [0.8542234332425068, 0.9019073569482289, 0.8896457765667575, 0.8365122615803815, 0.9373297002724795]
    scoreTestArr = [0.8913043478260869, 0.8913043478260869, 0.9130434782608695, 0.8858695652173914, 0.8804347826086957]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Lebar setiap bar
    bar_width = 0.4

    # Array untuk sumbu x
    x_pos = np.arange(len(nama_model))

    # Plot untuk akurasi train
    train_bars = ax.bar(x_pos, scoreTrainArr, width=bar_width, align='center', alpha=0.8, label='Train Accuracy')

    # Plot untuk akurasi test
    test_bars = ax.bar(x_pos + bar_width, scoreTestArr, width=bar_width, align='center', alpha=0.8, label='Test Accuracy')

    ax.set_xticks(x_pos + bar_width / 2)
    ax.set_xticklabels(nama_model)

    ax.set_ylabel('Accuracy')

    ax.set_title('Model Accuracy Comparison')

    # Untuk memberikan annotation di setiap puncak bar
    for bar1, bar2 in zip(train_bars, test_bars):
        height1 = bar1.get_height()
        height2 = bar2.get_height()
        ax.annotate(f'{height1:.3f}', xy=(bar1.get_x() + bar1.get_width() / 2, height1),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')
        ax.annotate(f'{height2:.3f}', xy=(bar2.get_x() + bar2.get_width() / 2, height2),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    ax.set_ylim(0, 1.05)

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    st.pyplot(fig)

    st.caption('Tampak bahwa model Catboost menghasilkan akurasi tertinggi ketika memprediksi data test. Selain itu, akurasinya pun tidak jauh berbeda dengan akurasi data train.')
    st.caption('Hal tersebut menunjukkan bahwa model Catboost tidak overfitting dan tidak underfitting, serta lebih baik dibandingkan model yang lain.')
    st.subheader('Alasan memilih Catboost:')
    st.caption('Catboost merupakan improvement dari Gradient Boosting yang bekerja dengan cara menggabungkan beberapa model prediksi yang lemah untuk membuat prediksi yang lebih kuat.')
    st.caption('Catboost membuat decision tree menggunakan algoritma Symmetric Binary Spitting yang mampu menghasilkan pohon yang seimbang dan simetris. Hal ini mampu mencegah terjadinya overfitting.')
    st.caption('Oleh karena itu, saya memilih model Catboost untuk memprediksi data yang diinputkan oleh user.')