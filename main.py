import getopt
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')

def main(argv):
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

    try:
        opts, args = getopt.getopt(
            argv, "h:u:", ["help", "in_filename=", "out_filename=", "pbkdf2_salt_str=", "aes_iv_str=", "wxid="])
    except getopt.GetoptError:
        show_help()
        exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            show_help()
            sys.exit(1)
        elif opt in ("--in_filename"):
            in_filename = arg
        elif opt in ("--out_filename"):
            out_filename = arg
        elif opt in ("--pbkdf2_salt_str"):
            pbkdf2_salt_str = arg
        elif opt in ("--aes_iv_str"):
            aes_iv_str = arg
        elif opt in ("--wxid"):
            wxid = arg
    
    if wxid == "":
        print("Missing options.")
        show_help()
        sys.exit(3)

    if not wxid.startswith("wx") or len(wxid) != 18:
        print("Warn: wxid not comply to the standard.")

    from utils.unpack import unpack_cli
    sys.exit(unpack_cli(in_filename, out_filename, pbkdf2_salt_str, aes_iv_str, wxid))
            

if __name__ == "__main__":
    main(sys.argv[1:])