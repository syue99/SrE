from nf8742.nf8742 import NF8742

class IMGXIN(NF8742):
    socket_address = ('192.168.1.27', 23)
    controller_axis = 1

__device__ = IMGXIN
