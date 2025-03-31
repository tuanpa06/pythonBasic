print("--------------------------------------------------------------------")
print("1.Mã nhân viên")
print("2.Phòng ban")
print("3.Lương nhân viên")
print("4.Thêm nhân viên")
print("5.Xóa nhân viên")
print("6.Lọc nhân viên theo phòng ban")
print("7.Hiển thị danh sách sinh viên")
print("8.Sửa thông tin nhân viên")
print("9.Xuất danh sách nhân viên ra file")
print("10.Thoát chương trình")
yeu_cau_cua_ban = int(input("Nhập lựa chọn của bạn: "))
if yeu_cau_cua_ban == 1:
    print("Thi triển Skill: 1.Mã nhân viên")
elif yeu_cau_cua_ban == 2:
    print("Thi triển Skill: 2.Phòng ban")
elif yeu_cau_cua_ban == 3:
    print("Thi triển Skill: 3.Lương nhân viên")
elif yeu_cau_cua_ban == 4:
    print("Thi triển Skill: 4.Thêm nhân viên")
elif yeu_cau_cua_ban == 5:
    print("Thi triển Skill: 5.Xóa nhân viên")
elif yeu_cau_cua_ban == 6:
    print("Thi triển Skill: 6.Lọc nhân viên theo phòng ban")
elif yeu_cau_cua_ban == 7:
    print("Thi triển Skill: 7.Hiển thị danh sách sinh viên")
elif yeu_cau_cua_ban == 8:
    print("Thi triển Skill: 8.Sửa thông tin nhân viên")
elif yeu_cau_cua_ban == 9:
    print("Thi triển Skill: 9.Xuất danh sách nhân viên ra file")
elif yeu_cau_cua_ban == 10:
    print("Thi triển Skill: 10.Thoát chương trình")
else:
    print("Lựa chọn không phù hợp, vui lòng thử lại")    