"""
Generate KTI - REVISI MENTOR (SIMBOTAK)
"""


# Load library properly
import types
with open('/opt/data/kti/kti_lib.py') as f:
    lib_code = f.read()
exec(lib_code)

def ref_line_bold(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-1.0)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.font.bold = True

# ===== TITLE =====
heading("SIMBOTAK: SISTEM INTEGRITAS MAKANAN BERBASIS OPTIMALISASI TAKWA DAN KEBERKAHAN", 0)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(12)
p.paragraph_format.line_spacing = 1.5
r = p.add_run("Integrasi Nilai-Nilai Al-Quran, Zakat, dan Kebijakan Pimpinan dalam Mewujudkan Ketahanan Pangan Nasional")
r.font.name = 'Times New Roman'
r.font.size = Pt(12)

# ===== PENDAHULUAN =====
heading("Pendahuluan")

par("Ketahanan pangan nasional Indonesia saat ini berada dalam posisi yang paradoksal. Di satu sisi, Indonesia dikenal sebagai negara agraris-maritim dengan kekayaan sumber daya alam yang melimpah. Luas lahan pertanian mencapai jutaan hektar dan laut Indonesia seluas 6,4 juta km persegi menyimpan potensi perikanan yang sangat besar. Di sisi lain, peringkat Global Food Security Index (GFSI) 2022 menempatkan Indonesia di posisi 63 dari 113 negara (Economist Impact, 2022). Indonesia masih mengimpor beras sekitar 3,3 juta ton pada tahun 2024 (BPS, 2024), sementara food loss and waste mencapai 20,93 juta ton per tahun, dan berdasarkan UNEP Food Waste Index Report 2024, Indonesia menduduki peringkat kedua sebagai negara penghasil sampah makanan terbesar di dunia. Kerugian ekonomi akibat food loss and waste diperkirakan mencapai Rp 213 hingga Rp 551 triliun per tahun, angka yang cukup untuk memberi makan 125 juta orang setiap harinya (Bappenas, 2021).")

par("Paradoks lain yang tidak kalah penting adalah kenyataan bahwa pada saat yang sama, masih banyak dari kalangan rakyat yang justru tersangkut dalam berbagai kemaksiatan yang merusak moral dan keberkahan hidup. Berbagai kasus keterlibatan anggota masyarakat—bahkan pejabat publik—dalam judi online, pornografi, dan asusila marak terjadi. Sebagai contoh, anggota DPR RI Sahroni mengeluarkan pernyataan resmi meminta polisi mewaspadai kemunculan judi berkedok game center di berbagai daerah (Kompas.com, 15 Juni 2026). Wali Kota Bandung Farhan juga mengancam sanksi berat bagi Aparatur Sipil Negara (ASN) yang terlibat judi online, khususnya di momentum Piala Dunia 2026 (Kompas.com, 15 Juni 2026). Di sisi lain, kasus pencucian uang hasil judi online senilai Rp 297 miliar juga mencuat di Surabaya (Kompas.com, 3 Juni 2026). Belum lagi berbagai kasus pornografi yang melibatkan publik figur dan oknum pejabat yang terus bermunculan. Fakta-fakta ini menunjukkan bahwa kemaksiatan tidak hanya terjadi di ruang privat, tetapi juga telah merambah ke ruang publik dan struktural, bahkan melibatkan mereka yang seharusnya menjadi teladan.")

par("Fenomena ini menjadi penting ketika dibaca dalam perspektif Al-Quran, khususnya QS Al-Araf ayat 96 yang secara eksplisit menyatakan bahwa iman dan taqwa penduduk suatu negeri menjadi kunci terbukanya keberkahan dari langit dan bumi. Jika kemaksiatan dibiarkan dan bahkan dilakukan oleh mereka yang duduk di kursi kekuasaan, maka hilangnya keberkahan bumi—termasuk krisis pangan—adalah keniscayaan yang tidak bisa dihindari. Pembiaran kemaksiatan oleh pemimpin dan masyarakat luas dapat dipahami sebagai bentuk ketiadaan taqwa yang berakibat langsung pada ketahanan pangan nasional.")

