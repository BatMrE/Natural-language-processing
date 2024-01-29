import requests
import pandas as pd

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def dat_to_df(dat_file_path, output_file_path):
  with open(dat_file_path, 'r') as dat_file:
      lines = dat_file.readlines()

  filtered_lines = [line for line in lines if '$' not in line or not any(char.isdigit() for char in line)]

  with open(output_file_path, 'w') as output_file:
      output_file.writelines(filtered_lines)

  with open('your_output_file.txt', 'r') as file:
      lines = file.read().replace('!', '').replace('\n', '').split(',')

  df = pd.DataFrame([{'Correct': line.strip().split()[0].lower(), 'Incorrect': line.strip().split()[1].lower()} for line in lines])
  return df


