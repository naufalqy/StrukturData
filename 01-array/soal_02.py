import matplotlib.pyplot as plt

nilai = []

print("Masukkan 10 nilai siswa:")
for i in range(10):
    n = int(input(f"Nilai ke-{i+1}: "))
    nilai.append(n)

nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1

tidak_lulus = len(nilai) - lulus

# grafik nilai tertinggi dan terendah
plt.bar(["Tertinggi","Terendah"],[nilai_tertinggi,nilai_terendah])
plt.title("Perbandingan Nilai")
plt.show()

# grafik kelulusan
plt.bar(["Lulus","Tidak Lulus"],[lulus,tidak_lulus])
plt.title("Data Kelulusan")
plt.show()
