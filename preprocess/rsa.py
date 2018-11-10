import Crypto.PublicKey.RSA
import Crypto.Random

# init
rng = Crypto.Random.new().read
rsa = Crypto.PublicKey.RSA.generate(1024, rng)

# 公開鍵を取得する
pub_rsa  = rsa.publickey()
priv_rsa = Crypto.PublicKey.RSA.construct((rsa.n, rsa.e, rsa.d))

# encryption and decreption
enc = pub_rsa.encrypt("hello", "solt")
dec = priv_rsa.decrypt(enc)