#!/bin/bash

# Define the output directory and file
output_dir="/Users/nadav_mbp_m/Documents/DevSecOps-NadavZarfin/wealth-management-app/back-end-as-text"
output_file="$output_dir/combined_output.txt"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Clear the output file if it exists
> "$output_file"

# Iterate over all files in the back-end directory and its subdirectories
find /Users/nadav_mbp_m/Documents/DevSecOps-NadavZarfin/wealth-management-app/back-end/ -type f | while read -r file; do
    echo "Processing $file"
    # Print the file path to the output file
    echo "### $file ###" >> "$output_file"
    # Append the contents of the file to the output file
    cat "$file" >> "$output_file"
    # Add a separator line
    echo -e "\n###\n" >> "$output_file"
done

echo "All files have been combined into $output_file"

