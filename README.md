Archur
======
  
Generates random arch wallpapers from a text file!  
Based on [this reddit
thread](https://www.reddit.com/r/archlinux/comments/4gc2lw/some_arch_wallpapers_i_made/)
 
  
Depends on pillow

Updated to work in 2024. Now includes "-n" number of images and "-o" save to folder.

```
 ╰─λ archur -h
usage: archur [-h] -o OUTPUT_DIR [-n NUM_IMAGES] [-t THEME] [--text TEXT] [-r RESOLUTION] [-ts TEXT_SCALE] [-ls LOGO_SCALE] [-fg FOREGROUND_COLOR]
              [-bg BACKGROUND_COLOR]

Generate random Arch wallpapers

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory for images
  -n NUM_IMAGES, --num-images NUM_IMAGES
                        Number of images to generate
  -t THEME, --theme THEME
                        The theme to use, else random. 'black', 'solarized', 'standart' or 'inverted'
  --text TEXT           Text on the picture, or "random"
  -r RESOLUTION, --resolution RESOLUTION
                        Sets the resolution of the image. Example: 1920x1080
  -ts TEXT_SCALE, --text-scale TEXT_SCALE
                        Sets scale for the text. Example: 1.75
  -ls LOGO_SCALE, --logo-scale LOGO_SCALE
                        Sets scale for the logo. Example: 3.0
  -fg FOREGROUND_COLOR, --foreground-color FOREGROUND_COLOR
                        Color for the text and the logo.
  -bg BACKGROUND_COLOR, --background-color BACKGROUND_COLOR
                        Color for the background.

```
