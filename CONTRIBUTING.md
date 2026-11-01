# Katkı ve Dokümantasyon Politikası (CONTRIBUTING)

`turkish-prepper` projesine katkıda bulunmak isteyen tüm araştırmacı ve gönüllülerin uyması gereken kesin ilkeler aşağıda belirtilmiştir.

---

## ⚠️ Zorunlu İçerik ve Doğrulama Kuralları

1. **Sıfırdan / Kaynaksız Doküman Eklemek Kesinlikle Yasaktır:**
   * Yapay zeka modelleri tarafından serbest üretilmiş (hallucination riski taşıyan), kişisel bloglara, kulaktan dolma bilgilere veya doğrulanmamış internet forumlarına dayanan hiçbir metin kabul edilmez.
2. **Resmî Kurum ve Literatür Şartı:**
   * Eklenen veya güncellenen her rehber; **T.C. Sağlık Bakanlığı, AFAD, Türk Kızılayı, BTK, Dünya Sağlık Örgütü (WHO), Avrupa Resüsitasyon Konseyi (ERC), Türk Nefroloji Derneği (TND)** veya benzeri akredite resmî/bilimsel kurumların yürürlükteki mevzuat, yönerge ve rehberlerine dayandırılmalıdır.
3. **Zorunlu Başlık Bloğu:**
   * Her `.md` dokümanının en üstünde referans alınan resmî yayın, yönerge adı ve kurum listelenmek zorundadır:

```markdown
# Doküman Başlığı

> **Resmî Kaynakça ve Referanslar:**  
> 1. [Kurum Adı]: *Yayın / Kılavuz Adı* (Tarih / Sürüm)  
> 2. ...
```

---

## 🛠️ Katkı Adımları (Pull Request Süreci)

1. Depoyu forklayın (`Fork`).
2. İlgili `docs/` alt dizininde veya `glossary/` dosyasında resmi kaynağa dayalı değişikliklerinizi yapın.
3. Yerel ortamda `python tools/build_site.py` çalıştırarak HTML çıktısında kırık bağlantı veya format hatası olmadığını doğrulayın.
4. Kaynak bağlantılarını ve gerekçenizi belirten bir Pull Request açın.
