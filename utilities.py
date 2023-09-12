from datetime import datetime
import os
import exifread
import csv


def convert_aperture(aperture):
    if '/' in aperture:
        numerator, denominator = aperture.split('/')
        return "{:.1f}".format(float(numerator) / float(denominator))
    else:
        return aperture


def format_datetime(input_datetime):
    # Parse the input string into a datetime object
    dt = create_datatime_object(input_datetime)

    # Format the date with full month name
    formatted_date = dt.strftime('%B %-d, %Y')  # %B: Full month name, %-d: Day of the month (no leading zero)

    # Format the time (including seconds)
    formatted_time = dt.strftime('%I:%M:%S %p')  # %I: Hour (12-hour clock), %M: Minute, %S: Second, %p: AM or PM

    return f"{formatted_date}, {formatted_time}"


def create_datatime_object(input_datetime):
    return datetime.strptime(input_datetime, '%Y:%m:%d %H:%M:%S')


def print_exif(config):
    # Iterate through subdirectories
    for root, dirs, files in os.walk(config.file_paths.photo_directory):
        for file in files:
            if file.endswith('.arw'):
                # Construct the full path to the file
                file_path = os.path.join(root, file)

                # Open the file for reading EXIF data
                with open(file_path, 'rb') as f:
                    tags = exifread.process_file(f)

                # Get camera-related information
                camera_make = tags.get('Image Make', 'Unknown')
                camera_model = tags.get('Image Model', 'Unknown')
                focal_length = tags.get('EXIF FocalLength', 'Unknown')
                aperture = tags.get('EXIF FNumber', 'Unknown')
                shutter_speed = tags.get('EXIF ExposureTime', 'Unknown')
                iso = tags.get('EXIF ISOSpeedRatings', 'Unknown')
                lens_model = tags.get('EXIF LensModel', 'Unknown')
                date_taken = tags.get('EXIF DateTimeOriginal', 'Unknown')

                print(f"File: {os.path.abspath(file_path)}")
                print(f"Date Taken: {format_datetime(str(date_taken))}")
                print(f"Camera: {camera_make} {camera_model}")
                print(f"Focal Length: {focal_length}mm")
                print(f"Aperture: ƒ/{convert_aperture(str(aperture))}")
                print(f"Shutter Speed: {shutter_speed}s")
                print(f"ISO: {iso}")
                print(f"Lens Model: {lens_model}")
                print()


def generate_lens_distribution_report(config):
    # Dictionary to store lens distribution
    lens_distribution = {}

    # Iterate through subdirectories
    for root, dirs, files in os.walk(config.file_paths.photo_directory):
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

                # Update lens distribution dictionary
                if lens_model:
                    lens_model = str(lens_model)
                    lens_distribution[lens_model] = lens_distribution.get(lens_model, 0) + 1

    # Generate report
    print("Lens Distribution Report:")
    for lens_model, count in lens_distribution.items():
        print(f"Lens Model: {lens_model}, Count: {count}")


def convert_aperture_to_readable_format(aperture):
    if '/' in aperture:
        numerator, denominator = aperture.split('/')
        return " ƒ/{:.1f}".format(float(numerator) / float(denominator))
    else:
        return " ƒ/{}".format(aperture)


def read_exif_data_from_csv(config):
    with open(config.export_path.export_csv_file_name, mode='r') as file:
        reader = csv.DictReader(file)
        exif_data_list = [row for row in reader]
    return exif_data_list
