"""
Generate KTI article content - EXPANDED VERSION for 6-8 pages
"""
exec(open('/opt/data/kti/kti_lib.py').read())

# TITLE
heading("TAQFIS: TAQWA-BASED FOOD INTEGRITY SYSTEM", 0)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(12)
p.paragraph_format.line_spacing = 1.5
r = p.add_run("Integrasi Ekoteologi, Zakat Pertanian-Bahari, dan Kebijakan Pangan\n dalam Perspektif Al-Quran sebagai Solusi Ketahanan Pangan Nasional")
r.font.name = 'Times New Roman'
r.font.size = Pt(12)

# ===================== PENDAHULUAN =====================
heading("Pendahuluan")

par("Ketahanan pangan nasional Indonesia saat ini berada dalam posisi yang paradoksal. Di satu sisi, Indonesia dikenal sebagai negara agraris-maritim dengan kekayaan sumber daya alam yang melimpah. Luas lahan pertanian mencapai jutaan hektar dan laut Indonesia seluas 6,4 juta km persegi menyimpan potensi perikanan yang sangat besar. Di sisi lain, peringkat Global Food Security Index (GFSI) 2022 menempatkan Indonesia di posisi 63 dari 113 negara (Economist Impact, 2022). Indonesia masih mengimpor beras sekitar 3,3 juta ton pada tahun 2024 (BPS, 2024), sementara food loss and waste mencapai 20,93 juta ton per tahun dan menempatkan Indonesia sebagai penghasil sampah makanan terbesar kedua di dunia setelah Arab Saudi (UNEP Food Waste Index Report, 2024). Kerugian ekonomi akibat food loss and waste diperkirakan mencapai Rp 213 hingga Rp 551 triliun per tahun, angka yang cukup untuk memberi makan 125 juta orang setiap harinya (Bappenas, 2021).")

par("Paradoks lain yang tidak kalah penting dan sering luput dari perhatian adalah kenyataan bahwa pada saat yang sama, negara justru membiarkan bahkan memfasilitasi kemaksiatan secara struktural. Pada Februari 2026, pemerintah Indonesia secara resmi menyetujui impor minuman beralkohol dari Amerika Serikat dengan alasan meningkatkan daya saing destinasi pariwisata internasional (Kompas, 22 Februari 2026). Keputusan ini mendapat teguran keras dari Majelis Ulama Indonesia (MUI) yang mengingatkan agar jangan membesarkan yang haram demi kepentingan ekonomi sesaat (Maklumat.id, 2026). Di tingkat daerah, Dinas Perindustrian dan Perdagangan Bali menemukan 452 supermarket yang menjual minuman beralkohol tanpa pengawasan optimal (ANTARA News Bali, 2025), sementara praktik penjualan miras di minimarket masih marak di Jakarta dan berbagai kota lain (Kompas, 4 Maret 2026; Tempo, 8 April 2026).")

par("Tidak hanya itu, konten hiburan yang mengarah pada promosi kemusyrikan juga semakin marak. Film berjudul Syirik Danyang Laut Selatan dirilis dengan mengusung tema mistis berbalut budaya lokal yang dikritik keras karena dianggap melecehkan nilai-nilai agama (Detik.com, Juni 2025). Sementara itu, tingkat kenakalan remaja dan degradasi moral semakin memprihatinkan, dengan Gubernur Jawa Barat mengambil langkah ekstrem mengirim pelajar yang terlibat pergaulan bebas ke barak militer untuk pembinaan (BBC Indonesia, 2025).")

par("Fenomena-fenomena ini menjadi penting ketika dibaca dalam perspektif Al-Quran, khususnya QS Al-Araf ayat 96 yang secara eksplisit menyatakan bahwa iman dan taqwa penduduk suatu negeri menjadi kunci terbukanya keberkahan dari langit dan bumi. Pembiaran kemaksiatan secara struktural oleh pemimpin dapat dipahami sebagai bentuk ketiadaan taqwa dalam kebijakan publik. Jika keberkahan adalah prasyarat kelimpahan pangan, maka krisis pangan yang berkepanjangan tidak bisa dilihat semata-mata sebagai masalah teknis-pertanian, melainkan juga harus dipahami sebagai masalah moral-spiritual struktural yang memerlukan solusi integratif.")

