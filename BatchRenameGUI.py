import os
import re
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

def select_folder():
    """ 打開資料夾選擇對話框 """
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)
        log_message(f"📂 選擇的資料夾: {folder_selected}\n")

def rename_files():
    """ 執行檔案重命名（替換或刪除字串） """
    selected_directory = folder_path.get().strip()
    target_text = target_text_var.get().strip()
    replace_text = replace_text_var.get().strip()
    save_log = save_log_var.get()

    if not selected_directory:
        messagebox.showerror("錯誤", "請先選擇資料夾！")
        return
    
    if not os.path.exists(selected_directory):
        messagebox.showerror("錯誤", "選擇的資料夾不存在！")
        return

    if not target_text:
        messagebox.showerror("錯誤", "請輸入要刪除或替換的字串！")
        return

    log_message(f"📂 處理資料夾: {selected_directory}\n")
    log_message(f"🔍 目標字串: {target_text}\n")
    log_message(f"🔄 替換為: {'(刪除字串)' if not replace_text else replace_text}\n\n")

    renamed_count = 0
    pattern = re.escape(target_text)
    log_entries = []

    try:
        for filename in os.listdir(selected_directory):
            file_path = os.path.join(selected_directory, filename)

            if os.path.isfile(file_path):
                new_filename = re.sub(pattern, replace_text, filename).strip()

                if new_filename != filename:
                    new_filepath = os.path.join(selected_directory, new_filename)

                    if not os.path.exists(new_filepath):
                        os.rename(file_path, new_filepath)
                        log_msg = f'✅ 已重命名: {filename} -> {new_filename}\n'
                        log_message(log_msg)
                        log_entries.append(log_msg)
                        renamed_count += 1
                    else:
                        log_msg = f'⚠ 無法重命名，檔案已存在: {new_filename}\n'
                        log_message(log_msg)
                        log_entries.append(log_msg)
        
        summary_msg = f"\n🎉 總共重命名 {renamed_count} 個檔案。\n" if renamed_count else "📌 未發現需要重命名的檔案。\n"
        log_message(summary_msg)
        log_entries.append(summary_msg)
    
        if save_log:
            log_file_path = os.path.join(selected_directory, "log.txt")
            with open(log_file_path, "w", encoding="utf-8") as log_file:
                log_file.writelines(log_entries)
            log_message(f"💾 日誌已儲存至: {log_file_path}\n")
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤: {str(e)}")

def log_message(message):
    """ 在日誌區域顯示訊息並自動滾動 """
    log_text.insert(tk.END, message + "\n")
    log_text.yview(tk.END)

# 創建 GUI 介面
root = tk.Tk()
root.title("批量重命名工具")
root.geometry("600x500")

# 變數來存儲選擇的資料夾與用戶輸入
folder_path = tk.StringVar()
target_text_var = tk.StringVar()
replace_text_var = tk.StringVar()
save_log_var = tk.BooleanVar()

# 選擇資料夾按鈕
select_button = tk.Button(root, text="選擇資料夾", command=select_folder)
select_button.pack(pady=5)

# 顯示所選資料夾的文字框
folder_label = tk.Label(root, textvariable=folder_path, wraplength=500, fg="blue")
folder_label.pack(pady=5)

# 輸入要刪除或替換的字串
tk.Label(root, text="輸入要刪除或替換的字串：").pack()
target_entry = tk.Entry(root, textvariable=target_text_var, width=50)
target_entry.pack(pady=5)

# 輸入替換的文字（可選）
tk.Label(root, text="輸入替換後的字串（留空則刪除）：").pack()
replace_entry = tk.Entry(root, textvariable=replace_text_var, width=50)
replace_entry.pack(pady=5)

# 是否輸出 log.txt 選項
save_log_checkbox = tk.Checkbutton(root, text="輸出 log.txt", variable=save_log_var)
save_log_checkbox.pack(pady=5)

# 建立滾動文字框來顯示日誌
log_text = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
log_text.pack(padx=10, pady=10)

# 開始重命名按鈕
rename_button = tk.Button(root, text="開始重命名", command=rename_files)
rename_button.pack(pady=5)

# 啟動 GUI
root.mainloop()
