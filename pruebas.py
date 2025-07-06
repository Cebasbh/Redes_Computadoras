from main import hash
test_vectors = {
    "": "d41d8cd98f00b204e9800998ecf8427e",
    "a": "0cc175b9c0f1b6a831c399e269772661",
    "ab": "187ef4436122d1cc2f40dc2b92f0eba0",
    "abc": "900150983cd24fb0d6963f7d28e17f72",
    "hello": "5d41402abc4b2a76b9719d911017c592",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "message digest": "f96b697d7cb7938d525a2f31aaf161d0",
    "md5": "1bc29b36f623ba82aaf6724fd3b16718",
    "abcdefghijklmnopqrstuvwxyz": "c3fcd3d76192e4007dfb496cca67e13b",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ": "437bba8e0bf58337674f4539e75186ac",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789": "d174ab98d277d9f5a5611c2c9f419d9f",
    "1234567890": "e807f1fcf82d132f9bb018ca6738a19f",
    "123456789012345678901234567890": "a46857f0ecc21f0a06ea434b94d9cf1d",
    "The quick brown fox jumps over the lazy dog": "9e107d9d372bb6826bd81d3542a419d6",
    "The quick brown fox jumps over the lazy dog.": "e4d909c290d0fb1ca068ffaddf22cbd0",
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": "6eb6a030bcce166534b95bc2ab45d9cf",
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": "1bb77918e5695c944be02c16ae29b25e",
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": "b6fe77c19f0f0f4946c761d62585bfea",
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": "e9e7e260dce84ffa6e0e7eb5fd9d37fc",
}

for msg, expected_hash in test_vectors.items():
    result = hash(msg) 
    if result == expected_hash:
        print(f"✅ '{msg}' → {result}")
    else:
        print(f"❌ '{msg}' → {result} (esperado: {expected_hash})")