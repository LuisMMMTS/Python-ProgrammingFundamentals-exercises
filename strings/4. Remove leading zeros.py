"""'

Write a Python function `remove_leading(ip)', ' that, given a string with an
IPv4 address `ip', ', returns a new string with all leading zeros removed from
`ip', '. An IPv4 address is an address in the format N.N.N.N, where N is an
integer in the interval [0, 255].

'

"""

def remove_leading(ip):
    n_ip=""
    for a in ip.split("."):
        n_ip+=str(int(a))+"."
        
    return n_ip[:-1]