par("Tulisan ini bertujuan untuk menawarkan sebuah gagasan integratif bernama SIMBOTAK (Sistem Integritas Makanan Berbasis Optimalisasi Takwa dan Keberkahan) yang menghubungkan tiga dimensi: (1) taqwa individu dalam konsumsi dan adab makan sebagaimana diajarkan Rasulullah Saw., (2) optimalisasi zakat sebagai instrumen distribusi keberkahan dan penguatan solidaritas sosial, dan (3) seruan kepada pemimpin untuk menjadi teladan dalam ketakwaan, termasuk mendorong shalat berjamaah di jajarannya, menunaikan zakat secara patuh, dan memberantas kemaksiatan di lingkungannya.")

# ===== LANDASAN TEORI =====
heading("Landasan Teori dan Tinjauan Pustaka")
heading("Konsep Ketahanan Pangan dan Keterbatasannya")

par("Organisasi Pangan dan Pertanian Dunia (FAO) mendefinisikan ketahanan pangan melalui empat pilar utama: ketersediaan (availability), akses (access), pemanfaatan (utilization), dan stabilitas (stability) (FAO, 1996). Keempat pilar ini bersifat material-empiris dan tidak mempertimbangkan faktor spiritual sama sekali. Data terkini dari FAO (2023) menunjukkan bahwa meskipun produksi pangan global terus meningkat, kerawanan pangan masih melanda 691 hingga 783 juta orang di seluruh dunia. Fakta ini mengindikasikan adanya variabel lain yang belum tertangkap oleh model ketahanan pangan konvensional, yaitu variabel keberkahan.")

par("Sementara itu, penelitian tentang food loss and waste di Indonesia oleh Bappenas (2021) mengungkap temuan penting: 44% dari total food loss terjadi pada tahap konsumsi rumah tangga. Artinya, hampir setengah dari pemborosan pangan nasional berasal dari perilaku individu dalam mengelola makanan sehari-hari. Problem ini jarang dibahas dari sudut pandang spiritual, padahal Al-Quran secara tegas melarang perilaku israf (berlebihan) dalam QS Al-Araf ayat 31, dan Rasulullah Saw. telah memberikan teladan adab makan yang sempurna.")

heading("Konsep Taqwa dalam Al-Quran")

par("Taqwa secara etimologis berasal dari akar kata waqa-yaqi-wiqayah yang berarti menjaga, melindungi, atau menghindarkan diri dari bahaya. Dalam terminologi Al-Quran, taqwa memiliki dimensi vertikal (hubungan dengan Allah) dan horizontal (hubungan dengan sesama manusia dan alam semesta). Ibnu Katsir dalam tafsirnya menjelaskan bahwa taqwa mencakup tiga hal pokok: melaksanakan perintah Allah, menjauhi larangan-Nya, dan konsisten dalam keduanya dalam segala kondisi (Ibnu Katsir, 2000).")

par("Ayat utama yang menjadi landasan pembahasan ini adalah firman Allah dalam QS Al-Araf ayat 96:")

arap("\u0648\u064e\u0644\u064e\u0648\u0652 \u0623\u064e\u0646\u0651\u064e \u0623\u064e\u0647\u0652\u0644\u064e \u0627\u0644\u0652\u0642\u064f\u0631\u064e\u0649\u0670 \u0622\u0645\u064e\u0646\u064f\u0648\u0627 \u0648\u064e\u0627\u062a\u0651\u064e\u0642\u064e\u0648\u0652\u0627 \u0644\u064e\u0641\u064e\u062a\u064e\u062d\u0652\u0646\u064e\u0627 \u0639\u064e\u0644\u064e\u064a\u0652\u0647\u0650\u0645\u0652 \u0628\u064e\u0631\u064e\u0643\u064e\u0627\u062a\u064d \u0645\u0650\u0646\u064e \u0627\u0644\u0633\u0651\u064e\u0645\u064e\u0627\u0621\u0650 \u0648\u064e\u0627\u0644\u0652\u0623\u064e\u0631\u0652\u0636\u0650", '"Sekiranya penduduk negeri-negeri beriman dan bertakwa, pasti Kami akan melimpahkan kepada mereka berkah dari langit dan bumi." (QS Al-Araf: 96)')

