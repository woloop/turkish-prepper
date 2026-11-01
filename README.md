# Turkish Prepper: Çevrimdışı Afet ve Acil Durum Bilgi Arşivi

[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](LICENSE)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content%20License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Kiwix](https://img.shields.io/badge/Format-Kiwix%20ZIM-blue.svg)](https://kiwix.org/)
[![Docker HAS Prepper Disk](https://img.shields.io/badge/Compatible-Docker%20HAS%20Prepper-green.svg)](https://github.com/woloop/Docker-HAS_Prepper_Disk)

Bu proje; doğal afetler, teknolojik kazalar veya altyapı kesintileri sırasında internet ve hücresel veri ağlarına erişimin tamamen kesildiği durumlar için hazırlanmış, doğrulanmış resmî kaynaklara dayalı çevrimdışı bir Türkçe bilgi havuzudur.

Hazırlanan tüm içerikler açık kaynaklı Kiwix (.zim) ekosistemiyle uyumlu olarak derlenmekte; Raspberry Pi, Docker tabanlı yerel sunucular, masaüstü bilgisayarlar ve mobil cihazlar üzerinden tamamen internetsiz olarak taranabilmektedir.

---

## 1. Projenin Amacı ve Kapsamı

Büyük ölçekli afetlerin (özellikle depremler ve seller) ilk saatlerinde ve takip eden günlerinde baz istasyonlarının hasar görmesi, enerji kesintileri ve aşırı yüklenme nedeniyle dijital iletişim altyapısı işlevsiz hale gelmektedir. Böyle anlarda ilk yardım, arama-kurtarma, su dezenfeksiyonu ve salgın hastalıkların önlenmesine yönelik bilgilere erişim hayati önem taşır.

* **Kiwix Ekosistemiyle Tamamlayıcılık:** Türkçe Vikipedi ve Vikikitap zaten Kiwix kataloğunda devasa bağımsız ZIM paketleri olarak yer almaktadır. `turkish-prepper`, bu genel ansiklopedik bilginin ötesine geçerek; panik anında kolayca taranabilecek **saha kontrol listeleri**, **özet müdahale algoritmaları** ve **uluslararası arama-kurtarma ekipleriyle iletişim kalıpları** sunmaya odaklanır.
* **Kiwix / ZIM Standardında Dağıtım:** Tüm rehberler tek bir `.zim` veri tabanına dönüştürülerek yerel ağda (Wi-Fi hotspot) veya doğrudan cihaz belleğinde sıfır internet bağımlılığıyla çalışır.

---

## 2. Doğrulama, Telif ve Tıbbi İnceleme Politikası

Hatalı bir ilk yardım veya müdahale bilgisi sahada telafisi mümkün olmayan sonuçlara yol açabilir. Bu nedenle projede kesin bir içerik politikası uygulanmaktadır:

* **Telif ve Yasal İlke (Fikir/Prosedür İstisnası):** FSEK hükümleri gereğince repoda üçüncü taraflara ait telifli PDF dosyaları barındırılmaz. Bilimsel ve tıbbi yöntemler referans alınarak, içerikler **özgün Türkçe anlatımla ve kontrol listeleriyle** kaleme alınır. Resmî belgelerin bağlantıları ve sürümleri [`kaynaklar.md`](kaynaklar.md) dosyasında tutulur.
* **Tıbbi İnceleme & Hakemlik (Peer Review):** İlk yardım ve medikal müdahale içeren her sayfa, en az bir sağlık profesyoneli (doktor, paramedik veya sertifikalı ilk yardım eğitmeni) tarafından incelenir. Belge başlığında inceleyen uzmanın adı, unvanı, inceleme tarihi ve ERC (Avrupa Resüsitasyon Konseyi) periyotlarına uygun gözden geçirme tarihi belirtilir.
* **Hayati Yasal Uyarı:** Rehberlerde yer alan bilgiler acil durum saha desteğidir; profesyonel ilk yardım eğitiminin ve 112 Acil Sağlık Hizmetleri'nin yerine geçmez.

---

## 3. Bilgi Havuzu Dizin Yapısı

```text
turkish-prepper/
├── docs/
│   ├── vikipedi-afet-fihristi.md   # Kiwix Vikipedi & Vikikitap için arama ve konu fihristi
│   ├── ilk-yardim/                 # T.C. Sağlık Bakanlığı ve ERC uyumlu özgün müdahale yönergeleri
│   ├── afet-ve-enkaz-yonetimi/     # AFAD ve INSARAG arama-kurtarma saha protokolleri
│   ├── hijyen-ve-halk-sagligi/     # Su sanitasyonu, atık yönetimi ve salgın önleme rehberleri
│   └── lojistik-ve-barinma/        # Çadır alanları, ısınma, acil tahliye ve stok yönetimi
├── glossary/                       # Uluslararası arama-kurtarma ekipleriyle iletişim ve terminoloji
├── kaynaklar.md                    # Referans alınan resmî kamu dokümanları ve link dökümü
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

# 3. ZIM paketine dönüştürün (Docker ile)
docker run --rm -v $(pwd):/data ghcr.io/openzim/zim-tools zimwriterfs \
  --welcome=index.html --illustration=icon.png --name=turkish-prepper \
  --language=tur --title="turkish-prepper" \
  --description="Cevrimdisi Turkce Afet Bilgi Arsivi" \
  /data/site /data/dist/turkish_prepper.zim
```

---

## 6. Lisans (İkili Lisans Modeli)

* **Yazılım ve Otomasyon Araçları (`tools/`, `.github/`):** [MIT Lisansı](LICENSE) altındadır.
* **Dokümantasyon ve İçerikler (`docs/`, `glossary/`, `README.md`):** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) lisansı altındadır.
