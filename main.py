from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import os


def main():
    VC_HOST = os.environ.get("VC_HOST")
    if not VC_HOST:
        return
    VC_USER = os.environ.get("VC_USER")
    if not VC_USER:
        return
    VC_PASS = os.environ.get("VC_PASS","")
    try:
        VC_PORT = int(os.environ.get("VC_PORT", "443"))
    except ValueError:
        exit(1)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    si = SmartConnect(
        host=VC_HOST,
        user=VC_USER,
        pwd=VC_PASS,
        port=VC_PORT,
        sslContext=ctx,
    )
    content = si.RetrieveContent()
    print("Connected to vCenter, API type:", content.about.apiType)
