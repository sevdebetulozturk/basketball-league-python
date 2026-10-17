# Basketball League Simulation (Python)

Python ile nesne yönelimli programlama (OOP) kullanılarak yazılmış basketbol ligi simülasyonu.
4 takım birbirleriyle iç saha ve deplasman olarak oynar, sezon sonunda şampiyon,
en çok sayı atan takım, en iyi oyuncu ve en etkili menajer belirlenir.

## Özellikler

- 4 takım, her takımda 1 menajer ve 5 oyuncu
- Her takımın diğerleriyle iç saha / deplasman maçı (toplam 12 maç)
- Maç motoru: 4 periyot, beraberlikte uzatma
- Oyuncuların rastgele atanan atış gücüne göre sayı üretmesi
- Menajerlerin maça rastgele etkisi ("influence" puanı)
- Lig puanı (galibiyet = 2 puan), atılan ve yenilen sayı takibi
- Her hafta sonunda takım, oyuncu ve menajer sıralamalarının güncellenmesi
- Sezon sonu istatistikleri

## Sınıf Yapısı

| Sınıf     | Görevi |
|-----------|--------|
| `Person`  | İsim ve soyisim, soyadına göre sıralama |
| `Player`  | `Person`'dan türer; atış gücü, sayı geçmişi, takım |
| `Manager` | `Person`'dan türer; etki puanı, takım |
| `Team`    | Takım adı, menajer, oyuncular, galibiyet ve sayı istatistikleri |
| `Match`   | İki takım arasındaki bir maçın simülasyonu |
| `Season`  | Fikstür oluşturma, haftaları oynatma, sezon istatistikleri |

## Nasıl Çalıştırılır?

Python 3.8 veya üzeri gerekir. Harici kütüphane kullanılmaz.

```bash
git clone https://github.com/KULLANICI_ADINIZ/basketball-league-python.git
cd basketball-league-python
python basketball_league.py
```

Sonuçlar rastgele üretildiği için her çalıştırmada farklıdır.

## Örnek Çıktı

```
(kendi terminalinizdeki çıktıyı buraya yapıştırın)
```

## Kullanılan Kavramlar

- Sınıflar ve kalıtım (`super()`)
- Sınıf değişkenleri (otomatik ID sayaçları)
- Operatör aşırı yükleme (`__lt__`, `__str__`)
- Kompozisyon (takım ↔ oyuncu ↔ menajer ilişkisi)
- `random` modülü ile simülasyon
- Sözlük, liste ve `sort` / `max` ile `lambda` anahtarları

## Bilinen Eksikler

- Maç sonucu tamamen rastgele; taktik veya oyuncu yorgunluğu gibi bir mantık yok.
- Periyot ve uzatma için sayı üretme kodu tekrar ediyor (ortak bir fonksiyona alınabilir).
- Takım ve oyuncu isimleri kodun içine sabit yazılmış.
- En iyi oyuncu ve menajer yazdırılırken sadece isim görünüyor, sayı/puan görünmüyor.
- Fikstürde ev sahibi / deplasman hafta numaraları sade bir sırayla verilmiş; gerçek bir lig takvimi gibi dengeli dağıtılmıyor.

## Geliştirme Fikirleri

- [ ] Takım ve oyuncuları dosyadan (CSV/JSON) okumak
- [ ] Oyuncu istatistik tablosu
- [ ] Rastgelelik için sabit `seed` seçeneği (tekrarlanabilir sonuçlar)
- [ ] Play-off sistemi

## Hakkında

Bu proje [Ders Adı] dersi kapsamında geliştirilmiştir.
