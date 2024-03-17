import ffmpeg
import os

def get_mp3_files(directory):
    files = os.listdir(directory)
    return sorted([file for file in files if file.endswith('.mp3')])
  
def concat_mp3s(mp3s, output):
    input_args = []
    for mp3 in mp3s:
        full_path = os.path.join(directory, mp3)
        print(f"Adding file: {full_path}")
        input_args.append(ffmpeg.input(full_path))
    ffmpeg.concat(*input_args, v=0, a=1).output(output).run()
    
directory = './harry_potter_book1/'
mp3_files = get_mp3_files(directory)

concat_mp3s(mp3_files, 'book1.mp3')
