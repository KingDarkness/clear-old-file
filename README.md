# clear-old-file
usage: clearlog.py [-h] -days N -d DIRECTORY

optional arguments:
  -h, --help            show this help message and exit
  -days N               Xoá file tạo trước hiện tại [days] ngày
  -d DIRECTORY, --directory DIRECTORY
                        Danh sách thư mục cần xoá

# cron
chạy m ngày lúc 00:00 
0 0 * * * /usr/bin/python /root/script/clearlog.py -days 15 -d "/var/log" > /dev/null 2>&1
