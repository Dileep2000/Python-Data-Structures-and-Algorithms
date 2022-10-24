import subprocess

if __name__ == '__main__':
    file_output  = open('output.txt','w')
    subprocess.check_call(['python3','output.py'],stdout=file_output)