par("Dalam tafsir Al-Mishbah, Prof. Dr. M. Quraish Shihab menjelaskan bahwa ayat ini menunjukkan hubungan kausal yang jelas antara iman dan taqwa dengan keberkahan alam. Berkah (barakah) di sini bukan sekadar bertambahnya kuantitas secara fisik, melainkan juga mencakup kualitas, manfaat, dan keberlanjutan dari sumber daya alam yang ada (Shihab, 2002). Ayat ini menjadi fondasi teologis bahwa krisis pangan tidak bisa dilepaskan dari krisis moral dan spiritual suatu bangsa.")

heading("Ayat-Ayat Pendukung")

par("Selain QS Al-Araf:96 sebagai ayat utama, terdapat beberapa ayat lain yang relevan:")

arap("QS Al-Araf ayat 31:\n\u064a\u064e\u0627 \u0628\u064e\u0646\u0650\u064a \u0622\u062f\u064e\u0645\u064e \u062e\u064f\u0630\u064f\u0648\u0627 \u0632\u0650\u064a\u0646\u064e\u062a\u064e\u0643\u064f\u0645\u0652 \u0639\u0650\u0646\u062f\u064e \u0643\u064f\u0644\u0651\u0650 \u0645\u064e\u0633\u0652\u062c\u0650\u062f\u064d \u0648\u064e\u0643\u064f\u0644\u064f\u0648\u0627 \u0648\u064e\u0627\u0634\u0652\u0631\u064e\u0628\u064f\u0648\u0627 \u0648\u064e\u0644\u064e\u0627 \u062a\u064f\u0633\u0652\u0631\u0650\u0641\u064f\u0648\u0627 \u0625\u0650\u0646\u0651\u064e\u0647\u064f \u0644\u064e\u0627 \u064a\u064f\u062d\u0650\u0628\u0651\u064f \u0627\u0644\u0652\u0645\u064f\u0633\u0652\u0631\u0650\u0641\u0650\u064a\u0646\u064e", '"Makan dan minumlah, tetapi jangan berlebihan. Sesungguhnya Allah tidak menyukai orang yang berlebihan."')

par("Ayat ini menjadi landasan normatif larangan israf dalam konsumsi pangan, dan menjadi dasar gerakan pengurangan food waste sebagai bentuk implementasi taqwa dalam kehidupan sehari-hari.")

arap("QS Ath-Thalaq ayat 2-3:\n\u0648\u064e\u0645\u064e\u0646\u0652 \u064a\u064e\u062a\u0651\u064e\u0642\u0650 \u0627\u0644\u0644\u0651\u064e\u0647\u064e \u064a\u064e\u062c\u0652\u0639\u064e\u0644\u0652 \u0644\u0651\u064e\u0647\u064f \u0645\u064e\u062e\u0652\u0631\u064e\u062c\u064b\u0627 . \u0648\u064e\u064a\u064e\u0631\u0652\u0632\u064f\u0642\u0652\u0647\u064f \u0645\u0650\u0646\u0652 \u062d\u064e\u064a\u0652\u062b\u064f \u0644\u064e\u0627 \u064a\u064e\u062d\u0652\u062a\u064e\u0633\u0650\u0628\u064f", '"Barangsiapa bertakwa kepada Allah niscaya Dia akan mengadakan baginya jalan keluar dan memberinya rezeki dari arah yang tidak disangka-sangkanya."')

par("Ayat ini menegaskan bahwa taqwa adalah kunci rezeki dan jalan keluar dari kesulitan, termasuk kesulitan pangan. Petani, nelayan, dan seluruh pelaku usaha pangan yang bertakwa akan mendapatkan jaminan rezeki dari Allah Swt.")

