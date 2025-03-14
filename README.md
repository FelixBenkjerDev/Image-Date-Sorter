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

---

## 🔧 Installation & Usage  

### Install Dependencies  
**Make sure Python** is installed, if not use this link:
[Python](https://www.python.org/downloads/windows/)

Then install the required package:  
```bash
pip install exifread
```

### Usage 

**Move the Image_sort.exe** into any folder with images and videos and double click the program.

The code then sortes all the images and videos into year and month folders for you.  

```yaml
🖼️ 20230122_9521
🖼️ 20230213_2131
🖼️ 20240201_2321
[...1000]
🎞️ 20240128_1234
🤖 Image_sort.exe
```
into ⬇️
```yaml
📂 2023
   📂 January
   📂 February
   📂 March
📂 2024
   📂 January
   📂 February
🤖 Image_sort.exe
```
You can **keep the program in the folder** and when **new photos and or videos are added run the program** again and it will sort it into the exsisting folders again.  

```yaml
[...]
📂 2024
   📂 January
   📂 February
🤖 Image_sort.exe
🖼️ 20240122_9521
🖼️ 20240213_2131
🖼️ 20240201_2321
```
into ⬇️
```yaml
[...]
📂 2024
   📂 January
   📂 February
🤖 Image_sort.exe
```

## 📦 [advanced user] Changes and Convert to an Executable

If you make any changes to the code and want to make it an executable use
``` Bash
cd path\to\the\script
pip install pyinstaller
pyinstaller --onefile Image_Sort.py
```

## 📜 License

This project is open-source and available under the MIT License.