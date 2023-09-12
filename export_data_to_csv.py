import os
import csv
import exifread


def collect_exif_data(photo_directory):
    exif_data_list = []
    total_count = 0
    # Iterate through subdirectories
    for root, dirs, files in os.walk(photo_directory):
        count = 0
        for file in files:
            if file.lower().endswith('.arw'):
                count += 1
                # Construct the full path to the file
                file_path = os.path.join(root, file)

                # Open the file for reading EXIF data
                with open(file_path, 'rb') as f:
                    tags = exifread.process_file(f)

                # Collect EXIF data
                exif_data = {
                    'File': file,
                    'Path': file_path,
                    'Camera Make': str(tags.get('Image Make', 'Unknown')),
                    'Camera Model': str(tags.get('Image Model', 'Unknown')),
                    'Focal Length': str(tags.get('EXIF FocalLength', 'Unknown')),
                    'Aperture': str(tags.get('EXIF FNumber', 'Unknown')),
                    'Shutter Speed': str(tags.get('EXIF ExposureTime', 'Unknown')),
                    'ISO': str(tags.get('EXIF ISOSpeedRatings', 'Unknown')),
                    'Lens Model': str(tags.get('EXIF LensModel', 'Unknown')),
                    'Date Taken': str(tags.get('EXIF DateTimeOriginal', 'Unknown'))
                }

                exif_data_list.append(exif_data)
        print(f"Found {count} RAW files in {os.path.basename(os.path.normpath(root))}")
        total_count += count
    print(f"{total_count} RAW files found.")
    return exif_data_list


def write_exif_to_csv(config, exif_data_list):
    csv_path = f'{config.export_path.export_csv_file_name}'
    with open(csv_path, mode='w', newline='') as csv_file:
        fieldnames = exif_data_list[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for exif_data in exif_data_list:
            writer.writerow(exif_data)
    print(f"Saved combined EXIF data to {csv_path}")