par("Selain itu, QS Al-Anam ayat 141 tentang zakat hasil bumi dan QS At-Taubah ayat 103 tentang fungsi zakat yang membersihkan dan mensucikan.")

par("QS At-Taubah:103: Ambillah zakat dari harta mereka, guna membersihkan dan mensucikan mereka... Zakat berfungsi ganda: membersihkan harta dan jiwa, serta menumbuhkan keberkahan dalam kehidupan bermasyarakat. Zakat bukan sekadar instrumen ekonomi, melainkan pilar ketakwaan yang menghubungkan dimensi spiritual dengan kesejahteraan sosial.")

arap("QS Saba ayat 15: \u0644\u064e\u0642\u064e\u062f\u0652 \u0643\u064e\u0627\u0646\u064e \u0644\u0650\u0633\u064e\u0628\u064e\u0627\u0621\u064d \u0641\u0650\u064a \u0645\u064e\u0633\u0652\u0643\u064e\u0646\u0650\u0647\u0650\u0645\u0652 \u0622\u064a\u064e\u0629\u064c \u062c\u064e\u0646\u0651\u064e\u062a\u064e\u0627\u0646\u0650 \u0639\u064e\u0646\u0652 \u064a\u064e\u0645\u0650\u064a\u0646\u064d \u0648\u064e\u0634\u0650\u0645\u064e\u0627\u0644\u0650 \u0643\u064f\u0644\u064f\u0648\u0627 \u0645\u0650\u0646\u0652 \u0631\u0650\u0632\u0652\u0642\u0650 \u0631\u064e\u0628\u0651\u0650\u0643\u064f\u0645\u0652 \u0648\u064e\u0627\u0634\u0652\u0643\u064f\u0631\u064f\u0648\u0627 \u0644\u064e\u0647\u064f \u0628\u064e\u0644\u0652\u062f\u064e\u0629\u064c \u0637\u064e\u064a\u0651\u0650\u0628\u064e\u0629\u064c \u0648\u064e\u0631\u064e\u0628\u0651\u064c \u063a\u064e\u0641\u064f\u0648\u0631\u064c", '"Sesungguhnya bagi kaum Saba ada tanda (kekuasaan Tuhan) di tempat kediaman mereka, yaitu dua buah kebun di sebelah kanan dan kiri. Makanlah olehmu dari rezeki Tuhanmu dan bersyukurlah kepada-Nya. (Negerimu adalah) negeri yang baik dan (Tuhanmu) adalah Tuhan Yang Maha Pengampun."')

par("Kisah negeri Saba yang makmur kemudian berubah menjadi negeri yang tandus akibat kesombongan dan kekufuran mereka menjadi pelajaran berharga: keberkahan pangan bisa hilang ketika manusia meninggalkan rasa syukur dan ketakwaan.")

heading("Research Gap")

par("Berdasarkan penelusuran literatur yang dapat diverifikasi, ditemukan bahwa belum ada penelitian yang secara eksplisit menghubungkan konsep taqwa dalam Al-Quran dengan indikator ketahanan pangan. Model ketahanan pangan konvensional (FAO, 1996; Global Food Security Index, 2022) hanya mengukur aspek material. Demikian pula, kajian tentang zakat banyak berfokus pada aspek fikih individual, belum banyak mengkaji peran zakat dalam kerangka ketahanan pangan nasional dari perspektif kepemimpinan dan keteladanan. Tulisan ini mengisi research gap tersebut dengan menawarkan konsep SIMBOTAK yang mengintegrasikan ekoteologi, zakat sebagai instrumen keberkahan, dan peran pemimpin sebagai teladan ketakwaan.")

# ===== TAWARAN GAGASAN =====
heading("Tawaran Gagasan: SIMBOTAK (Sistem Integritas Makanan Berbasis Optimalisasi Takwa dan Keberkahan)")

par("SIMBOTAK adalah sebuah sistem integratif yang menempatkan takwa dan keberkahan sebagai variabel utama dalam ketahanan pangan nasional. Berbeda dengan pendekatan konvensional yang hanya mengukur aspek material, SIMBOTAK mengintegrasikan dimensi spiritual ke dalam setiap aspek rantai pangan mulai dari produksi, konsumsi, distribusi, hingga kebijakan publik. Konsep ini terdiri dari tiga pilar utama yang saling terkait.")

