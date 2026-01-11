import os
import shutil
import locale
from datetime import datetime
import exifread

# Use system default language for month names
locale.setlocale(locale.LC_TIME, '')

def get_creation_date(image_path):
    with open(image_path, 'rb') as file:
        tags = exifread.process_file(file, details=False)
        date_tag = 'EXIF DateTimeOriginal'
        if date_tag in tags:
            date_str = str(tags[date_tag])
            return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
        else:
            return datetime.fromtimestamp(os.path.getmtime(image_path))

def sort_images(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            source_path = os.path.join(source_folder, filename)
            creation_date = get_creation_date(source_path)

            year = creation_date.year
            month_name = creation_date.strftime('%B').capitalize()

            # Month folder includes year
            month_folder_name = f"{month_name} {year}"

            year_folder = os.path.join(destination_folder, str(year))
            month_folder = os.path.join(year_folder, month_folder_name)

            os.makedirs(month_folder, exist_ok=True)

            destination_path = os.path.join(month_folder, filename)
            shutil.move(source_path, destination_path)

def main():
    current_directory = os.getcwd()
    sort_images(current_directory, current_directory)

if __name__ == "__main__":
    main()
