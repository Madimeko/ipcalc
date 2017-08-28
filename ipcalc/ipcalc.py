
def block_size(cidr, version):
    size = None
    if version == 4:
        size = 32
    if version == 6:
        size = 128
    if size is not None:
        bits = size - cidr
        ips = pow(2, bits)
    return ips