heading("Pilar 1: Taqwa Individu dalam Konsumsi Pangan dan Adab Makan ala Rasulullah")

par("Pilar pertama berangkat dari kesadaran fundamental bahwa perubahan besar harus dimulai dari diri sendiri. QS Al-Araf:31 secara eksplisit melarang israf dalam konsumsi, dan Rasulullah Saw. telah memberikan teladan sempurna dalam adab makan sehari-hari. Beberapa adab makan yang diajarkan Nabi Muhammad Saw. antara lain: (1) membaca basmalah sebelum makan (HR. Muslim), (2) makan dengan tangan kanan (HR. Bukhari-Muslim), (3) makan dari tepi wadah, tidak dari tengah (HR. Tirmidzi), (4) tidak mencela makanan—jika suka dimakan, jika tidak ditinggalkan (HR. Bukhari-Muslim), (5) menjilat jari dan membersihkan piring hingga tidak ada sisa makanan (HR. Muslim), (6) minum sambil duduk dan tidak bernafas dalam gelas (HR. Bukhari), (7) tidak makan dalam keadaan kenyang berlebihan (HR. Tirmidzi).")

par("Adab-adab ini bukan sekadar etika, melainkan bagian dari ibadah yang mengandung nilai-nilai mendalam untuk ketahanan pangan. Larangan menyisakan makanan, misalnya, memiliki relevansi langsung dengan problem food waste nasional yang mencapai 20,93 juta ton per tahun. Di sinilah peran pesantren dan program makan masyarakat menjadi sangat strategis: pesantren dapat menjadi pusat sosialisasi dan pembelajaran adab makan Islami kepada santri dan masyarakat sekitar. Data dari Kemenag (2024) mencatat ada sekitar 39.000 pesantren di Indonesia yang berpotensi menjadi episentrum gerakan ini. Program makan bergizi gratis di sekolah dan komunitas juga dapat diintegrasikan dengan kurikulum adab makan Islami, sehingga generasi muda tumbuh dengan kesadaran spiritual yang kuat tentang pentingnya menghargai makanan dan tidak berlebih-lebihan.")

heading("Pilar 2: Zakat sebagai Instrumen Keberkahan dan Penguatan Solidaritas Sosial")

par("Pilar kedua berfokus pada optimalisasi zakat sebagai instrumen yang membersihkan harta, menumbuhkan keberkahan, dan memperkuat solidaritas sosial dalam ketahanan pangan. Zakat dalam Al-Quran disebut sebanyak 27 kali beriringan dengan shalat, menunjukkan betapa eratnya hubungan antara ibadah vertikal dan horizontal ini. QS At-Taubah:103 menyatakan bahwa zakat berfungsi untuk membersihkan (tuthahhiruhum) dan mensucikan (tuzakkihim) harta dan jiwa.")

par("Potensi zakat nasional Indonesia mencapai angka fantastis Rp 327 triliun per tahun, namun realisasi penghimpunan baru sekitar Rp 33 triliun atau kurang dari 10% (BAZNAS Outlook, 2023). Artinya, potensi zakat yang sangat besar belum teroptimalkan. Jika zakat dikelola dengan baik dan disalurkan secara tepat, ia akan menjadi instrumen redistribusi yang luar biasa kuatnya untuk mengatasi kerawanan pangan masyarakat miskin dan mustahik.")

par("Model yang diusulkan adalah penguatan sistem zakat terintegrasi yang mencakup: (a) edukasi dan sosialisasi kepada para muzaki (pembayar zakat) tentang peran zakat menumbuhkan keberkahan harta dan masyarakat, (b) penyaluran zakat yang diarahkan pada program ketahanan pangan seperti bantuan sembako, modal usaha tani, dan program pemberdayaan petani kecil, (c) transparansi dan akuntabilitas pengelolaan zakat melalui BAZNAS dan LAZ, dan (d) peran pemimpin sebagai teladan dan pengawas kepatuhan berzakat di jajarannya.")

