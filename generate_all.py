"""
Generate KTI article content
"""
exec(open('/opt/data/kti/kti_lib.py').read())

# TITLE
heading("TAQFIS: TAQWA-BASED FOOD INTEGRITY SYSTEM", 0)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(12)
p.paragraph_format.line_spacing = 1.5
r = p.add_run("Integrasi Ekoteologi, Zakat Pertanian-Bahari, dan Kebijakan Pangan dalam Perspektif Al-Quran sebagai Solusi Ketahanan Pangan Nasional")
r.font.name = 'Times New Roman'
r.font.size = Pt(12)

# PENDAHULUAN
heading("Pendahuluan")

par("Ketahanan pangan nasional Indonesia saat ini berada dalam posisi yang paradoksal. Di satu sisi, Indonesia dikenal sebagai negara agraris-maritim dengan kekayaan sumber daya alam yang melimpah. Di sisi lain, peringkat Global Food Security Index (GFSI) 2022 menempatkan Indonesia di posisi 63 dari 113 negara (Economist Impact, 2022). Indonesia masih mengimpor beras sekitar 3,3 juta ton pada tahun 2024 (BPS, 2024), sementara food loss and waste mencapai 20,93 juta ton per tahun dan menempatkan Indonesia sebagai penghasil sampah makanan terbesar kedua di dunia (UNEP Food Waste Index Report, 2024). Kerugian ekonomi akibat food loss and waste diperkirakan mencapai Rp 213 hingga Rp 551 triliun per tahun (Bappenas, 2021).")

par("Paradoks lain yang tidak kalah penting adalah kenyataan bahwa pada saat yang sama, negara justru membiarkan bahkan memfasilitasi kemaksiatan struktural. Pada Februari 2026, pemerintah Indonesia secara resmi menyetujui impor minuman beralkohol dari Amerika Serikat dengan alasan meningkatkan daya saing destinasi pariwisata (Kompas, 22 Februari 2026). Keputusan ini mendapat teguran keras dari Majelis Ulama Indonesia (MUI) yang mengingatkan agar jangan membesarkan yang haram demi kepentingan ekonomi (Maklumat.id, 2026). Sementara itu, di tingkat daerah, terdapat 452 supermarket di Bali yang terbukti menjual minuman beralkohol tanpa pengawasan ketat (ANTARA News Bali, 2025), dan praktik penjualan miras di minimarket masih marak di berbagai kota (Kompas, 4 Maret 2026).")

par("Fenomena ini menjadi penting ketika dibaca dalam perspektif Al-Quran, khususnya QS Al-Araf ayat 96 yang menyatakan bahwa iman dan taqwa penduduk suatu negeri menjadi kunci terbukanya keberkahan dari langit dan bumi. Pembiaran kemaksiatan secara struktural oleh pemimpin dapat dipahami sebagai bentuk ketiadaan taqwa dalam kebijakan publik. Jika keberkahan adalah prasyarat kelimpahan pangan, maka krisis pangan tidak bisa dilihat semata-mata sebagai masalah teknis-pertanian, melainkan juga sebagai masalah moral-spiritual struktural.")

par("Tulisan ini bertujuan untuk menawarkan sebuah gagasan integratif bernama Taqfis (Taqwa-Based Food Integrity System) yang menghubungkan tiga dimensi: (1) taqwa individu melalui pengendalian konsumsi dan pengurangan food waste, (2) optimalisasi zakat pertanian dan hasil laut sebagai instrumen distribusi pangan, dan (3) seruan kepada pemimpin untuk memberantas kemaksiatan struktural sebagai prasyarat turunnya keberkahan bumi.")

# LANDASAN TEORI
heading("Landasan Teori dan Tinjauan Pustaka")
heading("Konsep Ketahanan Pangan dan Keterbatasannya")

par("Organisasi Pangan dan Pertanian Dunia (FAO) mendefinisikan ketahanan pangan melalui empat pilar: ketersediaan (availability), akses (access), pemanfaatan (utilization), dan stabilitas (stability) (FAO, 1996). Keempat pilar ini bersifat material-empiris dan tidak mempertimbangkan faktor spiritual. Penelitian terkini menunjukkan bahwa meskipun produksi pangan global terus meningkat, kerawanan pangan masih terjadi di berbagai negara, termasuk Indonesia (FAO, 2023). Hal ini mengindikasikan adanya variabel lain yang belum tertangkap oleh model konvensional.")

