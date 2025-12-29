user_data = {
    "username": "bartu_sec",
    "email": "bartu@example.com",
    "password": "cok_gizli_sifre_123",
    "last_login": "2023-10-27"

}

print(f"1. HAM VERİ:\n{user_data}\n")

kullanici_rolu = user_data.get("role", "Guest")
print(f"-> Kullanıcı Rolü: {kullanici_rolu}")

yeni_ayarlar = {"2fa_enabled": True, "status": "Active"}
user_data.update(yeni_ayarlar)
print(f"\n2. GÜNCELLENMİŞ VERİ (update sonrası):\n{user_data}")

silinen_sifre = user_data.pop("password")
print(f"\n-> SİLİNEN HASSAS VERİ: {silinen_sifre}")
print(f"3. TEMİZ VERİ (Password yok artık):\n{user_data}")

print("\n4. SON KONTROL RAPORU:")
for anahtar, deger in user_data.items():
    print(f" - {anahtar.upper()}: {deger}")