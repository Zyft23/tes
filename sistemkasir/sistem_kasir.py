
class Produk:
  def __init__(self, nama, harga, stok):
    self.nama = nama
    self.harga = harga
    self.stok = stok

class Keranjang:
  def __init__(self, member=False):
    self.daftar_barang = []
    self.__bayar = 0
    self.member = member

  def tambah_produk(self, produk_baru, jumlah=1):
    if produk_baru.stok < jumlah:
      print(f"Stok {produk_baru.nama} tidak cukup. Stok tersedia: {produk_baru.stok}")
      return
    for _ in range(jumlah):
      self.daftar_barang.append(produk_baru)
    print(f"Berhasil menambah: {produk_baru.nama} (x{jumlah}) ke keranjang.")

  def hapus_produk(self, produk_hapus):
    if produk_hapus in self.daftar_barang:
      self.daftar_barang.remove(produk_hapus)
      print(f"Berhasil menghapus: {produk_hapus.nama} dari keranjang.")
    else:
      print(f"{produk_hapus.nama} tidak ditemukan di keranjang.")

  def hitung_total(self):
    total = 0
    for barang in self.daftar_barang:
      total += barang.harga
    return total

  def hitung_diskon(self, total):
    if self.member and total > 100000:
      return total * 0.15
    elif self.member:
      return total * 0.1
    elif total > 100000:
      return total * 0.05
    else:
      return 0

  def hitung_ppn(self, total_setelah_diskon):
    return round(total_setelah_diskon * 0.11)

  def hitung_total_akhir(self):
    total = self.hitung_total()
    diskon = self.hitung_diskon(total)
    total_setelah_diskon = total - diskon
    ppn = self.hitung_ppn(total_setelah_diskon)
    return total_setelah_diskon + ppn, diskon, ppn

  def cetak_struk(self):
    print("\n=== Struk Belanja ===")
    for barang in self.daftar_barang:
      print(f"- {barang.nama} : Rp{barang.harga}")

    total = self.hitung_total()
    diskon = self.hitung_diskon(total)
    total_setelah_diskon = total - diskon
    ppn = self.hitung_ppn(total_setelah_diskon)
    total_akhir = total_setelah_diskon + ppn

    if diskon > 0:
      if self.member and total > 100000:
        print(f"\nDiskon (15%) \t: -Rp{int(diskon)}")
      elif self.member:
        print(f"\nDiskon (10%) \t: -Rp{int(diskon)}")
      else:
        print(f"\nDiskon (5%) \t: -Rp{int(diskon)}")
    else:
      print("\nTidak ada diskon")

    print(f"PPN (11%) \t: Rp{ppn}")
    print(f"Total Akhir \t: Rp{int(total_akhir)}")
    return total_akhir

  @property
  def bayar(self):
    return self.__bayar

  @bayar.setter
  def bayar(self, jumlah_bayar):
    total_akhir, diskon, ppn = self.hitung_total_akhir()
    if total_akhir <= 0:
      print("Keranjang kosong. Harap isi keranjang.")
      return
    if jumlah_bayar <= 0:
      print("Jumlah bayar harus lebih dari 0.")
      return

    kembalian = jumlah_bayar - total_akhir
    if kembalian >= 0:
      print(f"Berhasil Bayar Rp{jumlah_bayar}, Kembalian Rp{int(kembalian)}")
      self.__bayar = jumlah_bayar
    else:
      print("Jumlah bayar tidak cukup.")
    