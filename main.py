import yaml
import utilities
import export_data_to_csv
import read_data_from_csv

# Read the configuration file
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)


def get_exif_data():
    photo_directory = config['FilePaths']['photo_directory']
    utilities.generate_lens_distribution_report(photo_directory)


if __name__ == '__main__':
    # exif_data_list = export_data_to_csv.collect_exif_data(config['FilePaths']['photo_directory'])
    # export_data_to_csv.write_exif_to_csv(exif_data_list)
    read_data_from_csv.generate_statistics_report(config)
