# KAMUS
# adminORuser : string

def help(adminORuser): # F14 - Help
    if adminORuser == "admin":
        print('''
        ============HELP============
        register - untuk melakukan registrasi user baru
        login - untuk melakukan login ke dalam sistem
        tambah_game - Untuk menambah game yang dijual pada toko
        ubah_game - mengubah game yang ad di toko
        ubah_stok - mengubah stok game yang ad di toko
        list_game_toko - Untuk melihat list game yang dijual pada toko
        search_game_at_store - melakukan pencarian game di toko
        topup - menambahkan saldo kepada user
        help - untuk memberikan panduan penggunaan sistem
        save - untuk menyimpan data
        exit - untuk keluar dari aplikasi
        ''')
    else:
        print('''
        ---HELP---
        login - untuk melakukan login ke dalam sistem
        list_game_toko - Untuk melihat list game yang dijual pada toko
        buy_game - membeli game yang terdapat di toko
        list_game - melihat daftar game yang dimiliki pengguna
        search_my_game - memberikan informasi game yang di dalam inventory user
        search_game_at_store - melakukan pencarian game di toko
        riwayat - melihat riwayat pembelian game
        help - untuk memberikan panduan penggunaan sistem
        save - untuk menyimpan data
        exit - untuk keluar dari aplikasi
        ''')