par("Penelitian tentang food loss and waste di Indonesia oleh Bappenas (2021) menemukan bahwa 44% food loss terjadi pada tahap konsumsi rumah tangga, yang menunjukkan bahwa perilaku konsumtif dan pemborosan menjadi faktor dominan. Problem ini jarang dibahas dari sudut pandang spiritual, padahal Al-Quran secara tegas melarang perilaku israf (berlebihan) dalam QS Al-Araf ayat 31.")

heading("Konsep Taqwa dalam Al-Quran")

par("Taqwa secara etimologis berasal dari akar kata waqa-yaqi-wiqayah yang berarti menjaga atau melindungi. Dalam terminologi Al-Quran, taqwa memiliki dimensi vertikal (hubungan dengan Allah) dan horizontal (hubungan dengan sesama dan alam). Ibnu Katsir dalam tafsirnya menjelaskan bahwa taqwa mencakup tiga hal: menjalankan perintah Allah, menjauhi larangan-Nya, dan konsisten dalam keduanya dalam segala kondisi (Ibnu Katsir, 2000).")

par("Ayat utama dalam pembahasan ini adalah QS Al-Araf ayat 96:")

arap("وَلَوْ أَنَّ أَهْلَ الْقُرَىٰ آمَنُوا وَاتَّقَوْا لَفَتَحْنَا عَلَيْهِمْ بَرَكَاتٍ مِنَ السَّمَاءِ وَالْأَرْضِ", '"Sekiranya penduduk negeri-negeri beriman dan bertakwa, pasti Kami akan melimpahkan kepada mereka berkah dari langit dan bumi." (QS Al-Araf: 96)')

par("Dalam tafsir Al-Mishbah, Quraish Shihab menjelaskan bahwa ayat ini menunjukkan hubungan kausal antara iman dan taqwa dengan keberkahan alam. Berkah (barakah) di sini bukan sekadar bertambahnya kuantitas, melainkan juga kualitas dan manfaat dari sumber daya alam (Shihab, 2002). Dengan kata lain, kelimpahan pangan dan kesejahteraan tidak semata-mata ditentukan oleh faktor teknis, melainkan juga oleh kondisi spiritual masyarakat dan pemimpinnya.")

par("Ibnu Katsir dalam tafsirnya menambahkan bahwa ayat ini mengandung janji Allah sekaligus peringatan. Janji berupa keberkahan bagi yang beriman dan bertakwa, serta ancaman berupa musibah dan paceklik bagi yang ingkar. Konteks ayat ini turun berkaitan dengan kondisi penduduk suatu negeri yang mendustakan para rasul, sehingga Allah menimpakan berbagai bencana termasuk kelaparan dan kekurangan buah-buahan (Ibnu Katsir, 2000).")

heading("Ayat-Ayat Pendukung")

par("Selain QS Al-Araf:96, terdapat beberapa ayat lain yang relevan dengan ketahanan pangan:")

arap("Pertama, QS Al-Araf ayat 31: يَا بَنِي آدَمَ خُذُوا زِينَتَكُمْ عِندَ كُلِّ مَسْجِدٍ وَكُلُوا وَاشْرَبُوا وَلَا تُسْرِفُوا إِنَّهُ لَا يُحِبُّ الْمُسْرِفِينَ", '"...Makan dan minumlah, tetapi jangan berlebihan. Sesungguhnya Allah tidak menyukai orang yang berlebihan."')

par("Ayat ini menjadi landasan normatif larangan israf (pemborosan) dalam konsumsi pangan. Dalam kitab Ihya Ulumuddin, Imam Al-Ghazali menjelaskan bahwa adab makan termasuk bagian dari muamalah maa Allah (hubungan hamba dengan Tuhannya). Mengontrol konsumsi bukan sekadar gaya hidup sehat, melainkan bentuk ketaatan kepada Allah.")

arap("Kedua, QS Ath-Thalaq ayat 2-3: وَمَنْ يَتَّقِ اللَّهَ يَجْعَلْ لَّهُ مَخْرَجًا . وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ", '"Barangsiapa bertakwa kepada Allah niscaya Dia akan mengadakan baginya jalan keluar dan memberinya rezeki dari arah yang tidak disangka-sangkanya."')

