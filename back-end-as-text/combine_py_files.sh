#!/bin/bash

# Define the output directory and file
output_dir="/Users/nadav_mbp_m/Documents/DevSecOps-NadavZarfin/wealth-management-app/back-end-as-text"
output_file="$output_dir/combined_output.txt"
skipped_file_log="$output_dir/skipped_files.txt"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Clear the output file and skipped file log if they exist
> "$output_file"
> "$skipped_file_log"

# Iterate over all Python files in the back-end directory and its subdirectories
find /Users/nadav_mbp_m/Documents/DevSecOps-NadavZarfin/wealth-management-app/back-end/ -type f -name "*.py" | while read -r file; do
    echo "Processing $file"
    
    # Check the file type
    file_type=$(file "$file")
    echo "File type: $file_type"
    
    # Check if the file is a text file (not binary)
    if echo "$file_type" | grep -q text; then
        # Print the file path to the output file
        echo "### $file ###" >> "$output_file"
        # Append the contents of the file to the output file
        cat "$file" >> "$output_file"
        # Add a separator line
        echo -e "\n###\n" >> "$output_file"
    else
        echo "Skipping non-text file: $file"
        echo "$file" >> "$skipped_file_log"
    fi
done

echo "All Python files have been combined into $output_file"
echo "Skipped files have been logged in $skipped_file_log"

