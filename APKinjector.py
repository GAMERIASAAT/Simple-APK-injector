import argparse
import os
import shutil

# Set up the argparse ArgumentParser
parser = argparse.ArgumentParser()

# Add the command-line arguments
parser.add_argument("original_apk", help="The path to the original APK file")
parser.add_argument("payload_apk", help="The path to the payload APK file")
parser.add_argument("output_apk", help="The path to the output APK file")

# Parse the command-line arguments
args = parser.parse_args()

# Use the 'apktool' command to decompile the original APK
os.system("apktool d " + args.original_apk)

# Use the 'apktool' command to decompile the payload APK
os.system("apktool d " + args.payload_apk)

# Move the files from the payload APK's 'assets' folder
# to the original APK's 'assets' folder
os.system("mv " + args.payload_apk.split(".apk")[0] + "/assets/* " + args.original_apk.split(".apk")[0] + "/assets/")

# copy the 'lib' folder from payload APK to original APK
shutil.copytree(args.payload_apk.split(".apk")[0]+'/lib', args.original_apk.split(".apk")[0]+'/lib', dirs_exist_ok=True)

# Recompile the modified APK
os.system("apktool b " + args.original_apk.split(".apk")[0] + " -o " + args.output_apk)
