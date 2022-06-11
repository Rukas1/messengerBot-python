def clean_string(msg):
    occ = msg.count("&#39;")
    if occ == 0:
        return msg
    while occ != 0:
        preout = "".join([c if c != "&" else "'" for c in msg])
        occ -= 1
    indessirables = ['#', '3', '9', ';']
    out = "".join([c for c in preout if c not in indessirables])
    return out

print(clean_string("xy;93#&z"))