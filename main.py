import random
from sorular import sorular
from muzikler import muzik_listesi

# Duygulara ait puanları tutan sözlük
puanlar = {
    "mutlu": 0,
    "üzgün": 0,
    "motivasyon": 0,
    "yorgun": 0
}

print("🎭 Mini Ruh Hali Testi Başlıyor!\n")

# Soruları sırayla kullanıcıya sor
for i, soru in enumerate(sorular, 1):
    print(f"Soru {i}: {soru['soru']}")
    for harf, (metin, _) in soru["secenekler"].items():
        print(f"  {harf}) {metin}")

    # Geçerli cevap gelene kadar döngü
    while True:
        cevap = input(">> Seçimin (a/b/c/d): ").lower()
        if cevap in soru["secenekler"]:
            duygu = soru["secenekler"][cevap][1]
            puanlar[duygu] += 1
            break
        else:
            print("Lütfen sadece a, b, c veya d seçeneklerinden birini giriniz.")
    print()

# En yüksek puanı alan ruh hali seçilir
ruh_hali = max(puanlar, key=puanlar.get)

# Sonuç gösterimi
print(f"🧠 Ruh halin: {ruh_hali.upper()}")
print("🎵 Senin için önerilen şarkılar:")

for sarki in random.sample(muzik_listesi[ruh_hali], 3):
    print(f" - {sarki}")
