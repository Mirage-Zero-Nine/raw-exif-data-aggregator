import csv
import utilities


def read_exif_data_from_csv(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        exif_data_list = [row for row in reader]
    return exif_data_list


def count_photos_by_camera(exif_data_list, export_file_name):
    camera_models_set = set(entry['Camera Model'] for entry in exif_data_list)
    camera_counts = {model: 0 for model in camera_models_set}
    for entry in exif_data_list:
        camera_counts[entry['Camera Model']] += 1

    write_to_csv(['Camera Model', 'Count'], camera_counts, export_file_name)
    return camera_counts


def count_photos_by_lens(exif_data_list, export_file_name):
    lens_models_set = set(entry['Lens Model'] for entry in exif_data_list)
    lens_counts = {model: 0 for model in lens_models_set}
    for entry in exif_data_list:
        lens_counts[entry['Lens Model']] += 1

    write_to_csv(['Lens Model', 'Count'], lens_counts, export_file_name)
    return lens_counts


def count_photos_with_aperture(exif_data_list, export_file_name):
    aperture_set = set(entry['Aperture'] for entry in exif_data_list)
    aperture_count = {aperture: 0 for aperture in aperture_set}
    for entry in exif_data_list:
        aperture_count[entry['Aperture']] += 1
    converted_aperture_map = {convert_to_custom_format(key): value for key, value in aperture_count.items()}
    write_to_csv(['Aperture', 'Count'], converted_aperture_map, export_file_name)
    return converted_aperture_map


def count_photos_with_shutter_speed(exif_data_list, export_file_name):
    shutter_speed_set = set(entry['Shutter Speed'] for entry in exif_data_list)
    shutter_speed_counts = {shutter_speed: 0 for shutter_speed in shutter_speed_set}
    for entry in exif_data_list:
        shutter_speed_counts[entry['Shutter Speed']] += 1

    write_to_csv(['Shutter Speed', 'Count'], shutter_speed_counts, export_file_name)
    return shutter_speed_counts


def count_photos_with_focal_length(exif_data_list, export_file_name):
    focal_length_set = set(entry['Focal Length'] for entry in exif_data_list)
    focal_length_counts = {shutter_speed: 0 for shutter_speed in focal_length_set}
    for entry in exif_data_list:
        focal_length_counts[entry['Focal Length']] += 1

    write_to_csv(['Focal Length', 'Count'], focal_length_counts, export_file_name)
    return focal_length_counts


def write_to_csv(first_row, data_map, file_name):
    # Write distribution report for aperture values to a CSV file
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(first_row)
        for entry, count in data_map.items():
            writer.writerow([entry, count])


def convert_to_custom_format(aperture):
    if '/' in aperture:
        numerator, denominator = aperture.split('/')
        return " ƒ/{:.1f}".format(float(numerator) / float(denominator))
    else:
        return " ƒ/{}".format(aperture)


def generate_statistics_report(config):
    # Read EXIF data from the CSV file
    exif_data_list = read_exif_data_from_csv(config['ExportPath']['export_csv_file_name'])

    # Count number of photos taken by camera
    camera_counts = count_photos_by_camera(exif_data_list, config['ExportFileName']['camera_count'])
    print("Number of photos taken by each camera:")
    for camera_model, count in camera_counts.items():
        print(f"{camera_model}: {count}")

    # Count number of photos taken by lens
    lens_counts = count_photos_by_lens(exif_data_list, config['ExportFileName']['lens_count'])
    print("\nNumber of photos taken by each lens:")
    for lens_model, count in lens_counts.items():
        print(f"{lens_model}: {count}")

    # Count number of photos with specific Aperture
    print("\nNumber of photos taken by each aperture:")
    aperture_counts = count_photos_with_aperture(exif_data_list, config['ExportFileName']['aperture_count'])
    for aperture, count in aperture_counts.items():
        print(f"{aperture}: {count}")

    # Count number of photos with specific Shutter Speed
    print("\nNumber of photos taken by each shutter speed:")
    shutter_speed_counts = count_photos_with_shutter_speed(exif_data_list, config['ExportFileName']['shutter_speed_count'])
    for shutter_speed, count in shutter_speed_counts.items():
        print(f"{shutter_speed}: {count}")

    # Count number of photos with focal length
    print("\nNumber of photos taken by each focal length:")
    focal_length_count = count_photos_with_focal_length(exif_data_list, config['ExportFileName']['focal_length_count'])
    for focal_count, count in focal_length_count.items():
        print(f"{focal_count}: {count}")
