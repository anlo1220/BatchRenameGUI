# BatchRenameGUI

📝 **BatchRenameGUI** 是一個簡單易用的 **Python GUI 批量檔案重命名工具**，可讓使用者：
- **批量刪除或替換檔案名稱中的指定字串**
- **透過視覺化介面選擇資料夾，無需手動輸入**
- **選擇是否輸出 `log.txt` 來記錄變更記錄**
- **防止檔案名稱衝突，確保不會覆蓋原有檔案**

## 📷 預覽
![image](https://github.com/user-attachments/assets/6de161d8-54a8-4293-8755-3f1c14275c15)


---

## 🚀 **功能**
✅ **批量重命名**：一次性修改多個檔案名稱  
✅ **字串替換或刪除**：可將特定字串刪除或替換為新字串  
✅ **圖形化界面**：無需命令列操作，簡單直覺  
✅ **選擇是否輸出 `log.txt`**：記錄重命名過程，方便追蹤  
✅ **避免檔案名稱衝突**：若新檔名已存在，則不進行覆蓋  

---

## 🛠 **安裝與執行**
### **1⃣ 安裝 Python**
請確保已安裝 **Python 3.x**，可前往 [Python 官方網站](https://www.python.org/) 下載並安裝。

### **2⃣ 安裝必要套件**
打開端末機（Windows 用戶請使用 `cmd`），並執行：
```sh
pip install tk
```
`tkinter` 是內建於 Python 的 GUI 套件，但某些環境可能需要手動安裝。

### **3⃣ 執行程式**
下載程式碼後，進入該資料夾，執行：
```sh
python rename_gui.py
```
或直接**雙擊 `rename_gui.py`** 即可開啟 GUI 介面。

---

## 📚 **使用方法**
1. 點擊「選擇資料夾」，選擇包含要修改檔案的目錄。
2. 在 **「輸入要刪除或替換的字串」** 欄位輸入要刪除或替換的內容。
3. （可選）在 **「輸入替換後的字串」** 欄位輸入新字串，若留空則表示刪除該字串。
4. （可選）勾選 **「輸出 log.txt」**，將變更記錄儲存到選擇的資料夾內。
5. 點擊「開始重命名」，日誌視窗會顯示變更結果。

---

## 🛠 **技術細節**
- **程式語言**：Python 3.x
- **GUI 套件**：`tkinter`
- **正則處理**：`re.sub()` 用於字串替換
- **檔案操作**：`os.rename()` 處理檔名變更

---

## 📉 **TODO**
- [ ] **增加預覽功能**
- [ ] **支援子資料夾內的檔案重命名**
- [ ] **增加更多重命名選項（大小寫轉換、數字編號等）**
- [ ] **增加多語言支援**

---

## 🐝 **授權**
本專案以 **MIT License** 授權，歡迎自由使用與修改。

🚀 **歡迎 Star & Fork！如果你覺得這個工具有幫助，請點個 ⭐！**

