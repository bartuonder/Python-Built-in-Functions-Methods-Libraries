#örnek log analizi

gelen_log = "   [WARNING] | User:Admin_Bartu | IP:192.168.1.55 | Status:Failed_Login   "

print(f"1. HAM VERİ:\n'{gelen_log}'\n")

temiz_log = gelen_log.strip()
print(f"2. STRIP (Temizlendi):\n'{temiz_log}'")

kucuk_log = temiz_log.lower()
print(f"3. LOWER (Küçültüldü):\n'{kucuk_log}'")

if kucuk_log.startswith("[warning]"):
    print("\n-> ALARM: Bu bir uyarı logu!")

if kucuk_log.find("failed") != -1:
    print("-> ALARM: Başarısız giriş denemesi tespit edildi!")

basitlesmis_log = kucuk_log.replace("[", "").replace("]", "")

parcalar = basitlesmis_log.split("|")

print(f"\n4. SPLIT (Parçalandı): {parcalar}")

temiz_parcalar = [parca.strip() for parca in parcalar]

son_rapor = " -- ".join(temiz_parcalar)

print(f"\n5. JOIN (Raporlandı):\n{son_rapor}")