par("Tulisan ini bertujuan untuk menawarkan sebuah gagasan integratif bernama Taqfis (Taqwa-Based Food Integrity System) yang menghubungkan tiga dimensi: (1) taqwa individu melalui pengendalian konsumsi dan pengurangan food waste, (2) optimalisasi zakat pertanian dan hasil laut sebagai instrumen distribusi pangan, dan (3) seruan kepada pemimpin untuk memberantas kemaksiatan struktural sebagai prasyarat turunnya keberkahan bumi. Gagasan ini diharapkan dapat menjadi perspektif baru yang memperkaya diskursus ketahanan pangan yang selama ini didominasi oleh pendekatan teknis-ekonomis.")

# ===================== LANDASAN TEORI =====================
heading("Landasan Teori dan Tinjauan Pustaka")
heading("Konsep Ketahanan Pangan dan Keterbatasannya")

par("Organisasi Pangan dan Pertanian Dunia (FAO) mendefinisikan ketahanan pangan melalui empat pilar utama: ketersediaan (availability), akses (access), pemanfaatan (utilization), dan stabilitas (stability) (FAO, 1996). Keempat pilar ini bersifat material-empiris dan tidak mempertimbangkan faktor spiritual sama sekali. Data terkini dari FAO (2023) menunjukkan bahwa meskipun produksi pangan global terus meningkat, kerawanan pangan masih melanda 691 hingga 783 juta orang di seluruh dunia. Fakta ini mengindikasikan adanya variabel lain yang belum tertangkap oleh model ketahanan pangan konvensional.")

par("Sementara itu, penelitian tentang food loss and waste di Indonesia oleh Bappenas (2021) mengungkap temuan penting: 44% dari total food loss terjadi pada tahap konsumsi rumah tangga. Artinya, hampir setengah dari pemborosan pangan nasional berasal dari perilaku individu dalam mengelola makanan sehari-hari. Problem ini jarang dibahas dari sudut pandang spiritual, padahal Al-Quran secara tegas melarang perilaku israf (berlebihan) dalam QS Al-Araf ayat 31. Ironisnya, di tengah kelimpahan yang disia-siakan, masih ada jutaan rakyat Indonesia yang mengalami kerawanan pangan setiap harinya.")

heading("Konsep Taqwa dalam Al-Quran")

par("Taqwa secara etimologis berasal dari akar kata waqa-yaqi-wiqayah yang berarti menjaga, melindungi, atau menghindarkan diri dari bahaya. Dalam terminologi Al-Quran, taqwa memiliki dimensi vertikal (hubungan dengan Allah) dan horizontal (hubungan dengan sesama manusia dan alam semesta). Ibnu Katsir dalam tafsirnya yang monumental menjelaskan bahwa taqwa mencakup tiga hal pokok: melaksanakan perintah Allah, menjauhi larangan-Nya, dan konsisten dalam keduanya dalam segala kondisi dan situasi (Ibnu Katsir, 2000).")

par("Ayat utama yang menjadi landasan pembahasan ini adalah firman Allah dalam QS Al-Araf ayat 96:")

arap("\u0648\u064e\u0644\u064e\u0648\u0652 \u0623\u064e\u0646\u0651\u064e \u0623\u064e\u0647\u0652\u0644\u064e \u0627\u0644\u0652\u0642\u064f\u0631\u064e\u0649\u0670 \u0622\u0645\u064e\u0646\u064f\u0648\u0627 \u0648\u064e\u0627\u062a\u0651\u064e\u0642\u064e\u0648\u0652\u0627 \u0644\u064e\u0641\u064e\u062a\u064e\u062d\u0652\u0646\u064e\u0627 \u0639\u064e\u0644\u064e\u064a\u0652\u0647\u0650\u0645\u0652 \u0628\u064e\u0631\u064e\u0643\u064e\u0627\u062a\u064d \u0645\u0650\u0646\u064e \u0627\u0644\u0633\u0651\u064e\u0645\u064e\u0627\u0621\u0650 \u0648\u064e\u0627\u0644\u0652\u0623\u064e\u0631\u0652\u0636\u0650", '"Sekiranya penduduk negeri-negeri beriman dan bertakwa, pasti Kami akan melimpahkan kepada mereka berkah dari langit dan bumi." (QS Al-Araf: 96)')

