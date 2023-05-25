import physfs

assert physfs.__version__ == '0.0.1'

physfs.init()
assert physfs.ls("/") == []

physfs.mount("./example.zip")
assert physfs.ls("/") == ["example"]
assert physfs.cat("example/flag") == b"OqP$IwK7eiZyTWk4Xi3jYECi^IXLdZw1u@H5wOo4\n"

physfs.unmount("./example.zip")
assert physfs.ls("/") == []

physfs.deinit()

E = None
try:
    physfs.ls()
except RuntimeError as e:
    E = e
assert E is not None
