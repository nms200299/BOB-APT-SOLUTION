import sys
import subprocess
from optparse import OptionParser
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
def _command_pipeline(command:str) -> int:
    try:
        _ = subprocess.check_output(f'{command}',
            shell=True,
            stderr=subprocess.STDOUT,
        )
    except Exception as e:
        print(e)
        return -2

    return 1
if __name__ == "__main__":
    usage = "usage: %prog --file=file.pdf --no-obfuscate"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="pdf file")
    parser.add_option('--obfuscate', default=False, action='store_true')
    parser.add_option('--no-obfuscate', dest='obfuscate', action='store_false')

    (options, args) = parser.parse_args()
    
    file_name = options.filename.split('.')[0]
    print(f"[RUN] echo 'extract js > {file_name}.js' > {ROOT}/extract_cmd.txt")
    _command_pipeline(f"echo 'extract js > {file_name}.js' > {ROOT}/extract_cmd.txt")

    command = _command_pipeline(f"python2 {ROOT}/peepdf/peepdf.py -l -f -s {ROOT}/extract_cmd.txt {options.filename}")
    print(f"[RUN] python2 {ROOT}/peepdf/peepdf.py -l -f -s {ROOT}/extract_cmd.txt {options.filename} ==> return code {command}")
    
    if options.obfuscate or True:
        command = _command_pipeline(f"python2 {ROOT}/JS-Deobfuscator/deobfuscate.py {file_name}.js {file_name}.js")
        print(f"[OBFUSCATE] python2 {ROOT}/JS-Deobfuscator/deobfuscate.py {file_name}.js {file_name}.js ==> return code {command}")

    exit(0)