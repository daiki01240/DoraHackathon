import os, glob
import ipfsapi
import Crypto.PublicKey.RSA
import Crypto.Random
from image_cropper import image_cropper

# init
api = ipfsapi.connect('127.0.0.1', 5001)

# crop image
input   = '/Users/Yoshiharu/Desktop/dora/images/e_calte0001.png'
path    = os.path.dirname(input)
nCrop   = 3
imgPath = image_cropper(input, path, nCrop)

# save cropped images to ipfs
imgList     = glob.glob(imgPath + "/*.png")
ipfsRoots   = [] # for output
for i in range(0,len(imgList)):
    r  = api.add(imgList[i])
    ipfsRoots.extend([r['Hash']])
# write ipfsRoots to text file
with open("ipfsRoots_orig.txt", 'wt') as f:
    for ele in ipfsRoots:
        f.write(ele+'\n')

# init
rng = Crypto.Random.new().read
# generate and savekeys
private_key = Crypto.PublicKey.RSA.generate(1024, rng)
public_key  = private_key.publickey()
priv_rsa    = Crypto.PublicKey.RSA.construct((private_key.n, private_key.e, private_key.d))
with open('private.pem', 'w') as f:
    f.write(private_key.exportKey(format='PEM'))
with open('public.pem', 'w') as f:
    f.write(public_key.exportKey(format='PEM'))
# encryption
enc_ipfsRoots   = []
salt            = "ZqsF578UbTirCp79ii6CKQEGYj4s"
for i in range(0,len(ipfsRoots)):
    enc = public_key.encrypt(str(ipfsRoots[i]), salt)
    enc_ipfsRoots.extend([enc])
# write encrypted ipfsRoots to text file
with open("ipfsRoots_enc.txt", 'wt') as f:
    for i in range(0,len(enc_ipfsRoots)):
        s = ''.join(enc_ipfsRoots[0])
        f.write(s+'\n')