par("Dalam tafsir Al-Mishbah, Prof. Dr. M. Quraish Shihab menjelaskan bahwa ayat ini menunjukkan hubungan kausal yang jelas antara iman dan taqwa dengan keberkahan alam. Berkah (barakah) di sini bukan sekadar bertambahnya kuantitas secara fisik, melainkan juga mencakup kualitas, manfaat, dan keberlanjutan dari sumber daya alam yang ada (Shihab, 2002). Dengan kata lain, kelimpahan pangan dan kesejahteraan suatu bangsa tidak semata-mata ditentukan oleh faktor teknis seperti irigasi, pupuk, atau teknologi pertanian, melainkan sangat dipengaruhi oleh kondisi spiritual masyarakat dan kebijakan pemimpinnya.")

par("Ibnu Katsir dalam tafsirnya menambahkan bahwa ayat ini mengandung janji dan peringatan sekaligus. Janji berupa keberkahan bagi mereka yang beriman dan bertakwa, serta ancaman berupa musibah, kekeringan, dan paceklik bagi mereka yang ingkar dan berpaling. Konteks historis ayat ini turun berkaitan dengan kondisi penduduk suatu negeri yang mendustakan para rasul utusan Allah, sehingga Allah menimpakan berbagai bencana termasuk kelaparan, kekurangan buah-buahan, dan pencabutan keberkahan bumi (Ibnu Katsir, 2000).")

heading("Ayat-Ayat Pendukung")

par("Selain QS Al-Araf:96 sebagai ayat utama, terdapat beberapa ayat lain yang relevan dengan pembahasan ketahanan pangan dan taqwa:")

arap("QS Al-Araf ayat 31: \u064a\u064e\u0627 \u0628\u064e\u0646\u0650\u064a \u0622\u062f\u064e\u0645\u064e \u062e\u064f\u0630\u064f\u0648\u0627 \u0632\u0650\u064a\u0646\u064e\u062a\u064e\u0643\u064f\u0645\u0652 \u0639\u0650\u0646\u062f\u064e \u0643\u064f\u0644\u0651\u0650 \u0645\u064e\u0633\u0652\u062c\u0650\u062f\u064d \u0648\u064e\u0643\u064f\u0644\u064f\u0648\u0627 \u0648\u064e\u0627\u0634\u0652\u0631\u064e\u0628\u064f\u0648\u0627 \u0648\u064e\u0644\u064e\u0627 \u062a\u064f\u0633\u0652\u0631\u0650\u0641\u064f\u0648\u0627 \u0625\u0650\u0646\u0651\u064e\u0647\u064f \u0644\u064e\u0627 \u064a\u064f\u062d\u0650\u0628\u0651\u064f \u0627\u0644\u0652\u0645\u064f\u0633\u0652\u0631\u0650\u0641\u0650\u064a\u0646\u064e", '"Makan dan minumlah, tetapi jangan berlebihan. Sesungguhnya Allah tidak menyukai orang yang berlebihan."')

par("Ayat ini menjadi landasan normatif larangan israf (pemborosan) dalam konsumsi pangan dan minuman. Dalam kitab Ihya Ulumuddin, Imam Al-Ghazali menjelaskan bahwa adab makan termasuk bagian dari muamalah maa Allah (hubungan hamba dengan Tuhannya). Mengontrol konsumsi bukan sekadar gaya hidup sehat, melainkan bagian integral dari ketaatan kepada Allah. Ayat ini sangat relevan dengan problem food waste Indonesia yang mencapai 20,93 juta ton per tahun.")

