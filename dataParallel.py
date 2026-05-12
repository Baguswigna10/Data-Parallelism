from multiprocessing import Pool, current_process
import time

def hitung_kuadrat(data):
    nama_proses = current_process().name

    print(f"{nama_proses} memproses data: {data}")

    total = 0

    for angka in data:
        total += angka ** 2
        time.sleep(0.5)

    print(f"{nama_proses} selesai dengan hasil: {total}\n")

    return total

if __name__ == "__main__":

    data_utama = list(range(1, 21))

    bagian_data = [
        data_utama[0:5],
        data_utama[5:10],
        data_utama[10:15],
        data_utama[15:20]
    ]

    print("DATA PARALLELISM\n")

    start = time.time()

    with Pool(processes=4) as pool:
        hasil = pool.map(hitung_kuadrat, bagian_data)

    total_akhir = sum(hasil)

    end = time.time()

    print("HASIL AKHIR")
    print(f"Total seluruh hasil: {total_akhir}")
    print(f"Waktu eksekusi: {end - start:.2f} detik")