# python 複製檔案shutil 模組
# 1.shutil.copy(src, dst)
# 會 複製檔案內容 + 複製權限 (permission bits)。
# 不會複製檔案的其他 metadata（例如建立時間、修改時間、擁有者等）。
# dst 可以是：
# 檔案路徑 → 把 src 複製到 dst（新檔案)
# 資料夾路徑 → 把 src 複製到這個資料夾，檔名不變

# 2. shutil.copyfile(src, dst)
# 只會 複製檔案內容，不處理權限、metadata
# src、dst 必須是檔案路徑（不能是資料夾）
# 速度通常比 copy() 快一點（因為少處理 metadata)

# 3. shutil.copy2(src, dst)
# 會 複製檔案內容 + 複製所有 metadata（例如修改時間、存取時間、權限等)
# 是最完整的複製方式，等於 copy() 的加強版
# ✅ 比較表：
#
# 方法	            複製內容	  複製權限 (permission)	複製其他 metadata (時間戳等)	dst 可以是資料夾嗎？
# copyfile(src,dst)	檔案內容	     ❌	                   ❌	                      ❌ (只能檔案)
# copy(src,dst)	    檔案內容	     ✅	                   ❌	                      ✅
# copy2(src,dst)	檔案內容	     ✅	                   ✅	                      ✅

import shutil

#1.copyfile
#2.copy
#3.copy2

#1.copyfile
str4=r"C:\Users\Jasper\Desktop\workspace"
source=f"{str4}/source_file.txt"
destination=f"{str4}/destination_file.txt"
shutil.copyfile(source,destination)

#2.copy