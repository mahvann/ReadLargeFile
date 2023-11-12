# 7 giây
# import time
# from collections import Counter
# import re
#
# # Đường dẫn đến file txt của bạn
# file_path = 'D:\\ReadLargeFile\\log\\log.txt'
# start = time.time()
# count = 0
# # Sử dụng Counter để đếm số lượng xuất hiện của mỗi địa chỉ IP
# ip_counter = Counter()
#
# # Mở file và đọc từng dòng
# with open(file_path, 'r') as file:
#     for line in file:
#         # Sử dụng biểu thức chính quy để tìm địa chỉ IP trong mỗi dòng
#         match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
#         if match:
#             ip = match.group()
#             ip_counter[ip] += 1
# end = time.time()
# print("Execution time in seconds: ",(end-start))
# # In ra 10 địa chỉ IP xuất hiện nhiều nhất
# for ip, count in ip_counter.most_common(10):
#     print(f'{ip}: {count} lần')


# 5 giây
import time
from collections import Counter
import re
from multiprocessing import Pool

def process_line(line):
    match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
    return match.group() if match else None

def process_file_chunk(chunk):
    ip_counter = Counter()
    for line in chunk:
        ip = process_line(line)
        if ip:
            ip_counter[ip] += 1
    return ip_counter

def main():
    file_path = 'D:\\ReadLargeFile\\log\\log.txt'
    chunk_size = 3000  # Điều chỉnh kích thước của từng phần
    start = time.time()

    with open(file_path, 'r') as file:
        pool = Pool()
        lines = file.readlines()
        chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
        results = pool.imap_unordered(process_file_chunk, chunks)
        pool.close()
        pool.join()

    ip_counter = Counter()
    for result in results:
        ip_counter.update(result)

    end = time.time()
    print("Execution time in seconds: ", (end - start))

    # In ra 10 địa chỉ IP xuất hiện nhiều nhất
    for ip, count in ip_counter.most_common(10):
        print(f'{ip}: {count} lần')

if __name__ == "__main__":
    main()


# 8 giây
# import time
# from collections import Counter
# import re
# import mmap
# from concurrent.futures import ThreadPoolExecutor
#
# def process_line(line):
#     # Chuyển đối tượng line thành bytes nếu nó là chuỗi Unicode
#     line = line.encode('utf-8') if isinstance(line, str) else line
#     match = re.search(rb'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
#     return match.group() if match else None
#
# def process_file_chunk(chunk):
#     ip_counter = Counter()
#     for line in chunk:
#         ip = process_line(line)
#         if ip:
#             ip_counter[ip] += 1
#     return ip_counter
#
# def main():
#     file_path = 'D:\\ReadLargeFile\\log\\log.txt'
#     chunk_size = 1000  # Điều chỉnh kích thước của từng phần
#     start = time.time()
#
#     with open(file_path, 'r', encoding='utf-8') as file:
#         mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
#         lines = mmapped_file.read().splitlines()
#         mmapped_file.close()
#
#     # Chuyển đổi đối tượng bytes thành chuỗi
#     lines = [line.decode('utf-8') if isinstance(line, bytes) else line for line in lines]
#
#     with ThreadPoolExecutor() as executor:
#         chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
#         results = executor.map(process_file_chunk, chunks)
#
#     ip_counter = Counter()
#     for result in results:
#         ip_counter.update(result)
#
#     end = time.time()
#     print("Execution time in seconds: ", (end - start))
#
#     # In ra 10 địa chỉ IP xuất hiện nhiều nhất
#     for ip, count in ip_counter.most_common(10):
#         print(f'{ip}: {count} lần')
#
# if __name__ == "__main__":
#     main()








