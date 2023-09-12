# raw-exif-data-aggregator

## What's this?

It's a tool to collect exif data from camera RAW file, then save the data to a CSV file. It also contains some data
visualization tools (WIP) to generate some statistics for the photos.

I got the idea because I wanted to know how many pictures were taken with each of my cameras and lenses.

Lightroom can filter the photos taken by specific camera, lens, but it's not able to create an smart album for that.

Lightroom Classic can do this, but it's not included in my Adobe subscription.

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

PlotSavePath:
  plot_result_save_path: ./plot/
```