arap("QS Ath-Thalaq ayat 2-3: \u0648\u064e\u0645\u064e\u0646\u0652 \u064a\u064e\u062a\u0651\u064e\u0642\u0650 \u0627\u0644\u0644\u0651\u064e\u0647\u064e \u064a\u064e\u062c\u0652\u0639\u064e\u0644\u0652 \u0644\u0651\u064e\u0647\u064f \u0645\u064e\u062e\u0652\u0631\u064e\u062c\u064b\u0627 . \u0648\u064e\u064a\u064e\u0631\u0652\u0632\u064f\u0642\u0652\u0647\u064f \u0645\u0650\u0646\u0652 \u062d\u064e\u064a\u0652\u062b\u064f \u0644\u064e\u0627 \u064a\u064e\u062d\u0652\u062a\u064e\u0633\u0650\u0628\u064f", '"Barangsiapa bertakwa kepada Allah niscaya Dia akan mengadakan baginya jalan keluar dan memberinya rezeki dari arah yang tidak disangka-sangkanya."')

par("Ayat ini menegaskan hubungan langsung antara taqwa dengan jaminan rezeki dari Allah. Dalam konteks ketahanan pangan, ayat ini memberikan perspektif bahwa produktivitas pertanian dan perikanan tidak semata-mata bergantung pada faktor teknis, tetapi juga pada kualitas spiritual. Petani dan nelayan yang bertakwa akan mendapatkan jalan keluar dari kesulitan dan rezeki yang tidak terduga.")

arap("QS Al-Anam ayat 141: \u0643\u064f\u0644\u064f\u0648\u0627 \u0645\u0650\u0646\u0652 \u062b\u064e\u0645\u064e\u0631\u0650\u0647\u0650 \u0625\u0650\u0630\u064e\u0627 \u0623\u064e\u062b\u0652\u0645\u064e\u0631\u064e \u0648\u064e\u0622\u062a\u064f\u0648\u0627 \u062d\u064e\u0642\u0651\u064e\u0647\u064f \u064a\u064e\u0648\u0652\u0645\u064e \u062d\u064e\u0635\u064e\u0627\u062f\u0650\u0647\u0650", '"Makanlah dari buahnya apabila ia berbuah, dan tunaikanlah haknya di hari memetik hasilnya."')

par("Ayat ini menjadi dasar kewajiban zakat pertanian (zakat az-zari). Para ulama seperti Yusuf Al-Qardhawi dalam Fiqh al-Zakah menjelaskan bahwa nisab zakat pertanian adalah 5 wasaq setara dengan 653 kg gabah atau 520 kg beras, dengan kadar 10% untuk tanaman yang diairi dengan air alami dan 5% untuk yang menggunakan irigasi buatan (Al-Qardhawi, 2005). Zakat pertanian memiliki potensi besar sebagai instrumen redistribusi pangan.")

arap("QS An-Nahl ayat 14: \u0648\u064e\u0647\u064f\u0648\u064e \u0627\u0644\u0651\u064e\u0630\u0650\u064a \u0633\u064e\u062e\u0651\u064e\u0631\u064e \u0627\u0644\u0652\u0628\u064e\u062d\u0652\u0631\u064e \u0644\u0650\u062a\u064e\u0623\u0652\u0643\u064f\u0644\u064f\u0648\u0627 \u0645\u0650\u0646\u0652\u0647\u064f \u0644\u064e\u062d\u0652\u0645\u064b\u0627 \u0637\u064e\u0631\u0650\u064a\u0651\u064b\u0627", '"Dan Dialah yang menundukkan lautan agar kamu dapat memakan daging segar darinya."')

par("Sebagai negara maritim dengan 17.000 pulau dan luas laut mencapai 6,4 juta km persegi, potensi sumber daya perikanan Indonesia sangat luar biasa. Zakat hasil laut (zakat al-bahri) merupakan instrumen yang belum teroptimalkan secara sistematis dan dapat menjadi sumber pendanaan baru untuk program ketahanan pangan nasional.")

par("Selain ayat-ayat di atas, QS Ar-Rum:41 juga relevan: Telah tampak kerusakan di darat dan di laut disebabkan perbuatan tangan manusia. Ayat ini mengingatkan bahwa kerusakan alam termasuk krisis pangan dan degradasi lahan pertanian adalah akibat dari perilaku manusia yang menyimpang. QS Al-Hasyr:18 memerintahkan setiap jiwa untuk memperhatikan apa yang telah diperbuatnya untuk hari esok, sebuah ajakan untuk melakukan muhasabah atas pola konsumsi dan pengelolaan pangan.")

