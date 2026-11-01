# Turkish Prepper: Çevrimdışı Afet ve Acil Durum Bilgi Arşivi

Bu proje; doğal afetler, teknolojik kazalar veya altyapı kesintileri sırasında internet ve hücresel veri ağlarına erişimin tamamen kesildiği durumlar için hazırlanmış, doğrulanmış resmi kaynaklara dayalı çevrimdışı bir Türkçe bilgi havuzudur.

Hazırlanan tüm içerikler açık kaynaklı Kiwix (.zim) ekosistemiyle uyumlu olarak derlenmekte; Raspberry Pi, Docker tabanlı yerel sunucular, masaüstü bilgisayarlar ve mobil cihazlar üzerinden tamamen internetsiz olarak taranabilmektedir.

---

## 1. Projenin Amacı ve Kapsamı

Büyük ölçekli afetlerin (özellikle depremler ve seller) ilk saatlerinde ve takip eden günlerinde baz istasyonlarının hasar görmesi, enerji kesintileri ve aşırı yüklenme nedeniyle dijital iletişim altyapısı işlevsiz hale gelmektedir. Böyle anlarda ilk yardım, arama-kurtarma, su dezenfeksiyonu ve salgın hastalıkların önlenmesine yönelik bilgilere erişim hayati önem taşır.

Mevcut çevrimdışı bilgi kütüphaneleri (WikiMed, MDWiki vb.) küresel ölçekte zengin olmakla birlikte ağırlıklı olarak İngilizce dilindedir. `turkish-prepper`, bu açığı kapatmak amacıyla iki temel hedef doğrultusunda yapılandırılmıştır:

1. **Doğrulanmış Türkçe Kaynak Derlemesi:** T.C. Sağlık Bakanlığı, AFAD, Türk Kızılayı ve uluslararası standart belirleyicilerin (ERC, WHO, INSARAG) kamuya açık yönergelerini ve resmi protokollerini tek çatı altında toplamak.
2. **Kiwix / ZIM Standardında Dağıtım:** Tüm metin, şema ve kontrol listelerini optimize edilmiş tek bir `.zim` veri tabanına dönüştürerek yerel ağda (Wi-Fi hotspot) veya doğrudan cihaz belleğinde sıfır internet bağımlılığıyla sunmak.

---

## 2. Doğrulama ve İçerik Politikası

Hatalı bir ilk yardım veya müdahale bilgisi sahada telafisi mümkün olmayan sonuçlara yol açabilir. Bu nedenle projede kesin bir içerik politikası uygulanmaktadır:

* **Sentezlenmiş / Doğrulanmamış İçerik Yasağı:** Projeye yapay zeka tarafından serbestçe üretilen veya kaynağı belirsiz kişisel görüşler eklenemez.
* **Resmi Kaynak Şartı:** Eklenen her doküman, T.C. kamu kurumlarının (Sağlık Bakanlığı, AFAD, Kızılay vb.) veya uluslararası tıp/afet konseylerinin yürürlükteki yönerge, tebliğ ve bilimsel yayınlarına dayandırılmak zorundadır.
* **Kaynak ve Sürüm Belirtme:** Her belgenin başında referans alınan resmî kurum, doküman adı ve varsa revizyon tarihi açıkça belirtilmelidir.

---

## 3. Bilgi Havuzu Dizin Yapısı

Arşiv, afet anında ihtiyaç duyulan öncelik sırasına göre kategorize edilmiştir:

```text
turkish-prepper/
├── docs/
│   ├── ilk-yardim/                 # T.C. Sağlık Bakanlığı ve ERC uyumlu müdahale yönergeleri
│   ├── afet-ve-enkaz-yonetimi/     # AFAD ve INSARAG arama-kurtarma saha protokolleri
│   ├── hijyen-ve-halk-sagligi/     # Su sanitasyonu, atık yönetimi ve salgın önleme rehberleri
│   ├── lojistik-ve-barinma/        # Çadır alanları, ısınma, acil tahliye ve stok yönetimi
│   └── acil-durum-haberlesmesi/    # Telsiz frekansları, röle protokolleri ve çağrı standartları
├── resmi-belgeler-pdf/             # Kurumların sunucularından doğrudan indirilmiş orijinal PDF'ler
├── glossary/                       # Uluslararası ekiplerle ortak terminoloji eşleştirmesi
├── tools/                          # Dokümanları HTML ve ZIM formatına çeviren derleme araçları
└── .github/workflows/              # Otomatik ZIM üretim ve yayın (CI/CD) hattı
```

---

## 4. Kullanım ve Dağıtım

### A. Kiwix Uygulamaları ile Doğrudan Kullanım
Hazırlanan `.zim` dosyaları [Releases](../../releases) bölümünden temin edilebilir:
* **Mobil:** Android ve iOS için Kiwix uygulaması ile dosya cihaza aktarılarak doğrudan açılabilir.
* **Masaüstü:** Windows, macOS ve Linux sistemlerinde Kiwix Reader aracılığıyla görüntülenebilir.

### B. Sunucu ve Hotspot Entegrasyonu
Afet bölgelerinde kurulan yerel ağ sunucularında (Raspberry Pi veya Docker kurulu mini PC'ler) `kiwix-serve` ile tüm yerel ağa (Wi-Fi) kablosuz olarak dağıtılabilir:

```bash
kiwix-serve --port=8080 turkish_prepper.zim
```

Docker tabanlı kapsamlı bir afet sunucusu için [Docker-HAS_Prepper_Disk](https://github.com/woloop/Docker-HAS_Prepper_Disk) projesi kullanılabilir.

---

## 5. Yerel Derleme Talimatları

Kaynak Markdown belgelerinden statik web sitesi ve `.zim` paketi oluşturmak için:

```bash
# 1. Projeyi klonlayın
git clone https://github.com/woloop/turkish-prepper.git
cd turkish-prepper

# 2. Statik web yapısını üretin
python tools/build_site.py

# 3. ZIM paketine dönüştürün (zimwriterfs gerektirir)
zimwriterfs --welcome=index.html --language=tur --title="turkish-prepper" --description="Cevrimdisi Turkce Afet Bilgi Arsivi" site/ dist/turkish_prepper.zim
```

---

## 6. Katkı ve İnceleme Süreci

İçerik ekleme ve düzeltme süreçleri hakemli ve kaynaklı inceleme esasına dayanır. Lütfen detaylar için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyiniz.