par("Ayat ini relevan dalam konteks produksi pangan. Jaminan rezeki dari Allah bagi yang bertakwa menunjukkan bahwa keberhasilan sektor pertanian dan perikanan tidak semata-mata bergantung pada modal dan teknologi, tetapi juga pada kualitas spiritual para pelakunya.")

arap("Ketiga, QS Al-Anam ayat 141: كُلُوا مِنْ ثَمَرِهِ إِذَا أَثْمَرَ وَآتُوا حَقَّهُ يَوْمَ حَصَادِهِ", '"...Makanlah dari buahnya (yang bermacam-macam itu) apabila ia berbuah, dan tunaikanlah haknya di hari memetik hasilnya."')

par("Ayat ini menjadi dasar kewajiban zakat pertanian (zakat az-zari). Para ulama menetapkan nisab zakat pertanian sebesar 5 wasaq (653 kg gabah atau 520 kg beras) dengan kadar 10% untuk tanaman yang diairi dengan air alami dan 5% untuk yang menggunakan irigasi buatan (Al-Qardhawi, 2005).")

arap("Keempat, QS An-Nahl ayat 14: وَهُوَ الَّذِي سَخَّرَ الْبَحْرَ لِتَأْكُلُوا مِنْهُ لَحْمًا طَرِيًّا", '"Dan Dialah yang menundukkan lautan agar kamu dapat memakan daging segar darinya."')

par("Sebagai negara maritim dengan 17.000 pulau dan luas laut 6,4 juta km persegi, potensi sumber daya perikanan Indonesia sangat besar. Zakat hasil laut (zakat al-bahri) merupakan instrumen yang belum teroptimalkan secara sistematis.")

heading("Research Gap")

par("Berdasarkan penelusuran literatur, ditemukan bahwa belum ada penelitian yang secara eksplisit menghubungkan konsep taqwa dalam Al-Quran dengan indikator ketahanan pangan. Model ketahanan pangan yang ada (FAO, 1996; Global Food Security Index, 2022) hanya mengukur aspek material. Demikian pula, literatur tentang zakat belum banyak mengkaji potensi zakat pertanian dan hasil laut secara integratif dalam kerangka ketahanan pangan. Sementara itu, kajian tentang food waste di Indonesia lebih banyak dilihat dari perspektif lingkungan dan ekonomi, belum dari perspektif teologis sebagai pelanggaran terhadap larangan israf. Tulisan ini mengisi research gap tersebut dengan menawarkan pendekatan integratif yang menggabungkan ekoteologi, zakat, dan kebijakan publik.")

# TAWARAN GAGASAN
heading("Tawaran Gagasan: Taqfis (Taqwa-Based Food Integrity System)")

par("Taqfis adalah akronim dari Taqwa-Based Food Integrity System, sebuah konsep integratif yang menempatkan taqwa sebagai variabel utama dalam sistem ketahanan pangan. Gagasan ini terdiri dari empat pilar yang saling terkait: taqwa individu, taqwa farming berbasis pesantren, optimalisasi zakat pertanian dan hasil laut, serta barakah metrics sebagai indikator baru ketahanan pangan.")

heading("Pilar 1: Taqwa Individu - Gerakan No Israf, Save Food")

par("Pilar pertama berangkat dari kesadaran bahwa perubahan harus dimulai dari diri sendiri. QS Al-Araf:31 secara eksplisit melarang israf (pemborosan) dalam konsumsi. Dalam konteks Indonesia yang menghasilkan 20,93 juta ton food waste per tahun, larangan ini menjadi sangat relevan. Gerakan No Israf dapat dimulai dari langkah-langkah sederhana: membuat daftar belanja sebelum berbelanja, mengolah kembali makanan sisa, dan membiasakan pola konsumsi ambil secukupnya, habiskan apa yang diambil.")

par("Jika setiap individu Muslim Indonesia mengurangi food waste sebanyak 100 gram per hari, maka secara nasional akan terselamatkan sekitar 10.000 ton pangan per hari. Dalam setahun, angka ini mencapai 3,65 juta ton pangan yang dapat dialokasikan kepada masyarakat yang membutuhkan. Yang lebih penting, gerakan ini mengubah paradigma dari membuang makanan adalah soal pribadi menjadi membuang makanan adalah pelanggaran terhadap perintah Allah.")

