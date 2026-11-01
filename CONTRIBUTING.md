# Katkı ve Dokümantasyon Politikası (CONTRIBUTING)

`turkish-prepper` projesine katkıda bulunmak isteyen tüm araştırmacı ve gönüllülerin uyması gereken temel ilkeler aşağıda belirtilmiştir.

---

## 1. Telif ve Lisans Standartları (İkili Lisans)

* **Kodlar ve Araçlar (`tools/`):** MIT Lisansı altındadır.
* **İçerik ve Dokümanlar (`docs/`, `glossary/`):** Creative Commons Attribution-ShareAlike 4.0 International (**CC BY-SA 4.0**) lisansı altındadır. Vikipedi veya Vikikitap'tan alınan içerikler bu lisans ile tam uyumludur; kaynak ve yazar atfı mutlaka eklenmelidir.
* ⚠️ **Ham PDF Yüklemek Yasaktır:** Depoya kamu kurumlarına veya üçüncü şahıslara ait telifli PDF/belge yüklenemez. Referans verilen resmî belgelerin bağlantıları, sürümleri ve tarihleri [`kaynaklar.md`](kaynaklar.md) dosyasına işlenmelidir.

---

## 2. Tıbbi İnceleme ve Akreditasyon İlkeleri (Peer Review)

İlk yardım ve acil tıp konularındaki özgün metinlerin güvenilirliği hayati önem taşır:

1. **Yetkili Sağlık İncelemesi Şartı:**
   * Hazırlanan veya güncellenen her ilk yardım rehberi, bir sağlık profesyoneli (hekim, paramedik, acil tıp teknisyeni veya sertifikalı ilk yardım eğitmeni) tarafından bilimsel doğruluk açısından incelenmelidir.
2. **Zorunlu Başlık Bloğu ve Revizyon Tarihi:**
   * ERC (Avrupa Resüsitasyon Konseyi) kılavuzları 5 yılda bir güncellendiği için rehberlerin başında onaylayan uzman ve gözden geçirme tarihi bulunmalıdır:

```markdown
# Doküman Başlığı

> **⚠️ Hayati Uyarı:** Bu dokümanda yer alan bilgiler acil durum saha rehberidir; yetkili kurumlardan alınacak uygulamalı ilk yardım eğitiminin ve 112 Acil Sağlık Hizmetleri'nin yerine geçmez.  
> **Resmî Referans:** [Kurum / Yönerge Adı]  
> **Tıbbi İnceleme & Onay:** [Uzman Adı, Unvanı / Branşı]  
> **Son Gözden Geçirme Tarihi:** [GG.AA.YYYY] (Bir Sonraki Revizyon: [GG.AA.YYYY])
```

---

## 3. Katkı Süreci (Pull Request)

1. Depoyu forklayın (`Fork`).
2. İlgili `docs/` veya `glossary/` dizininde çalışmanızı yapın.
3. Yerel ortamda `python tools/build_site.py` çalıştırarak HTML çıktısında ve menü yapısında hata olmadığını test edin.
4. Kaynaklarınızı belirten açıklayıcı bir PR açın.
