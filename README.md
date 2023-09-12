# raw-exif-data-aggregator

## How to use the script?

1. Install dependency from `requirement.txt`.
2. Create a `.yml` file under `./config`, to include the photo files. See sample below

## Sample config:

```yaml
FilePaths:
  photo_directory: <REPLACE_WITH_YOUR_FILE_PATH>

ExportPath:
  export_csv_file_name: ./csv/exif_data.csv

ExportFileName:
  camera_count: ./csv/camera_count.csv
  lens_count: ./csv/lens_count.csv
  aperture_count: ./csv/aperture_count.csv
  shutter_speed_count: ./csv/shutter_speed_count.csv
  focal_length_count: ./csv/focal_length_count.csv
  iso_count: ./csv/iso_count.csv
```