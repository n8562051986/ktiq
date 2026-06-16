"""Generate KTI - SIMBOTAK v3 FINAL"""
with open('/opt/data/kti/kti_lib.py') as f:
    exec(f.read())

def ref_bold(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-1.0)
    r.font.name = 'Times New Roman'; r.font.size = Pt(11); r.font.bold = True

def model_line(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.line_spacing = 1.5
    r.font.name = 'Times New Roman'; r.font.size = Pt(11); r.font.bold = True

def arrw():
    p = doc.add_paragraph()
    r = p.add_run('\u25bc')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.line_spacing = 1.5
    r.font.name = 'Times New Roman'; r.font.size = Pt(11)

heading("SIMBOTAK: SISTEM INTEGRITAS MAKANAN BERBASIS OPTIMALISASI TAKWA DAN KEBERKAHAN", 0)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(12)
p.paragraph_format.line_spacing = 1.5
r = p.add_run("Integrasi Adab Konsumsi, Zakat, dan Kepemimpinan Bertakwa untuk Ketahanan Pangan Nasional")
r.font.name = 'Times New Roman'; r.font.size = Pt(12)

heading("Pendahuluan")

par("Ketahanan pangan Indonesia berada dalam posisi paradoksal. Peringkat Global Food Security Index (GFSI) 2022 menempatkan Indonesia di posisi 63 dari 113 negara (Economist Impact, 2022). Impor beras masih mencapai sekitar 3,3 juta ton (BPS, 2024), sementara food loss and waste mencapai 20,93 juta ton per tahun, menempatkan Indonesia di peringkat kedua global (UNEP Food Waste Index Report, 2024). Kerugian ekonomi akibat food waste diperkirakan Rp 213-551 triliun per tahun, cukup untuk memberi makan 125 juta orang (Bappenas, 2021).")

par("Di sisi lain, kemaksiatan di ruang publik masih marak. Kasus pencucian uang hasil judi online Rp 297 miliar di Surabaya (Kompas, 3 Juni 2026), peringatan Wali Kota Bandung tentang ASN yang terlibat judi online pada momentum Piala Dunia 2026 (Kompas, 15 Juni 2026), dan impor minuman alkohol yang mendapat teguran keras MUI (Maklumat, 2026) menunjukkan bahwa problem moral belum mendapat perhatian serius dalam kebijakan publik negara. Ironisnya, di tengah maraknya kemaksiatan ini, rakyat kecil yang tidak terlibat pun ikut merasakan dampak sosial dan ekonominya.")

par("Tulisan ini menawarkan SIMBOTAK (Sistem Integritas Makanan Berbasis Optimalisasi Takwa dan Keberkahan), sebuah model konseptual yang menghubungkan adab konsumsi Islami, optimalisasi zakat, dan kepemimpinan bertakwa dalam satu kerangka utuh. Dalam perspektif normatif QS Al-Araf:96, rendahnya ketakwaan dipandang sebagai faktor yang dapat mengurangi keberkahan kehidupan sosial, termasuk dalam sektor pangan. Melalui model ini, penulis berupaya menjembatani pendekatan spiritual yang sering dianggap terpisah dari kebijakan pangan publik.")

heading("Landasan Teori dan Tinjauan Pustaka")
heading("Ketahanan Pangan dan Dimensi yang Terabaikan")

par("FAO mendefinisikan ketahanan pangan melalui empat pilar: availability, access, utilization, dan stability (FAO, 1996). Keempat pilar ini bersifat material-empiris dan belum mempertimbangkan faktor perilaku konsumsi. Bappenas (2021) mencatat 44% food loss terjadi pada konsumsi rumah tangga, menunjukkan dimensi perilaku yang luput dari model konvensional. Sementara itu, ekonomi perilaku (behavioral economics) menunjukkan bahwa kebiasaan konsumsi sangat dipengaruhi oleh nilai dan norma yang dianut individu, bukan semata-mata oleh ketersediaan atau harga.")

heading("Konsep Takwa dalam Al-Quran")

par("Takwa secara etimologis berarti menjaga atau melindungi diri. Ayat utama dalam pembahasan ini adalah QS Al-Araf:96:")

arap('\u0648\u064e\u0644\u064e\u0648\u0652 \u0623\u064e\u0646\u0651\u064e \u0623\u064e\u0647\u0652\u0644\u064e \u0627\u0644\u0652\u0642\u064f\u0631\u064e\u0649\u0670 \u0622\u0645\u064e\u0646\u064f\u0648\u0627 \u0648\u064e\u0627\u062a\u0651\u064e\u0642\u064e\u0648\u0652\u0627 \u0644\u064e\u0641\u064e\u062a\u064e\u062d\u0652\u0646\u064e\u0627 \u0639\u064e\u0644\u064e\u064a\u0652\u0647\u0650\u0645\u0652 \u0628\u064e\u0631\u064e\u0643\u064e\u0627\u062a\u064d \u0645\u0650\u0646\u064e \u0627\u0644\u0633\u0651\u064e\u0645\u064e\u0627\u0621\u0650 \u0648\u064e\u0627\u0644\u0652\u0623\u064e\u0631\u0652\u0636\u0650', '"Sekiranya penduduk negeri-negeri beriman dan bertakwa, pasti Kami akan melimpahkan kepada mereka berkah dari langit dan bumi." (QS Al-Araf:96)')

par("Quraish Shihab (2002) dalam Tafsir Al-Mishbah menafsirkan barakah sebagai kualitas dan keberlanjutan manfaat sumber daya, bukan sekadar kuantitas. Dalam perspektif normatif ini, rendahnya ketakwaan dipandang dapat mengurangi keberkahan sosial-ekonomi. Ayat pendukung meliputi: (a) QS Al-Araf:31 tentang larangan israf yang menjadi landasan pengendalian konsumsi; (b) QS Ath-Thalaq:2-3 tentang jaminan rezeki bagi yang bertakwa; (c) QS At-Taubah:103 tentang fungsi zakat yang membersihkan harta dan jiwa; serta (d) QS Saba:15 tentang pelajaran dari negeri Saba yang kehilangan keberkahan karena kesombongan.")

heading("Adab Makan dan Hadits Makan Bersama")

par("Rasulullah Saw. mengajarkan adab makan yang sarat nilai efisiensi pangan. Hadits-hadits shahih meriwayatkan: membaca basmalah sebelum makan (HR. Muslim), makan dengan tangan kanan (HR. Bukhari-Muslim), tidak mencela makanan apa pun yang dihidangkan (HR. Bukhari-Muslim), menjilat jari dan membersihkan piring hingga tidak tersisa makanan (HR. Muslim). Khusus tentang makan bersama, Rasulullah bersabda: Makanan untuk dua orang cukup untuk tiga orang, dan makanan untuk tiga orang cukup untuk empat orang (HR. Bukhari no. 5392, HR. Muslim no. 2058). Dalam riwayat lain, beliau bersabda: Berkumpullah kalian dalam makanan kalian, karena sesungguhnya keberkahan itu turun bersama kebersamaan (HR. Abu Daud no. 3764, dishahihkan Al-Albani). Hadits-hadits ini menegaskan bahwa makan bersama bukan sekadar tradisi sosial, melainkan mengandung prinsip efisiensi dan distribusi keberkahan yang relevan untuk menekan food waste.")

heading("Research Gap")

par("Penulis belum menemukan penelitian yang secara spesifik mengintegrasikan konsep takwa, zakat, adab konsumsi, dan kepemimpinan ke dalam satu model ketahanan pangan nasional sebagaimana yang ditawarkan melalui SIMBOTAK. Kajian zakat selama ini lebih banyak berfokus pada fikih individual dan penghitungan nisab (Al-Qardhawi, 2005), sementara studi food waste didominasi perspektif lingkungan dan ekonomi (UNEP, 2024; Bappenas, 2021). SIMBOTAK menawarkan jembatan antar-dimensi yang selama ini berjalan sendiri-sendiri dalam satu kerangka yang sistematis.")

heading("Tawaran Gagasan: SIMBOTAK")
heading("Model Konseptual")

par("SIMBOTAK terdiri dari tiga jalur intervensi yang bermuara pada ketahanan pangan nasional:")

model_line("JALUR I: TAKWA INDIVIDU"); arrw(); model_line("Pengurangan Israf & Food Waste"); arrw(); model_line("Efisiensi Konsumsi Nasional")
blank()
model_line("JALUR II: ZAKAT"); arrw(); model_line("Redistribusi Pangan"); arrw(); model_line("Penguatan Kelompok Rentan")
blank()
model_line("JALUR III: KEPEMIMPINAN BERTAKWA"); arrw(); model_line("Integritas Kebijakan"); arrw(); model_line("Kepercayaan Publik")
blank()
model_line("--- KETIGA JALUR ---"); arrw(); model_line("KEBERKAHAN SOSIAL"); arrw(); model_line("KETAHANAN PANGAN NASIONAL")
blank()
par("Model ini bersifat hipotetis-konseptual dan memerlukan pengujian empiris lebih lanjut. Ketiga jalur tersebut bekerja secara simultan: individu yang bertakwa akan membatasi konsumsi dan mengurangi israf, zakat menyalurkan kelebihan pangan ke kelompok rentan, dan pemimpin yang bertakwa menciptakan ekosistem kebijakan yang mendukung keberkahan.")

heading("Pilar 1: Takwa Individu dan Adab Makan")

par("Pilar ini bertumpu pada kesadaran bahwa efisiensi pangan dimulai dari individu. QS Al-Araf:31 melarang israf, sementara hadits-hadits adab makan dan makan bersama mengajarkan penghargaan terhadap makanan. Pesantren (sekitar 39.000 unit, Kemenag, 2024) dan program makan masyarakat menjadi wahana strategis untuk mensosialisasikan adab makan ini. Jika setiap individu mengurangi food waste 100 gram/hari, secara nasional terselamatkan sekitar 10.000 ton pangan per hari. Indikator operasional: penurunan food waste rumah tangga (%), jumlah lembaga yang mengintegrasikan edukasi adab makan.")

heading("Pilar 2: Zakat untuk Keberkahan dan Solidaritas Sosial")

par("Zakat sebagaimana disebut dalam QS At-Taubah:103 berfungsi membersihkan harta (tuthahhiruhum) dan menyucikan jiwa (tuzakkihim). Potensi zakat nasional mencapai Rp 327 triliun, namun realisasi baru Rp 33 triliun (BAZNAS, 2023). Kesenjangan ini menunjukkan urgensi optimalisasi. Implikasi sosial zakat yang dapat diamati meliputi: redistribusi pendapatan dari muzaki ke mustahik, penguatan daya beli kelompok rentan terhadap pangan, serta pengurangan kesenjangan konsumsi antar-kelompok masyarakat. Indikator operasional: peningkatan penghimpunan zakat (nominal), volume distribusi zakat pangan, dan cakupan mustahik penerima manfaat.")

heading("Pilar 3: Kepemimpinan Bertakwa dan Integritas Kebijakan")

par("Pilar ini memiliki dua sisi argumen yang saling melengkapi. Sisi keagamaan: pemimpin didorong menjadi teladan dalam shalat berjamaah dan kepatuhan berzakat. Shalat berjamaah yang diikuti para pejabat dan staf secara rutin mencerminkan kedisiplinan dan ketundukan kolektif kepada nilai-nilai ilahiah. Sisi kebijakan publik: shalat berjamaah membangun disiplin organisasi yang terukur; zakat memperkuat solidaritas sosial dan jaring pengaman bagi masyarakat miskin; pemberantasan judi online dan pornografi mengurangi kebocoran ekonomi rumah tangga yang mencapai miliaran rupiah; keteladanan pemimpin dalam integritas moral meningkatkan kepercayaan publik terhadap institusi pemerintahan. Indikator: kepatuhan pelaporan zakat ASN, jumlah program integritas dan pembinaan, serta penurunan kasus pelanggaran moral aparatur.")

heading("Indikator Operasional SIMBOTAK")

par("Takwa Konsumsi: penurunan food waste rumah tangga (%), jumlah lembaga dengan program edukasi adab makan. Zakat: peningkatan penghimpunan zakat (nominal), volume distribusi zakat pangan, cakupan mustahik. Kepemimpinan: persentase kepatuhan pelaporan zakat ASN, jumlah program pembinaan integritas, tren penurunan kasus pelanggaran moral. Indikator hasil akhir: indeks ketahanan pangan daerah yang dapat merujuk pada Food Security and Vulnerability Atlas (FSVA) yang diterbitkan Badan Pangan Nasional.")

heading("Penutup")
heading("Kesimpulan")

par("SIMBOTAK menawarkan model konseptual yang mengintegrasikan tiga dimensi yang selama ini berjalan sendiri-sendiri: adab konsumsi Islami, optimalisasi zakat, dan kepemimpinan bertakwa. Dalam perspektif normatif QS Al-Araf:96, ketiga dimensi ini dipandang berkontribusi terhadap keberkahan sosial yang pada gilirannya memperkuat ketahanan pangan nasional. Model ini bersifat hipotetis-konseptual dan memerlukan pengujian empiris lebih lanjut untuk memvalidasi hubungan antarvariabel yang diajukan, misalnya melalui studi lintas provinsi dengan data FSVA dan data keagamaan.")

heading("Rekomendasi")

par("(1) Pemerintah perlu mengambil langkah tegas memberantas kemaksiatan struktural yang menggerus keberkahan sosial, khususnya judi online, pornografi, dan peredaran barang haram. (2) Pemimpin di semua level perlu menjadi teladan dalam ketakwaan, disiplin organisasi, dan kepatuhan berzakat. (3) BAZNAS dan LAZ perlu mengoptimalkan penghimpunan dan penyaluran zakat, khususnya untuk program ketahanan pangan dan pemberdayaan kelompok rentan. (4) Masyarakat, pesantren, dan lembaga pendidikan perlu menghidupkan kembali adab makan Rasulullah sebagai bagian dari pendidikan karakter dan pengurangan food waste. (5) Penelitian lanjutan diperlukan untuk menguji secara empiris hubungan antarvariabel dalam model SIMBOTAK menggunakan data ketahanan pangan dan keagamaan di tingkat provinsi. Wallahu alam bishawab.")

heading("Daftar Pustaka")

ref_bold("Sumber Berita:")
ref_line("Kompas.com. (15 Juni 2026). Farhan Ancam Sanksi Berat ASN yang Terlibat Judi Online.")
ref_line("Kompas.com. (3 Juni 2026). Cuci Uang Hasil Judi Online Rp 297 Miliar di Surabaya.")
ref_line("Maklumat.id. (2026). Impor Miras AS, MUI Tegur Pemerintah.")
blank()
ref_bold("Buku dan Laporan:")
for r in [
    "Bappenas. (2021). Laporan Kajian Food Loss and Waste di Indonesia. Jakarta.",
    "BAZNAS. (2023). Outlook Zakat Nasional 2023. Jakarta: Puskas BAZNAS.",
    "Economist Impact. (2022). Global Food Security Index 2022.",
    "FAO. (1996). Rome Declaration on World Food Security. Rome.",
    "Ibnu Katsir. (2000). Tafsir Al-Quran Al-Azhim. Riyadh: Dar Thayyibah.",
    "Shihab, M.Q. (2002). Tafsir Al-Mishbah. Jakarta: Lentera Hati.",
    "UNEP. (2024). Food Waste Index Report 2024. Nairobi.",
]:
    ref_line(r)
blank()
ref_bold("Referensi Hadits:")
ref_line("HR. Bukhari, Kitab al-At'imah, no. 5392.")
ref_line("HR. Muslim, Kitab al-At'imah, no. 2019-2020, 2058.")
ref_line("HR. Abu Daud, Kitab al-At'imah, no. 3764 (keberkahan makan bersama).")
ref_line("HR. Tirmidzi, no. 1807.")

out = "/opt/data/kti/KTI_SIMBOTAK_v3.docx"
save(out)
import os; print(f"OK: {out} ({os.path.getsize(out)} bytes)")

# Word count
from docx import Document
d = Document(out)
words = sum(len(p.text.split()) for p in d.paragraphs if p.text.strip())
print(f"Total kata: {words}")
print("DONE")
