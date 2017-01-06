#! /bin/bash
latest_release=$(curl -s  "https://api.github.com/repos/adafruit/Adafruit_CircuitPython_Bundle/releases/latest")
download_link=$(echo $latest_release | grep -o "\"browser_download_url\": \"[^\"]*" | cut -d \" -f 4)
tag=$(echo $latest_release | grep -o "\"tag_name\": \"[^\"]*" | cut -d \" -f 4)
current=$(head -n 1 VERSIONS.txt | tr -d '[:space:]')
if [ $? -ne 0 ]
then echo "No VERSIONS.txt please run from lib/"
fi
if [ $current == $tag ]
then echo "Already updated to the latest."; exit 0
fi
save_to=~/Downloads/$(basename $download_link)
echo "Downloading to " $save_to
curl -sL $download_link > $save_to
unzip -o $save_to -d ..
