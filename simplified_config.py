import os
import sys

def replace_placeholders(spingest_section_name, total_ingest):
    # Read the contents of 00_SYSTEM_SPDATA.txt
    with open('00_SYSTEM_SPDATA.txt', 'r') as system_file:
        system_content = system_file.read()
    
    # Read the contents of 01_SPINGEST_HEADER.txt
    with open('01_SPINGEST_HEADER.txt', 'r') as template_file:
        template_content = template_file.read()
    
    # Replace placeholders in the template content
    template_content = template_content.replace('{spingest_section_name}', spingest_section_name)
    template_content = template_content.replace('{total_ingest}', str(total_ingest))
    
    # Combine the contents
    output_content = system_content + '\n' + template_content
    
    # Sort the filenames that start with '2'
    sorted_files = sorted([f for f in os.listdir('.') if f.startswith('2')])
    
    # Append the content of the sorted files
    for idx, filename in enumerate(sorted_files):
        with open(filename, 'r') as file:
            file_content = file.read()
            # Replace placeholders in each file's content
            file_content = file_content.replace('{spingest_section_name}', spingest_section_name)
            file_content = file_content.replace('MINE0', f'MINE{idx}')
            output_content += '\n' + file_content
    
    # Write to the output file
    with open('simplified_output.txt', 'w') as output_file:
        output_file.write(output_content)

def replace_miner_placeholders(spminer_section_name, total_miner):
    # Read the existing contents of the output file
    with open('simplified_output.txt', 'r') as system_file:
        system_content = system_file.read()
        
    # Read the contents of 03_SPMINER_HEADER.txt
    with open('03_SPMINER_HEADER.txt', 'r') as template_file:
        template_content = template_file.read()
    
    # Replace placeholders in the template content
    template_content = template_content.replace('{spminer_section_name}', spminer_section_name)
    template_content = template_content.replace('{total_miner}', str(total_miner))
    
    # Combine the contents
    output_content = system_content + '\n' + template_content
    
    # Sort the filenames that start with '3'
    sorted_files = sorted([f for f in os.listdir('.') if f.startswith('3')])
    
    # Append the content of the sorted files
    for idx, filename in enumerate(sorted_files):
        with open(filename, 'r') as file:
            file_content = file.read()
            # Replace placeholders in each file's content
            file_content = file_content.replace('{spminer_section_name}', spminer_section_name)
            file_content = file_content.replace('MINE0', f'MINE{idx}')
            output_content += '\n' + file_content
    
    # Write to the output file
    with open('simplified_output.txt', 'w') as output_file:
        output_file.write(output_content)

def count_files_with_prefix(directory, prefix):
    count = 0
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            count += 1
    return count

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <spingest_section_name> <spminer_section_name>")
        sys.exit(1)

    spingest_section_name = sys.argv[1]
    spminer_section_name = sys.argv[2]
    directory = '.'  # Current directory, you can change this to any directory you want to scan
    
    prefix = '2'
    total_ingest = count_files_with_prefix(directory, prefix)
    replace_placeholders(spingest_section_name, total_ingest)
    
    prefix = '3'
    total_miner = count_files_with_prefix(directory, prefix)
    replace_miner_placeholders(spminer_section_name, total_miner)

    print(f"Output written to simplified_output.txt with section name '{spingest_section_name}' and total ingest '{total_ingest}'")
