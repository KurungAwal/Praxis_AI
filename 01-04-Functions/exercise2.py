def hitung_huruf(teks):
    
    frekuensi_huruf = {}
    
    
    for huruf in teks:
        if huruf.isalpha():  
            huruf = huruf.lower() 
            if huruf in frekuensi_huruf:
                frekuensi_huruf[huruf] += 1
            else:
                frekuensi_huruf[huruf] = 1
    
    return frekuensi_huruf

teks = "budi mulkidi"
hasil = hitung_huruf(teks)
print(hasil)