heading("Research Gap")

par("Berdasarkan penelusuran terhadap literatur akademik yang dapat diakses, ditemukan bahwa belum ada penelitian yang secara eksplisit menghubungkan konsep taqwa dalam Al-Quran dengan indikator ketahanan pangan. Model ketahanan pangan yang ada selama ini, baik dari FAO (1996) maupun Global Food Security Index (Economist Impact, 2022), hanya mengukur aspek material seperti produksi, distribusi, stabilitas harga, dan konsumsi. Tidak ada satu pun indikator yang mengukur dimensi spiritual atau keberkahan.")

par("Demikian pula, literatur tentang zakat masih banyak berfokus pada aspek fikih individual dan penghitungan nisab, belum banyak mengkaji potensi zakat pertanian dan hasil laut secara integratif dalam kerangka ketahanan pangan nasional. Sementara itu, kajian food waste di Indonesia lebih banyak didominasi perspektif lingkungan dan ekonomi (Bappenas, 2021; UNEP, 2024), dan belum ada yang membahasnya sebagai pelanggaran terhadap larangan israf dalam Al-Quran. Tulisan ini hadir untuk mengisi research gap tersebut dengan menawarkan pendekatan integratif yang menggabungkan ekoteologi, zakat berbasis sumber daya, dan kritik terhadap kebijakan publik.")

# ===================== TAWARAN GAGASAN =====================
heading("Tawaran Gagasan: Taqfis (Taqwa-Based Food Integrity System)")

par("Taqfis adalah akronim dari Taqwa-Based Food Integrity System, sebuah konsep integratif yang menempatkan taqwa sebagai variabel utama dalam sistem ketahanan pangan nasional. Berbeda dengan pendekatan konvensional yang hanya mengukur aspek material, Taqfis mengintegrasikan dimensi spiritual ke dalam setiap tahapan rantai pangan mulai dari produksi, distribusi, konsumsi, hingga pengawasan kebijakan. Konsep ini terdiri dari empat pilar yang saling terkait dan memperkuat satu sama lain.")

heading("Pilar 1: Taqwa Individu - Gerakan No Israf, Save Food")

par("Pilar pertama berangkat dari kesadaran fundamental bahwa perubahan besar harus dimulai dari diri sendiri. QS Al-Araf:31 secara eksplisit melarang israf (pemborosan) dalam konsumsi. Dalam konteks Indonesia yang menghasilkan 20,93 juta ton food waste per tahun, larangan ini menjadi sangat relevan dan mendesak. Gerakan No Israf dapat dimulai dari langkah-langkah sederhana namun berdampak besar: membuat daftar belanja sebelum berbelanja agar tidak membeli berlebihan, mengolah kembali makanan sisa menjadi hidangan baru, dan membiasakan pola konsumsi ambil secukupnya dan habiskan apa yang diambil.")

par("Konsep hisab (perhitungan amal) dalam QS Al-Hasyr:18 - Hendaklah setiap jiwa memperhatikan apa yang telah diperbuatnya untuk hari esok - dapat menjadi motivasi spiritual yang kuat untuk mengendalikan konsumsi. Jika setiap individu Muslim Indonesia mengurangi food waste sebanyak 100 gram per hari, maka secara nasional akan terselamatkan sekitar 10.000 ton pangan per hari. Dalam setahun, angka ini mencapai 3,65 juta ton pangan yang dapat dialokasikan kepada masyarakat yang membutuhkan. Lebih penting dari angka-angka tersebut, gerakan ini mengubah paradigma dari membuang makanan adalah soal pribadi menjadi membuang makanan adalah pelanggaran terhadap perintah Allah yang harus dipertanggungjawabkan.")

heading("Pilar 2: Taqwa Farming - Pesantren sebagai Living Lab Kemandirian Pangan")

