import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))