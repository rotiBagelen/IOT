function hapusHistory() {
  const konfirmasi = confirm("Apakah yakin ingin menghapus seluruh riwayat akses?");
  if (konfirmasi) {
    fetch("/api/delete-history", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ delete: konfirmasi })
    })
    .then(response => {
      if (response.ok) {
        // Jika berhasil, reload halaman
        window.location.reload();
      } else {
        alert("Gagal menghapus riwayat.");
      }
    })
    .catch(error => {
      console.error("Terjadi kesalahan:", error);
    });
  }
}
