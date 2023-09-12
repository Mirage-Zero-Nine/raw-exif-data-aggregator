import date_distribution
import utilities
import export_data_to_csv
import config.config_object as config

# build config object
config = config.ConfigObject('config/config.yml')


def get_exif_data():
    utilities.generate_lens_distribution_report(config.file_paths.photo_directory)


def generate_base_csv_file():
    exif_data_list = export_data_to_csv.collect_exif_data(config)
    export_data_to_csv.write_exif_to_csv(config, exif_data_list)


if __name__ == '__main__':
    # read_data_from_csv.generate_statistics_report(config)
    data_list = utilities.read_exif_data_from_csv(config)
    date_distribution.draw_photo_distribution(config, data_list)
    date_distribution.draw_photo_distribution_by_month(config, data_list)
