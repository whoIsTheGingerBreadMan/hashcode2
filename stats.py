def library_score(lb,bs,i):
    return sum(bs[i] for i in lb[i])

def libraries_score(lb, bs):
    LBS = []
    for lib in lb:
        LBS.append(library_score(lb,bs,lib))
    return LBS