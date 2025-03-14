# 📂 Image Sorter by Date

## 🖼️ Automatically Organize Images by Year and Month

This Python script sorts images into folders based on their **creation date (EXIF metadata or file modification date)**.  
It organizes images into **year and month** folders, using the **system’s default language** for month names while ensuring they are capitalized.

---

## 🚀 Features  
✅ Sorts images automatically based on creation date  
✅ Uses EXIF metadata if available  
✅ Falls back to file modification date if EXIF data is missing  
✅ Adapts to system language (localized month names)  
✅ Works on Windows, macOS, and Linux  

---

## 🔧 Installation & Usage  

### 1️⃣ Install Dependencies  
Make sure Python is installed, if not use this link:
[Python](https://www.python.org/downloads/windows/)

Then install the required package:  
```bash
pip install exifread
```

Move the Image_sort.exe into any folder with images and videos and double click the program.

The code then sortes all the images and videos into year and month folders for you.  

```yaml
📂 2023
   📂 January
   📂 February
   📂 March
📂 2024
   📂 January
   📂 February
```


## 📦 Changes and Convert to an Executable

If you make any changes to the code and want to make it an executable use
``` Bash
cd path\to\your\script
pip install pyinstaller
pyinstaller --onefile Image_Sort.py
```

## 📜 License

This project is open-source and available under the MIT License.