import os
import shutil

#ここのみ変更可能
########################################################################################
#ファイル数                                                                             ##
files_count = 15;                                 
#                                                                                      #
# コピー先のフォルダのパス                                                                 #
folder_next_copy =  "/Users/rinichimrt/Desktop/school/jisshu3/jisshu3_text"            #
#                   #-----------------------------------------------------#            #
# コピーしたいファイルが入っているフォルダのパス                                               #
folder_path = "/Users/rinichimrt/Desktop/copy_file"                                    #
#            #------------------------------------#                                    #  
#                                                                                      #
########################################################################################















def get_file_name(path):
    return os.path.splitext(os.path.basename(path))[0]


def copy_file(file_path, count, copy_dir):
    dir_path = os.path.dirname(file_path)
    file_name = get_file_name(file_path)
    file_ext = os.path.splitext(file_path)[1]

    for i in range(4, count+1):
        copy_path = os.path.join(copy_dir, f"{file_name}_{i}{file_ext}")

        shutil.copy(file_path, copy_path)



# フォルダ内のファイルを取得
files = os.listdir(folder_path)

# フォルダ内の各ファイルに対して処理を実行
for file in files:
    # 拡張子がないファイルは処理をスキップ
    if not os.path.splitext(file)[1]:
        continue
    
    # ファイルを複製する
    file_path = os.path.join(folder_path, file)
    copy_file(file_path, files_count, folder_next_copy)