par("Pilar kedua memanfaatkan potensi besar pesantren di Indonesia yang berjumlah sekitar 39.000 unit tersebar dari Aceh hingga Papua (Kemenag RI, 2024). Banyak pesantren telah mempraktikkan kemandirian pangan secara turun-temurun. Pondok Pesantren Al-Ittifaq di Bandung, misalnya, sukses mengembangkan agribisnis sayuran organik dan menjadi pemasok utama ke berbagai pasar modern. Program Kementerian Agama tentang Kemandirian Pangan Pesantren yang diluncurkan pada tahun 2022 menjadi landasan kebijakan yang mendukung pengembangan pilar ini.")

par("Model Taqwa Farming mengintegrasikan prinsip ihsan (QS Al-Qashash:77 - berbuat baik sebagaimana Allah berbuat baik kepadamu) ke dalam praktik pertanian. Prinsip ini mencakup: (a) pertanian organik yang ramah lingkungan sebagai bentuk menjaga bumi dan tidak membuat kerusakan (QS Al-Araf:56), (b) penerapan fiqih pertanian dalam pengelolaan lahan, pembagian air, dan penanganan hasil panen, serta (c) distribusi kelebihan panen melalui mekanisme zakat pertanian dan sedekah kepada masyarakat sekitar pesantren. Dengan demikian, pesantren tidak hanya menjadi pusat pendidikan agama, tetapi juga menjelma menjadi lumbung pangan masyarakat dan model ekonomi kerakyatan berbasis taqwa.")

heading("Pilar 3: Optimalisasi Zakat Az-Zari (Pertanian) dan Zakat Al-Bahri (Hasil Laut)")

par("Pilar ketiga berfokus pada optimalisasi instrumen zakat yang secara spesifik terkait dengan sumber daya pangan. Zakat pertanian (zakat az-zari) memiliki landasan kuat dalam QS Al-Anam:141 dan telah dipraktikkan sejak masa Rasulullah Saw. Potensi zakat nasional Indonesia secara keseluruhan mencapai angka fantastis Rp 327 triliun per tahun, namun realisasi penghimpunan baru sekitar Rp 33 triliun atau kurang dari 10% dari potensi (BAZNAS Outlook, 2023). Potensi zakat pertanian dan hasil laut sendiri belum terpetakan secara sistematis dan merupakan ceruk yang sangat potensial.")

par("Model yang diusulkan adalah Lumbung Pangan Zakat (Zakat Food Bank), yaitu: (a) petani dan nelayan membayar zakat dalam bentuk hasil bumi atau tangkapan langsung, bukan dalam bentuk uang tunai, sehingga pangan tetap dalam bentuk fisik yang bisa langsung didistribusikan, (b) BAZNAS dan LAZ mendistribusikan zakat pangan ini secara langsung kepada mustahik yang mengalami kerawanan pangan di daerah masing-masing, dan (c) kelebihan distribusi dapat dijual melalui mekanisme pasar dan hasilnya digunakan untuk program pemberdayaan petani dan nelayan kecil berupa bantuan bibit, alat tangkap, atau modal kerja. Pendekatan ini mengembalikan zakat pada fungsi aslinya sebagai instrumen distribusi kekayaan dan jaring pengaman sosial.")

heading("Pilar 4: Barakah Metrics - Indeks Keberkahan Pangan Nasional")

par("Pilar keempat merupakan gagasan paling inovatif dalam konsep Taqfis: menambahkan Indeks Keberkahan sebagai pilar kelima dalam kerangka ketahanan pangan, melengkapi empat pilar konvensional dari FAO (availability, access, utilization, dan stability). Indeks ini dirancang sebagai instrumen terukur yang mencakup: (1) tingkat food loss and waste nasional sebagai indikator ketaatan masyarakat terhadap larangan israf, (2) tingkat optimalisasi zakat pertanian dan hasil laut, (3) jumlah komunitas religius yang mandiri pangan seperti pesantren dan majelis taklim, serta (4) indeks kepuasan dan kesejahteraan masyarakat terhadap kebijakan pangan pemerintah.")

