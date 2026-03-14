nilai = []

print("Masukkan 10 nilai siswa:")

for i in range(10):
    n = int(input(f"Nilai ke-{i+1}: "))
    nilai.append(n)

nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

rata_rata = sum(nilai) / len(nilai)

lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1

tidak_lulus = len(nilai) - lulus

print("\n===== HASIL =====")
print("Nilai tertinggi :", nilai_tertinggi)
print("Nilai terendah :", nilai_terendah)
print("Rata-rata :", rata_rata)
print("Jumlah lulus :", lulus)
print("Jumlah tidak lulus :", tidak_lulus)
