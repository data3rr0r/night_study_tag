from nfc_uid import nfc_uid
#To run, keyboard module must be installed

nfc_uid = nfc_uid.NFC_UID()

nfc_hwid = nfc_uid.read()

print(nfc_uid)