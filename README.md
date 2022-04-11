> **Note**: This script currently only works with the protocols of the 18. Wahlperiode.

This script splits Bundestags protocols into their table of contents (tos) and main part. The Anlagen part is currently omitted.

Download URLs for all protocols from Wahlperiode 1 to 18 are provided in the `Download URLs by Wahlperiode` folder.

In the `split files` folder are already split files, so you don't need to run the script yourself.

# Setup / Prerequisites

 - Install pdftk cli from "https://www.pdflabs.com/tools/pdftk-server/"
 - Next to your PDF files create two folders named `tos` and `main`.
 - All your PDF files must have their original names (e.g. 18001.pdf)

# Usage
 - To only split one file run `python split_tos_main.py <PATH_TO_PDF>`. It will create two files in the coresponding folder containing only the TOS and the main text.
 - To split all files in a folder run `python split_tos_main.py <PATH_TO_FOLDER>`. It will split all PDF files in the folder.

# Problems
 - Not working reliable for all WPs. Sometimes the bookmarks are missing.
 - For some protocols the automatic splitting does not work. For these split values are hardcoded. As a result this script currently only works with the 18. Wahlperiode (WP18).