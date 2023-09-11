import os
import csv
import exifread
import yaml


def get_config():
    with open('config/config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config


def collect_exif_data(photo_directory):
    exif_data_list = []

    # Iterate through subdirectories
    for root, dirs, files in os.walk(photo_directory):
        print(f"Collecting data from {os.path.basename(os.path.normpath(root))}")
        for file in files:
            if file.lower().endswith('.arw'):
                # Construct the full path to the file
                file_path = os.path.join(root, file)

                # Open the file for reading EXIF data
                with open(file_path, 'rb') as f:
                    tags = exifread.process_file(f)

                # Get lens model
                lens_model = tags.get('EXIF LensModel', 'Unknown')

                # Collect EXIF data
                exif_data = {
                    'File': file_path,
                    'Camera Make': str(tags.get('Image Make', 'Unknown')),
                    'Camera Model': str(tags.get('Image Model', 'Unknown')),
                    'Focal Length': str(tags.get('EXIF FocalLength', 'Unknown')),
                    'Aperture': str(tags.get('EXIF FNumber', 'Unknown')),
                    'Shutter Speed': str(tags.get('EXIF ExposureTime', 'Unknown')),
                    'ISO': str(tags.get('EXIF ISOSpeedRatings', 'Unknown')),
                    'Lens Model': str(lens_model),
                    'Date Taken': str(tags.get('EXIF DateTimeOriginal', 'Unknown'))
                }

                exif_data_list.append(exif_data)

    return exif_data_list


def write_exif_to_csv(exif_data_list):
    csv_path = f'{get_config()["ExportPath"]["export_csv_file_name"]}'
    with open(csv_path, mode='w', newline='') as csv_file:
        fieldnames = exif_data_list[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for exif_data in exif_data_list:
            writer.writerow(exif_data)
    print(f"Saved combined EXIF data to {csv_path}")
