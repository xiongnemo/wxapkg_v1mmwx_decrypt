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

```# nemo @ nemo-workstation in \wxapkg_v1mmwx_decrypt on git:master x [14:10:26]
$ python .\main.py --in_filename=samples/__APP__.wxapkg --wxid=wx<REDACTED>
2023-09-14 14:11:04,439 - utils.unpack.check_v1mmwx_header - DEBUG - Header check: Header from file: b'V1MMWX'
2023-09-14 14:11:04,439 - utils.unpack.check_v1mmwx_header - DEBUG - Header check: V1MMWX_HEADER:    b'V1MMWX'
2023-09-14 14:11:04,440 - utils.unpack.unpack_cli - DEBUG - Generated AES key: b'<REDACTED>'
2023-09-14 14:11:04,440 - utils.unpack.unpack_cli - DEBUG - Generated AES key length: 32
2023-09-14 14:11:04,442 - utils.unpack.unpack_cli - DEBUG - Because your wxid's length is larger than 2, the second to last character's ASCII will be used as xor key.
2023-09-14 14:11:04,443 - utils.unpack.unpack_cli - DEBUG - Key: 100, <class 'int'>
2023-09-14 14:11:04,443 - utils.unpack.unpack_cli - INFO - 0/<REDACTED>
2023-09-14 14:11:04,488 - utils.unpack.unpack_cli - INFO - 500000/<REDACTED>
2023-09-14 14:11:04,533 - utils.unpack.unpack_cli - INFO - 1000000/<REDACTED>
2023-09-14 14:11:04,554 - utils.unpack.unpack_cli - INFO - Size of AES decrypted header: <REDACTED>
2023-09-14 14:11:04,554 - utils.unpack.unpack_cli - INFO - Size of dexored data: <REDACTED>
2023-09-14 14:11:04,555 - utils.unpack.unpack_cli - INFO - Size of total data: <REDACTED>
2023-09-14 14:11:04,555 - utils.unpack.unpack_cli - INFO - Size of original data: <REDACTED>
```