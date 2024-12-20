# Proyek Akhir: Menyelesaikan Permasalahan Dropout Mahasiswa di Kiyut Institute 🏫

## Business Understanding

Kiyut Institute merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Kiyut Institute ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

- Bagaimana mengidentifikasi karakteristik mahasiswa yang memiliki risiko tinggi untuk dropout?
- Apakah terdapat pola dropout berdasarkan gender, usia, status pernikahan, dan jurusan?
- Jurusan dan kelompok usia mana yang memiliki tingkat dropout tertinggi?

### Cakupan Proyek

1. Menganalisis data performa mahasiswa dan mencari penyebab dropout.
2. Membuat dashboard performa mahasiswa untuk menampilkan statistik terkait dropout dan memberikan wawasan yang lebih baik.
3. Menyediakan rekomendasi berbasis machine learning untuk mengurangi tingkat dropout.

### Persiapan

Sumber data: [Student Perfomance Dataset](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

Setup environment:

```
#Instal virtual env with conda
conda create --name student_performance python=3.9

#activate virtual env
conda activate student_performance

# Install necessary packages
pip install numpy pandas xgboost scipy plotly matplotlib seaborn sqlalchemy scikit-learn==1.2.2 joblib==1.3.1 streamlit==1.24.0

# Run the Streamlit app
streamlit run app.py
```

## Business Dashboard

Dashboard ini menampilkan berbagai visualisasi terkait performa mahasiswa yang mencakup jumlah total mahasiswa, tingkat dropout, distribusi dropout berdasarkan usia, jenis kelamin, status pernikahan, serta program studi. Dashboard ini berfungsi sebagai alat bagi manajemen untuk memahami pola dropout mahasiswa, mengidentifikasi kelompok usia dan jurusan dengan tingkat dropout tertinggi, serta menganalisis tren berdasarkan gender dan status sosial untuk mendukung pengambilan keputusan yang lebih tepat.

Kiyut Institute Student Performance Dashboard bisa diliat disini: [Tableau Public Dashboard](https://public.tableau.com/views/student-performance/KiyutInstitute?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Dashboard Preview

![image](https://github.com/user-attachments/assets/101ef1a8-b709-4a18-a52a-5f9441cf6e45)


## Menjalankan Sistem Machine Learning

Untuk menjalankan machine learning prototype, ikuti langkah berikut:

```
# Clone the repository
git clone <repository-url>

# Install necessary packages
pip install numpy pandas xgboost scipy plotly matplotlib seaborn sqlalchemy scikit-learn joblib streamlit

# Run the Streamlit app
streamlit run app.py
```

Berikut adalah Link Kiyut Institute Student Dropout Predictor : [Kiyut Institute Student Dropout Prediction App](https://student-performance-predictor-sahrul.streamlit.app/)

## Conclusion

Dashboard ini menampilkan berbagai visualisasi terkait performa mahasiswa dengan fokus pada analisis dropout. Tingginya angka **dropout sebesar 32.55%** dari total **3,174 mahasiswa** mengindikasikan masalah serius yang perlu ditangani. Berdasarkan visualisasi, dropout tertinggi terjadi pada m**ahasiswa usia di bawah 20 tahun (392 kasus)** dan **20-29 tahun (468 kasus)**, menunjukkan bahwa mahasiswa muda lebih rentan mengalami dropout. Dari segi gender, **laki-laki** (51%) sedikit lebih mendominasi dibanding **perempuan** (49%), sedangkan dari status pernikahan, mahasiswa **single** menyumbang dropout tertinggi (860 kasus). Dropout juga paling banyak terjadi di program studi seperti **Management (kelas malam)** , **Management reguler**, dan **Nursing**, yang masing-masing mencatat lebih dari **100 kasus**.

### Rekomendasi Action Items

Berikut adalah rekomendasi action items yang harus diterapkan oleh Kiyut Institute agar meningkatkan lulusan dengan reputasi yang baik:

- **Bimbingan Akademik Intensif**: Targetkan mahasiswa muda (di bawah 20) agar mendapatkan dukungan tambahan.
- **Konsultasi Psikologis**: Fokus pada mahasiswa single yang berisiko mengalami dropout.
- **Evaluasi Jurusan dengan Tingkat Dropout Tinggi**: Manajemen dan Nursing perlu evaluasi lebih mendalam.
- **Penerapan Early Warning System (EWS)**: Identifikasi mahasiswa dengan performa rendah secara dini menggunakan model prediktif.