heading("Pilar 3: Kepemimpinan Teladan — Pemimpin yang Memimpin dengan Takwa")

par("Pilar ketiga ini merupakan inti dari relevansi sosial dan kenegaraan tulisan ini. Seorang pemimpin tidak cukup hanya membuat kebijakan, tetapi harus menjadi teladan dalam ketakwaan. Dalam konteks ketahanan pangan dan keberkahan, pemimpin yang bertakwa adalah mereka yang: (1) menjadi teladan dalam menunaikan zakat tepat waktu dan penuh kesadaran, (2) mengawasi dan mendorong kepatuhan berzakat di seluruh jajaran pemerintahannya, (3) menjauhkan diri dan institusinya dari berbagai kemaksiatan seperti judi online, pornografi, dan korupsi yang menghilangkan keberkahan, dan (4) memimpin dengan nilai-nilai Al-Quran dalam setiap kebijakan publik.")

par("Salah satu bentuk keteladanan pemimpin yang sangat relevan adalah mendorong dan mencontohkan shalat berjamaah di lingkungan kerjanya. Shalat berjamaah bukan sekadar ritual, melainkan simbol persatuan, kedisiplinan, dan ketundukan kepada Allah yang menjadi fondasi ketakwaan. Seorang pemimpin yang menyempatkan diri shalat berjamaah bersama jajarannya menunjukkan bahwa nilai-nilai spiritual bukan sekadar pajangan, melainkan dihayati dalam kehidupan organisasi. Ini adalah bentuk taqwa yang kasat mata, yang keberkahannya akan menular ke seluruh aspek kehidupan, termasuk produktivitas dan keberkahan rezeki yang pada akhirnya berdampak pada ketahanan pangan.")

par("Sebaliknya, jika di kalangan masyarakat—termasuk para pemimpin dan pejabat—masih banyak yang tersangkut kemaksiatan seperti judi online dan pornografi, maka keberkahan akan sulit turun. Dalam QS Al-Araf:96, janji keberkahan dikaitkan langsung dengan iman dan taqwa. Pembiaran kemaksiatan adalah antitesis dari ketakwaan. Karena itu, seruan kepada pemimpin adalah untuk memberantas kemaksiatan di lingkungannya, mulai dari diri sendiri, keluarga, hingga institusi yang dipimpinnya.")

par("Pendekatan ini bukan berarti mengabaikan aspek teknis ketahanan pangan. Irigasi, pupuk, teknologi pertanian, dan stabilitas harga tetaplah penting. Namun, seluruh aspek teknis tersebut tanpa dibarengi dengan keberkahan akan menghasilkan hasil yang suboptimal. Ketahanan pangan bukan hanya soal mencukupi perut, melainkan juga soal menjaga hubungan vertikal dengan Allah, membersihkan masyarakat dari kemaksiatan, dan menghidupkan nilai-nilai keteladanan dalam kepemimpinan.")

# ===== PENUTUP =====
heading("Penutup")
heading("Kesimpulan")

par("Krisis ketahanan pangan yang dialami Indonesia tidak dapat dipahami semata-mata sebagai persoalan teknis-pertanian. Melalui perspektif QS Al-Araf:96, krisis pangan adalah cerminan dari hilangnya keberkahan yang disebabkan oleh lemahnya iman dan taqwa—baik pada level individu maupun kepemimpinan. Maraknya kasus judi online, pornografi, dan kemaksiatan lainnya di kalangan rakyat dan pejabat menjadi indikator bahwa nilai-nilai ketakwaan belum menjadi landasan kehidupan bermasyarakat dan berbangsa.")

par("Konsep SIMBOTAK (Sistem Integritas Makanan Berbasis Optimalisasi Takwa dan Keberkahan) yang ditawarkan dalam tulisan ini memberikan solusi integratif yang mencakup tiga pilar: adab makan Rasulullah Saw. dan pengurangan food waste sebagai manifestasi taqwa individu, penguatan zakat sebagai instrumen keberkahan dan distribusi kesejahteraan, serta kepemimpinan teladan yang mendorong shalat berjamaah, patuh berzakat, dan memberantas kemaksiatan di lingkungannya.")

