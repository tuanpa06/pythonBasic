# Hàm nhập thông tin cầu thủ
def nhap_cau_thu():
    global so_luong, ten1, goal1, vi_tri_da1, ten2, goal2, vi_tri_da2, ten3, goal3 , vi_tri_da3

    so_luong = int(input("Nhập số cầu thủ (tối đa 3): "))
    if so_luong > 3:
        print("Chỉ cho phép tối đa 3 cầu thủ.")
        so_luong = 3

    for i in range(1, so_luong + 1):
        print(f"\n--- Nhập thông tin cầu thủ {i} ---")
        ten = input("Nhập tên: ")
        ban_thang = float(input("Nhập số bàn thắng ghi được: "))
        vi_tri = (input("Nhập vị trí sở trường của bạn: "))

        if i == 1:
            ten1 = ten
            goal1 = ban_thang
            vi_tri_da1 = vi_tri
        elif i == 2:
            ten2 = ten
            goal2 = ban_thang
            vi_tri_da2 = vi_tri
        elif i == 3:
            ten3 = ten
            goal3 = ban_thang
            vi_tri_da3 = vi_tri

# Hàm hiển thị thông tin cầu thủ
def thong_tin_cau_thu():
    if so_luong == 0:
        print("Chưa có dữ liệu cầu thủ. Vui lòng nhập trước.")
        return

    print("\n===== DANH SÁCH CẦU THỦ =====")
    print("{:<5} {:<20} {:<10} {:<10}".format("STT", "Tên", "Bàn thắng", "Vị trí đá"))

    for i in range(1, so_luong + 1):
        if i == 1:
            print("{:<5} {:<20} {:<10} {:<10}".format(i, ten1, goal1, vi_tri_da1))
        elif i == 2:
            print("{:<5} {:<20} {:<10} {:<10}".format(i, ten2, goal2, vi_tri_da2))
        elif i == 3:
            print("{:<5} {:<20} {:<10} {:<10}".format(i, ten3, goal3, vi_tri_da3))

# Thông tin HLV
def thong_tin_HLV(): 
    thong_tin_HLV1 = {
        "ten": "Nguyễn Văn A",
        "tuoi": 45,
        "quoc_tich": "Việt Nam",
        "kinh_nghiem": "15 năm",
        "so_tran_dan_dat": 120
    }

    print("\n--- THÔNG TIN HUẤN LUYỆN VIÊN HIỆN TẠI ---")
    print("Họ tên          : " + thong_tin_HLV1["ten"])
    print("Tuổi            : " + str(thong_tin_HLV1["tuoi"]))
    print("Quốc tịch       : " + thong_tin_HLV1["quoc_tich"])
    print("Kinh nghiệm     : " + thong_tin_HLV1["kinh_nghiem"])
    print("Số trận dẫn dắt : " + str(thong_tin_HLV1["so_tran_dan_dat"]))

# Chiến thuật thi đấu
def chien_thuat_thi_dau():
    chien_thuat = {
        "ten_chien_thuat": "Cầm bóng đến chết",
        "so_do_doi_hinh": "4-3-3",
        "phong_cach_choi": "Kiểm soát bóng và pressing ngay khi mất bóng",
        "ghi_chu": "Thích hợp khi gặp đối thủ yếu hơn, cần giữ nhịp độ trận đấu."
    }

    print("\n--- CHIẾN THUẬT THI ĐẤU HIỆN TẠI ---")
    print("Tên chiến thuật  : " + chien_thuat["ten_chien_thuat"])
    print("Sơ đồ đội hình    : " + chien_thuat["so_do_doi_hinh"])
    print("Phong cách chơi   : " + chien_thuat["phong_cach_choi"])
    print("Ghi chú           : " + chien_thuat["ghi_chu"])

# Lịch sử các trận 
def lich_su_thi_dau():
    lich_su = [
        {
            "ngay": "12/03/2025",
            "doi_thu": "FC Barcelona",
            "ket_qua": "Thắng 3-1",
        },
        {
            "ngay": "18/03/2025",
            "doi_thu": "Bayern Munich",
            "ket_qua": "Hòa 2-2",
        },
        {
            "ngay": "25/03/2025",
            "doi_thu": "Real MAdrid",
            "ket_qua": "Thua 0-1",
        }
    ]

    print("\n--- LỊCH SỬ CÁC TRẬN ĐẤU ---")
    i = 1
    for tran in lich_su:
        print("\nTrận " + str(i) + ":")
        print("Ngày        : " + tran["ngay"])
        print("Đối thủ     : " + tran["doi_thu"])
        print("Kết quả     : " + tran["ket_qua"])
        print("Ghi chú     : " + tran["ghi_chu"])
        i += 1

# Hiệu suất thi đấu
def Hieu_suat_thi_dau():
    thong_ke = {
        "so_tran": 20,
        "thang": 12,
        "hoa": 5,
        "thua": 3,
        "ban_thang": 30,
        "ban_thua": 15
    }

    ty_le_thang = round(thong_ke["thang"] / thong_ke["so_tran"] * 100, 2)

    print("\n--- THỐNG KÊ HIỆU SUẤT THI ĐẤU ---")
    print("Tổng số trận     :", thong_ke["so_tran"])
    print("Thắng            :", thong_ke["thang"])
    print("Hòa              :", thong_ke["hoa"])
    print("Thua             :", thong_ke["thua"])
    print("Bàn thắng        :", thong_ke["ban_thang"])
    print("Bàn thua         :", thong_ke["ban_thua"])
    print("Tỷ lệ thắng      :", str(ty_le_thang) + "%")

# Chương trình chính sử dụng vòng lặp while            
def main():
    while True:
         print("\n===== QUẢN LÝ ĐỘI BÓNG =====")
         print("1. Nhập danh sách cầu thủ")
         print("2. Thông tin cầu thủ")
         print("3. Quản lý huấn luyện viên")
         print("4. Chiến thuật thi đấu")
         print("5. Lịch sử các trận đấu")
         print("6. Thống kê hiệu suất")
         print("7. Thoát chương trình quản lý")
         chon = input("Chọn chức năng (1-7): ")
         if chon == "1":
             nhap_cau_thu()
         elif chon == "2":
             thong_tin_cau_thu()
         elif chon == "3":
             thong_tin_HLV()
         elif chon == "4":
             chien_thuat_thi_dau()
         elif chon == "5":
             lich_su_thi_dau()
         elif chon == "6":
             Hieu_suat_thi_dau()
         elif chon == "7":
             print("Kết thúc chương trình. Tạm biệt!")
             break #thoát khỏi vòng lặp
         else:
             print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
main()