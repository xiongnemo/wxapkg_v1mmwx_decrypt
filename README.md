# wxapkg_v1mmwx_decrypt
DECRYPT process of V1MMWX type of encryption. Python port of pc_wxapkg_decrypt (https://github.com/BlackTrace/pc_wxapkg_decrypt)

## Requirements

```
pycryptodome==3.10.1
```

## Usage

```python
in_filename = "__APP__.wxapkg"
out_filename = "__APP__.decrypted.wxapkg"
pbkdf2_salt_str = "saltiest"
aes_iv_str = "the iv: 16 bytes"
wxid = ""

def show_help():
    print(f"""{__file__}: Util for handling V1MMWX type of encryption from wxapkg.
CLI options:
    -h      : print help.
    --help

    --in_filename=<wxapkg filename in>      : default to {in_filename}
    --out_filename=<wxapkg filename out>    : default to {out_filename}
    --pbkdf2_salt_str=<salt in AES decrypt> : default to {pbkdf2_salt_str}
    --aes_iv_str=<iv in AES decrypt>        : default to {aes_iv_str}
    --wxid=<wxid of the Wechat Mini Program>: string, wx[16 bytes of hex string]""")
```

## Sample Usage

```bash
% python .\main.py --in_filename=samples/__APP__.wxapkg --wxid=wx****************
Header check: Header from file: b'V1MMWX'
Header check: V1MMWX_HEADER:    b'V1MMWX'
Generated AES key: b'%>C\xb3\xa6\x17z\x0b\x16i\xd2\x91q\x07\x80\xda\x90|c\x8e3C\x02\x15\x90\x9f\x0f\xcc\x02M{\x01'
Generated AES key length: 32
Because your wxid's length is larger than 2, the second to last character's ASCII will be used as xor key.
Key: 54, <class 'int'>
0/2537009
500000/2537009
1000000/2537009
1500000/2537009
2000000/2537009
2500000/2537009
Size of AES decrypted header: 1024
Size of dexored data: 2537009
Size of total data: 2538033
Size of original data: 2538040
```