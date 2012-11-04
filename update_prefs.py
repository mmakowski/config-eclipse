'''
usage: update_prefs <file to update> <exported prefs>
'''
import sys

def read_prefs(fn):
    prefs = {}
    order = []
    with open(fn) as f:
        for l in f.readlines():
            if not l.startswith('#'):
                l = l.rstrip()
                (key, val) = l.split('=', 1)
                prefs[key] = val
                order.append(key)
    return (prefs, order)

def updated_prefs(src, overrides):
    updated = {}
    for k in src.keys():
        updated[k] = overrides[k] if overrides.has_key(k) else src[k]
    return updated

def write(prefs, keys, fn):
    with open(fn, 'w') as f:
        for k in keys:
            f.write('%s=%s\n' % (k, prefs[k]))

prefs_file = sys.argv[1]
exported_file = sys.argv[2]
(src_prefs, order) = read_prefs(prefs_file)
(new_prefs, _) = read_prefs(exported_file)
write(updated_prefs(src_prefs, new_prefs), order, prefs_file)