heading("Rekomendasi")

par("Berdasarkan pembahasan di atas, penulis merekomendasikan beberapa hal sebagai berikut. (1) Pemerintah agar mengambil langkah tegas memberantas kemaksiatan struktural seperti judi online, pornografi, dan peredaran barang haram yang menghilangkan keberkahan negeri, serta mengintegrasikan pemberantasan kemaksiatan ke dalam kebijakan ketahanan pangan nasional. (2) Para pemimpin di semua tingkatan agar menjadi teladan dalam ketakwaan, termasuk dalam menunaikan zakat, mendorong shalat berjamaah, serta mengawasi kepatuhan berzakat di jajarannya. (3) BAZNAS dan LAZ agar mengoptimalkan penghimpunan dan penyaluran zakat, khususnya untuk program ketahanan pangan dan pemberdayaan petani kecil. (4) Masyarakat Muslim dan pesantren agar menghidupkan kembali adab makan ala Rasulullah Saw. sebagai bagian dari pendidikan karakter dan pengurangan food waste. (5) Program makan bergizi di masyarakat agar diintegrasikan dengan pembelajaran adab makan Islami. Wallahu alam bishawab.")

# ===== DAFTAR PUSTAKA =====
heading("Daftar Pustaka")

ref_line_bold("Sumber Berita:")
ref_line("Kompas.com. (15 Juni 2026). Sahroni Minta Polisi Waspadai Kemunculan Judi Berkedok Game Center di Daerah.")
ref_line("Kompas.com. (15 Juni 2026). Farhan Ancam Sanksi Berat ASN yang Terlibat Judi Online di Momentum Piala Dunia 2026.")
ref_line("Kompas.com. (3 Juni 2026). Cuci Uang Hasil Judi Online Rp 297 Miliar, Pria di Surabaya Dituntut 11 Tahun.")
ref_line("Kompas.com. (22 Februari 2026). Pemerintah Sebut Impor Minuman Alkohol dari AS demi Genjot Pariwisata.")
blank()
ref_line_bold("Buku, Jurnal, dan Laporan:")
refs = [
    "Bappenas. (2021). Laporan Kajian Food Loss and Waste di Indonesia. Jakarta: Kementerian PPN/Bappenas.",
    "BAZNAS. (2023). Outlook Zakat Nasional 2023. Jakarta: Pusat Kajian Strategis BAZNAS.",
    "Economist Impact. (2022). Global Food Security Index 2022.",
    "FAO. (1996). Rome Declaration on World Food Security. Rome: FAO.",
    "FAO. (2023). The State of Food Security and Nutrition in the World 2023. Rome: FAO.",
    "Ibnu Katsir, I. (2000). Tafsir Al-Quran Al-Azhim. Riyadh: Dar Thayyibah.",
    "Shihab, M. Q. (2002). Tafsir Al-Mishbah: Pesan, Kesan, dan Keserasian Al-Quran. Jakarta: Lentera Hati.",
    "UNEP. (2024). Food Waste Index Report 2024. Nairobi: United Nations Environment Programme.",
]
for ref in refs:
    ref_line(ref)

blank()
ref_line_bold("Referensi Hadits:")
ref_line("HR. Bukhari, Kitab al-At'imah (Makanan), no. 5376 (adab makan).")
ref_line("HR. Muslim, Kitab al-At'imah (Makanan), no. 2019, 2020 (adab makan).")
ref_line("HR. Tirmidzi, Kitab al-At'imah, no. 1807 (makan dari tepi wadah).")

output_path = "/opt/data/kti/KTI_SIMBOTAK_Ketahanan_Pangan.docx"
save(output_path)
print(f"SUKSES! Dokumen: {output_path}")
import os
print(f"Ukuran: {os.path.getsize(output_path)} bytes")
print("SELESAI")
