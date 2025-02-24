import os
import re
import tkinter as tk
from tkinter import filedialog, scrolledtext

def select_folder():
    """ 打開資料夾選擇對話框 """
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)
        log_text.insert(tk.END, f"📂 選擇的資料夾: {folder_selected}\n\n")

def rename_files():
    """ 執行檔案重命名（替換或刪除字串） """
    selected_directory = folder_path.get()
    target_text = target_text_var.get().strip()
    replace_text = replace_text_var.get().strip()
    save_log = save_log_var.get()  # 是否儲存 log.txt

    if not selected_directory:
        log_text.insert(tk.END, "❌ 請先選擇資料夾！\n")
        return

    if not target_text:
        log_text.insert(tk.END, "❌ 請輸入要刪除或替換的字串！\n")
        return

    log_text.insert(tk.END, f"📂 處理資料夾: {selected_directory}\n")
    log_text.insert(tk.END, f"🔍 目標字串: {target_text}\n")
    log_text.insert(tk.END, f"🔄 替換為: {'(刪除字串)' if not replace_text else replace_text}\n\n")

    renamed_count = 0
    pattern = re.escape(target_text)  # 確保特殊字元可以匹配
    log_entries = []  # 存放日誌內容

    for filename in os.listdir(selected_directory):
        file_path = os.path.join(selected_directory, filename)

        if os.path.isfile(file_path):
            new_filename = re.sub(pattern, replace_text, filename).strip()

            if new_filename != filename:  # 只修改有變動的檔案
                new_filepath = os.path.join(selected_directory, new_filename)

                if not os.path.exists(new_filepath):
                    os.rename(file_path, new_filepath)
                    log_message = f'✅ 已重命名: {filename} -> {new_filename}\n'
                    log_text.insert(tk.END, log_message)
                    log_entries.append(log_message)
                    renamed_count += 1
                else:
                    log_message = f'⚠ 無法重命名，檔案已存在: {new_filename}\n'
                    log_text.insert(tk.END, log_message)
                    log_entries.append(log_message)

    if renamed_count == 0:
        log_message = "📌 未發現需要重命名的檔案。\n"
        log_text.insert(tk.END, log_message)
        log_entries.append(log_message)
    else:
        log_message = f"\n🎉 總共重命名 {renamed_count} 個檔案。\n"
        log_text.insert(tk.END, log_message)
        log_entries.append(log_message)

    log_text.yview(tk.END)  # 自動滾動到最新日誌

    # 如果使用者選擇了儲存 log.txt
    if save_log:
        log_file_path = os.path.join(selected_directory, "log.txt")
        with open(log_file_path, "w", encoding="utf-8") as log_file:
            log_file.writelines(log_entries)
        log_text.insert(tk.END, f"💾 日誌已儲存至: {log_file_path}\n")

# 創建 GUI 介面
root = tk.Tk()
root.title("批量重命名工具")

# 變數來存儲選擇的資料夾
folder_path = tk.StringVar()
target_text_var = tk.StringVar()
replace_text_var = tk.StringVar()
save_log_var = tk.BooleanVar()  # 是否輸出 log.txt

# 選擇資料夾按鈕
select_button = tk.Button(root, text="選擇資料夾", command=select_folder)
select_button.pack(pady=5)

# 顯示所選資料夾的文字框
folder_label = tk.Label(root, textvariable=folder_path, wraplength=500)
folder_label.pack(pady=5)

# 輸入要刪除或替換的字串
target_label = tk.Label(root, text="輸入要刪除或替換的字串：")
target_label.pack()
target_entry = tk.Entry(root, textvariable=target_text_var, width=50)
target_entry.pack(pady=5)

# 輸入替換的文字（可選）
replace_label = tk.Label(root, text="輸入替換後的字串（留空則刪除）：")
replace_label.pack()
replace_entry = tk.Entry(root, textvariable=replace_text_var, width=50)
replace_entry.pack(pady=5)

# 是否輸出 log.txt 選項
save_log_checkbox = tk.Checkbutton(root, text="輸出 log.txt", variable=save_log_var)
save_log_checkbox.pack(pady=5)

# 建立滾動文字框來顯示日誌
log_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
log_text.pack(padx=10, pady=10)

# 開始重命名按鈕
rename_button = tk.Button(root, text="開始重命名", command=rename_files)
rename_button.pack(pady=5)

# 啟動 GUI
root.mainloop()
