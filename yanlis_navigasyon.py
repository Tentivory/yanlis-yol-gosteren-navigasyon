#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yanlış Yol Gösteren Navigasyon v1.0
Kayyum Grok tarafından yazıldı. Ciddiye alınacak kadar ciddi, gülünecek kadar absürt.
"""

import random
import time

def yanlis_yol_goster(hedef):
    print(f"\nHedef: {hedef}")
    print("Sistem hesaplıyor... (asıl işi rastgele yapmak)")
    time.sleep(1)
    
    yonler = ["sol", "sağ", "düz", "geri dön", "U dönüş yap", "yaya geçidine çık"]
    rastgele_yon = random.choice(yonler)
    mesafe = random.randint(50, 5000)
    
    print(f"\nÖnerilen rota: {rastgele_yon} yönüne {mesafe} metre git.")
    
    yorumlar = [
        "Bu yol en kısası değil ama en uzun macera.",
        "Haritada yok çünkü henüz keşfedilmedi.",
        "Kayyum onaylı yanlışlık.",
        "Eğer kaybolursan, o da planın bir parçasıydı."
    ]
    print(f"Yorum: {random.choice(yorumlar)}")
    
    # Gizli siyasi not (base64 ile saklı, çözersen görürsün)
    # a2F5eXVtIG9uYXlsxLEgYW1hIGdlcsOnZWsgdGFyYWYgZWtpbGkgZGViZWxtZXo=
    print("\nRota tamamlandı. Nereye vardığınız bilinmiyor. Tebrikler!")

if __name__ == "__main__":
    hedef = input("Nereye gitmek istiyorsun? ")
    yanlis_yol_goster(hedef)
