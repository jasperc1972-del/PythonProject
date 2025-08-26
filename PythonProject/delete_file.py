#python os module
import os
import shutil
path=r"C:\Users\Jasper\Desktop\workspace"
#刪除檔案
#os.remove(f"{path}/src.txt")
# 刪除空的資料夾
# os.rmdir(f"{path}/dir1")
# 刪除資料夾及其內容
#shutil.rmtree(f"{path}/dir1")
# 丟到資源回收桶
import send2trash

send2trash.send2trash(fr"{path}\test3.txt")