heading("Pilar 2: Taqwa Farming - Pesantren sebagai Living Lab Kemandirian Pangan")

par("Pilar kedua memanfaatkan potensi besar pesantren di Indonesia yang berjumlah sekitar 39.000 unit (Kemenag RI, 2024). Banyak pesantren telah mempraktikkan kemandirian pangan, seperti Pondok Pesantren Al-Ittifaq di Bandung yang sukses mengembangkan agribisnis sayuran organik. Program Kementerian Agama tentang Kemandirian Pangan Pesantren (2022) menjadi landasan kebijakan yang mendukung pilar ini.")

par("Model Taqwa Farming mengintegrasikan prinsip ihsan (QS Al-Qashash:77) ke dalam praktik pertanian. Prinsip ini mencakup: (a) pertanian organik yang ramah lingkungan sebagai bentuk menjaga bumi (QS Al-Araf:56), (b) penerapan fiqih pertanian dalam pengelolaan lahan dan hasil panen, dan (c) distribusi kelebihan panen melalui mekanisme zakat pertanian dan sedekah kepada masyarakat sekitar.")

heading("Pilar 3: Optimalisasi Zakat Az-Zari dan Zakat Al-Bahri")

par("Pilar ketiga berfokus pada optimalisasi instrumen zakat yang terkait dengan sumber daya pangan. Zakat pertanian (az-zari) memiliki landasan kuat dalam QS Al-Anam:141. Potensi zakat nasional Indonesia mencapai Rp 327 triliun per tahun, namun realisasi penghimpunan baru sekitar Rp 33 triliun (BAZNAS Outlook, 2023). Potensi zakat pertanian dan hasil laut belum terpetakan secara sistematis.")

par("Model yang diusulkan adalah Lumbung Pangan Zakat (Zakat Food Bank), yaitu: (a) petani dan nelayan membayar zakat dalam bentuk hasil bumi atau tangkapan, (b) BAZNAS dan LAZ mendistribusikan zakat pangan ini secara langsung kepada mustahik yang mengalami kerawanan pangan, dan (c) kelebihan distribusi digunakan untuk program pemberdayaan petani dan nelayan kecil.")

heading("Pilar 4: Barakah Metrics - Indeks Keberkahan Pangan Nasional")

par("Pilar keempat adalah gagasan paling inovatif: menambahkan Indeks Keberkahan sebagai pilar kelima dalam kerangka ketahanan pangan, melengkapi empat pilar FAO (availability, access, utilization, stability). Indeks ini mencakup: (1) tingkat food loss and waste nasional, (2) tingkat optimalisasi zakat pertanian dan hasil laut, (3) jumlah komunitas religius yang mandiri pangan, dan (4) indeks kepuasan masyarakat terhadap kebijakan pangan pemerintah.")

par("Pilar ini didasarkan pada argumen bahwa ketahanan pangan tidak boleh diukur semata-mata dari ketersediaan beras di gudang Bulog. Ukuran yang lebih fundamental adalah apakah suatu negeri diberkahi pangannya - dalam arti cukup, halal, thayyib, dan didistribusikan secara adil.")

heading("Seruan kepada Pemimpin: Berantas Kemaksiatan Struktural")

par("Bagian ini merupakan inti dari relevansi sosial tulisan ini. Berdasarkan data yang telah dipaparkan, negara dalam beberapa hal justru memfasilitasi atau membiarkan kemaksiatan secara struktural. Impor minuman beralkohol atas nama pariwisata (2026), maraknya penjualan miras di minimarket, serta konten hiburan yang mengarah pada kemusyrikan dan pergaulan bebas adalah fakta yang tidak bisa diabaikan.")

par("Dalam kerangka QS Al-Araf:96, pembiaran kemaksiatan ini memiliki konsekuensi teologis: hilangnya keberkahan bumi. Sebagaimana hadits riwayat Abu Daud: Tidaklah suatu kaum membiarkan kemaksiatan di tengah-tengah mereka, lalu mereka mampu mengubahnya, melainkan Allah akan meratakan azab kepada mereka semua. (HR. Abu Daud, dishahihkan Al-Albani).")