par("Pilar ini didasarkan pada argumen teologis bahwa ketahanan pangan tidak boleh diukur semata-mata dari ketersediaan beras di gudang Bulog atau stabilitas harga di pasar. Ukuran yang lebih fundamental adalah apakah suatu negeri benar-benar diberkahi pangannya - dalam arti cukup secara kuantitas, halal secara proses, thayyib secara kualitas, dan didistribusikan secara adil. QS Al-Araf:96 menjadi dasar teologis bahwa keberkahan adalah variabel riil yang memengaruhi ketahanan pangan, bukan sekadar slogan religius tanpa makna operasional.")

heading("Seruan kepada Pemimpin: Berantas Kemaksiatan Struktural")

par("Bagian ini merupakan inti dari relevansi sosial dan kenegaraan dari tulisan ini. Berdasarkan data yang telah dipaparkan di bagian pendahuluan, terlihat bahwa negara dalam beberapa hal justru memfasilitasi atau membiarkan kemaksiatan secara struktural. Impor minuman beralkohol dari AS atas nama pariwisata (Februari 2026), maraknya penjualan miras di minimarket dan supermarket (452 supermarket di Bali), serta konten hiburan yang mengarah pada kemusyrikan adalah fakta yang tidak bisa diabaikan dalam membahas krisis ketahanan pangan.")

par("Dalam kerangka QS Al-Araf:96, pembiaran kemaksiatan secara struktural ini memiliki konsekuensi teologis yang serius: hilangnya keberkahan bumi. Ketika pemimpin membiarkan maksiat berlangsung tanpa pengawasan, maka rakyat yang tidak bersalah pun ikut merasakan dampaknya. Rasulullah Saw. bersabda dalam hadits riwayat Abu Daud dan Ibnu Majah: Tidaklah suatu kaum membiarkan kemaksiatan di tengah-tengah mereka, lalu mereka mampu mengubahnya, melainkan Allah akan meratakan azab kepada mereka semua. (HR. Abu Daud, dishahihkan Al-Albani).")

par("Oleh karena itu, seruan kepada para pemimpin - mulai dari presiden, menteri, gubernur, bupati, wali kota, hingga pimpinan daerah dan lembaga - adalah sebagai berikut. Pertama, hentikan segala kebijakan yang memfasilitasi atau melegitimasi kemaksiatan, seperti impor minuman beralkohol dan pembiaran peredaran barang haram di ruang publik. Kedua, perkuat pengawasan terhadap konten hiburan dan peredaran barang haram yang dapat merusak moral masyarakat. Ketiga, jadikan nilai-nilai Al-Quran sebagai pedoman dan filter dalam setiap kebijakan pembangunan ketahanan pangan, bukan sekadar pendekatan teknis-ekonomis yang sekuler. Keempat, integrasikan program pemberantasan kemaksiatan ke dalam kebijakan ketahanan pangan nasional sebagai bagian dari upaya mengembalikan keberkahan bumi.")

par("Perlu ditegaskan bahwa pendekatan ini bukan berarti mengabaikan aspek teknis ketahanan pangan. Irigasi, pupuk, teknologi pertanian, distribusi logistik, stabilitas harga, dan infrastruktur pasar tetaplah penting dan harus terus ditingkatkan. Namun, seluruh aspek teknis tersebut tanpa dibarengi dengan keberkahan akan menghasilkan hasil yang suboptimal. Dengan kata lain, ketahanan pangan bukan hanya soal mencukupi perut, melainkan juga soal menjaga hubungan vertikal dengan Allah dan membersihkan masyarakat dari kemaksiatan.")

# ===================== PENUTUP =====================
heading("Penutup")
heading("Kesimpulan")

par("Krisis ketahanan pangan yang dialami Indonesia tidak dapat dipahami semata-mata sebagai persoalan teknis-pertanian. Melalui perspektif QS Al-Araf:96, krisis pangan adalah cerminan dari hilangnya keberkahan yang disebabkan oleh lemahnya iman dan taqwa - baik pada level individu maupun struktural. Pembiaran kemaksiatan oleh pemimpin, seperti impor minuman beralkohol dan maraknya peredaran barang haram, menjadi indikator bahwa nilai-nilai ketakwaan belum menjadi landasan dalam kebijakan publik negara.")

