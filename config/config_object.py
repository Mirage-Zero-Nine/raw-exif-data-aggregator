import yaml


class FilePaths:
    def __init__(self, photo_directory):
        self.photo_directory = photo_directory


class ExportPath:
    def __init__(self, export_csv_file_name):
        self.export_csv_file_name = export_csv_file_name


class ExportFileName:
    def __init__(self, camera_count, lens_count, aperture_count, shutter_speed_count, focal_length_count, iso_count):
        self.camera_count = camera_count
        self.lens_count = lens_count
        self.aperture_count = aperture_count
        self.shutter_speed_count = shutter_speed_count
        self.focal_length_count = focal_length_count
        self.iso_count = iso_count


class PlotSavePath:
    def __init__(self, plot_result_save_path):
        self.plot_result_save_path = plot_result_save_path


class ConfigObject:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)

        self.file_paths = FilePaths(config_data['FilePaths']['photo_directory'])
        self.export_path = ExportPath(config_data['ExportPath']['export_csv_file_name'])
        self.export_file_name = ExportFileName(
            config_data['ExportFileName']['camera_count'],
            config_data['ExportFileName']['lens_count'],
            config_data['ExportFileName']['aperture_count'],
            config_data['ExportFileName']['shutter_speed_count'],
            config_data['ExportFileName']['focal_length_count'],
            config_data['ExportFileName']['iso_count']
        )
        self.plot_save_path = PlotSavePath(config_data['PlotSavePath']['plot_result_save_path'])