par("Seruan kepada pemimpin: (1) hentikan kebijakan yang memfasilitasi kemaksiatan, (2) perkuat pengawasan terhadap konten hiburan dan peredaran barang haram, (3) jadikan nilai-nilai Al-Quran sebagai pedoman dalam membangun ketahanan pangan, dan (4) integrasikan pemberantasan kemaksiatan ke dalam kebijakan ketahanan pangan nasional.")

par("Pendekatan ini bukan berarti mengabaikan aspek teknis ketahanan pangan - irigasi, pupuk, teknologi pertanian, dan stabilitas harga tetaplah penting. Namun, aspek teknis tanpa keberkahan akan menghasilkan hasil yang tidak optimal.")

# PENUTUP
heading("Penutup")
heading("Kesimpulan")

par("Krisis ketahanan pangan Indonesia tidak dapat dipahami semata-mata sebagai persoalan teknis-pertanian. Melalui perspektif QS Al-Araf:96, krisis pangan adalah cerminan hilangnya keberkahan yang disebabkan oleh lemahnya iman dan taqwa - baik pada level individu maupun struktural. Pembiaran kemaksiatan oleh pemimpin, seperti impor miras, menjadi indikator bahwa nilai-nilai ketakwaan belum menjadi landasan kebijakan publik.")

par("Konsep Taqfis (Taqwa-Based Food Integrity System) menawarkan solusi integratif yang mencakup: gerakan No Israf sebagai manifestasi taqwa individu, pengembangan pesantren sebagai living lab kemandirian pangan, optimalisasi zakat pertanian dan hasil laut, serta indeks keberkahan pangan sebagai indikator baru ketahanan pangan.")

heading("Rekomendasi")

par("(1) Pemerintah agar menghentikan kebijakan yang memfasilitasi kemaksiatan dan memperkuat regulasi pengawasan peredaran barang haram. (2) Kementerian Agama dan BAZNAS agar mengoptimalkan Zakat Az-Zari dan Zakat Al-Bahri sebagai instrumen ketahanan pangan. (3) Pesantren agar dikembangkan sebagai pusat kemandirian pangan yang mengintegrasikan nilai-nilai Al-Quran dengan praktik pertanian modern. (4) Masyarakat Muslim agar memulai perubahan dari diri sendiri dengan mengendalikan konsumsi dan mengurangi food waste sebagai bagian dari implementasi taqwa.")

# DAFTAR PUSTAKA
heading("Daftar Pustaka")

refs = [
    "Al-Qardhawi, Y. (2005). Fiqh al-Zakah. Beirut: Muassasah al-Risalah.",
    "Bappenas. (2021). Laporan Kajian Food Loss and Waste di Indonesia. Jakarta: Bappenas.",
    "BAZNAS. (2023). Outlook Zakat Nasional 2023. Jakarta: Pusat Kajian Strategis BAZNAS.",
    "Economist Impact. (2022). Global Food Security Index 2022.",
    "FAO. (1996). Rome Declaration on World Food Security. Rome: FAO.",
    "FAO. (2023). The State of Food Security and Nutrition in the World 2023. Rome: FAO.",
    "Ibnu Katsir, I. (2000). Tafsir Al-Quran Al-Azhim. Riyadh: Dar Thayyibah.",
    "Shihab, M. Q. (2002). Tafsir Al-Mishbah. Jakarta: Lentera Hati.",
    "UNEP. (2024). Food Waste Index Report 2024. Nairobi: UNEP.",
]
blank()
ref_line("Sumber Berita:")
ref_line("ANTARA News Bali. (2025). Disperindag Temukan 452 Supermarket Jual Minuman Beralkohol.")
ref_line("Kompas.com. (22 Feb 2026). Pemerintah Sebut Impor Minuman Alkohol dari AS demi Genjot Pariwisata.")
ref_line("Kompas.com. (4 Mar 2026). Minimarket di Jakbar Disegel karena Jual Miras Golongan A.")
ref_line("Maklumat.id. (2026). Impor Miras AS Demi Pariwisata, MUI Tegur Pemerintah.")
ref_line("Tempo.co. (8 Apr 2026). Penjualan Minuman Keras Dilarang, Peretail Dipanggil.")

for ref in refs:
    ref_line(ref)

output_path = "/opt/data/kti/KTI_Taqfis_Ketahanan_Pangan.docx"
save(output_path)
print(f"SUKSES! Dokumen tersimpan di: {output_path}")
print(f"Ukuran: {os.path.getsize(output_path)} bytes")