par("Konsep Taqfis (Taqwa-Based Food Integrity System) yang ditawarkan dalam tulisan ini memberikan solusi integratif yang mencakup empat pilar: gerakan No Israf sebagai manifestasi taqwa individu dalam konsumsi pangan, pengembangan pesantren sebagai living lab kemandirian pangan dan model Taqwa Farming, optimalisasi zakat pertanian dan hasil laut sebagai instrumen distribusi pangan yang berkeadilan, serta indeks keberkahan pangan sebagai indikator baru yang melengkapi empat pilar ketahanan pangan konvensional.")

heading("Rekomendasi")

par("Berdasarkan pembahasan di atas, penulis merekomendasikan beberapa hal sebagai berikut. (1) Pemerintah pusat dan daerah agar segera menghentikan kebijakan yang memfasilitasi atau melegitimasi kemaksiatan, khususnya impor dan peredaran minuman beralkohol, serta memperkuat regulasi dan pengawasan terhadap konten hiburan dan pergaulan bebas. (2) Kementerian Agama bersama BAZNAS agar mengoptimalkan Zakat Az-Zari (Pertanian) dan Zakat Al-Bahri (Hasil Laut) sebagai instrumen strategis ketahanan pangan nasional melalui program Lumbung Pangan Zakat. (3) Pesantren di seluruh Indonesia agar didorong dan difasilitasi untuk dikembangkan sebagai pusat kemandirian pangan yang mengintegrasikan nilai-nilai Al-Quran dengan praktik pertanian modern. (4) Masyarakat Muslim Indonesia agar memulai perubahan dari diri sendiri dengan mengendalikan konsumsi harian dan mengurangi food waste sebagai bagian dari implementasi taqwa dalam kehidupan sehari-hari. Wallahu alam bishawab.")

# ===================== DAFTAR PUSTAKA =====================
heading("Daftar Pustaka")

refs = [
    "Al-Qardhawi, Y. (2005). Fiqh al-Zakah. Beirut: Muassasah al-Risalah.",
    "Bappenas. (2021). Laporan Kajian Food Loss and Waste di Indonesia. Jakarta: Kementerian PPN/Bappenas.",
    "BAZNAS. (2023). Outlook Zakat Nasional 2023. Jakarta: Pusat Kajian Strategis BAZNAS.",
    "Economist Impact. (2022). Global Food Security Index 2022.",
    "FAO. (1996). Rome Declaration on World Food Security. Rome: FAO.",
    "FAO. (2023). The State of Food Security and Nutrition in the World 2023. Rome: FAO.",
    "Ibnu Katsir, I. (2000). Tafsir Al-Quran Al-Azhim. Riyadh: Dar Thayyibah.",
    "Shihab, M. Q. (2002). Tafsir Al-Mishbah: Pesan, Kesan, dan Keserasian Al-Quran. Jakarta: Lentera Hati.",
    "UNEP. (2024). Food Waste Index Report 2024. Nairobi: United Nations Environment Programme.",
]
blank()
ref_line("Sumber Berita:")
ref_line("ANTARA News Bali. (2025). Disperindag Temukan 452 Supermarket Jual Minuman Beralkohol.")
ref_line("BBC Indonesia. (2025). Dedi Mulyadi Kirim Pelajar Bandel ke Barak Militer.")
ref_line("Kompas.com. (22 Februari 2026). Pemerintah Sebut Impor Minuman Alkohol dari AS.")
ref_line("Kompas.com. (4 Maret 2026). Minimarket di Jakbar Disegel karena Jual Miras.")
ref_line("Maklumat.id. (2026). Impor Miras AS Demi Pariwisata, MUI Tegur Pemerintah.")
ref_line("Tempo.co. (8 April 2026). Penjualan Minuman Keras Dilarang, Peretail Dipanggil.")
blank()
for ref in refs:
    ref_line(ref)

output_path = "/opt/data/kti/KTI_Taqfis_Ketahanan_Pangan.docx"
save(output_path)
print(f"SUKSES! Dokumen tersimpan di: {output_path}")
import os
print(f"Ukuran: {os.path.getsize(output_path)} bytes")
