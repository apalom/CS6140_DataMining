import hashlib

m = hashlib.sha1()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()


print(m.digest)
print(m.digest_size)

print(m.block_size)