
import logging
logger = logging.getLogger(__name__)

from Crypto.Cipher import AES
from hashlib import pbkdf2_hmac

V1MMWX_HEADER = b'V1MMWX'


def check_v1mmwx_header(encrypted_wxapkg_bytes: bytes) -> bool:
    header_from_file = encrypted_wxapkg_bytes[0:6]
    logger.debug(f"Header check: Header from file: {header_from_file}")
    logger.debug(f"Header check: V1MMWX_HEADER:    {V1MMWX_HEADER}")
    return (header_from_file == V1MMWX_HEADER)


def unpack_cli(in_filename: str, out_filename: str, pbkdf2_salt_str: str, aes_iv_str: str, wxid: str) -> int:
    if not wxid:
        return 100

    with open(in_filename, "rb") as wxapkg_in_file:
        wxapkg_in_binary = wxapkg_in_file.read()

    if not check_v1mmwx_header(wxapkg_in_binary):
        logger.fatal("Header check failed (not V1MMWX).")
        return 101

    aes_key = pbkdf2_hmac("sha1", wxid.encode(),
                          pbkdf2_salt_str.encode(), 1000, 32)

    logger.debug(f"Generated AES key: {aes_key}")
    logger.debug(f"Generated AES key length: {len(aes_key)}")

    cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv_str.encode())

    aes_out = cipher.decrypt(wxapkg_in_binary[6:1024 + 6])

    xored_data = wxapkg_in_binary[1024 + 6 + 1:]

    xor_key = 0x66
    if len(wxid) >= 2:
        xor_key = ord(wxid[-2])
        logger.debug(
            "Because your wxid's length is larger than 2, the second to last character's ASCII will be used as xor key.")
        logger.debug(f"Key: {xor_key}, {type(xor_key)}")

    buffer_size = len(xored_data)

    dexor_buffer = bytearray(buffer_size)

    for index in range(buffer_size):
        dexored_byte_int = xored_data[index] ^ xor_key
        dexor_buffer[index] = dexored_byte_int
        if index % 500000 == 0:
            logger.info(f"{index}/{buffer_size}")

    out = aes_out + dexor_buffer

    logger.info(f"Size of AES decrypted header: {len(aes_out)}")
    logger.info(f"Size of dexored data: {len(dexor_buffer)}")
    logger.info(f"Size of total data: {len(out)}")
    logger.info(f"Size of original data: {len(wxapkg_in_binary)}")

    with open(out_filename, "wb") as wxapkg_out_file:
        wxapkg_out_file.write(out)

    return 0
