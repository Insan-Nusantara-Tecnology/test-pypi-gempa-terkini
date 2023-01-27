import gempa_terkini_BMKG

if __name__ == "__main__":
    print("Aplikasi utama")
    result = gempa_terkini_BMKG.ekstraski_data()
    gempa_terkini_BMKG.tampilkan_data(result)