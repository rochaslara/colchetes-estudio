import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
U = os.path.join(ROOT, 'src') + '/'
# Inside the platform each tool runs in its own frame. This shim lets a tool reach Claude's save
# feature through the top page (when the platform is opened as a Claude artifact) and marks the
# frame with .in-suite so each tool can hide the title the tab bar already shows.
SHIM = '<script>(function(){try{var P=window.parent;if(P!==window&&!("claude" in window)){Object.defineProperty(window,"claude",{configurable:true,get:function(){try{var C=P.claude;if(!C||!C.use)return undefined;return{use:function(n){return Promise.resolve(C.use(n)).then(function(ns){if(n!=="downloads"||!ns||!P.__atelieSave)return ns;return{save:function(o){var d=o&&o.data;return Promise.resolve(d&&d.arrayBuffer?d.arrayBuffer():d).then(function(buf){return P.__atelieSave(o.filename,buf,(d&&d.type)||"")})}}})}}}catch(e){return undefined}}});}document.documentElement.classList.add("in-suite");}catch(e){}})();</script>'
APPS = [
    ('colchetes', 'colchetes.html', '<style>.in-suite header.page{display:none}.in-suite body{padding-block-start:20px}</style>'),
    ('graficos', 'graficos.html', ''),
]
os.makedirs(os.path.join(ROOT, 'build'), exist_ok=True)
out = {}
for key, f, css in APPS:
    s = open(U + f, encoding='utf-8').read()
    shim = SHIM + css
    if '<head>' in s:
        s = s.replace('<head>', '<head>' + shim, 1)
    else:
        s = ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
             '<style>[hidden]{display:none!important}body{margin:0}</style>' + shim + '</head><body>' + s + '</body></html>')
    out[key] = s
data = json.dumps(out).replace('<', '\\u003c')
shell = open(U + 'shell.html', encoding='utf-8').read().replace('/*APPS*/{}', data)
open(os.path.join(ROOT, 'build', 'artifact.html'), 'w', encoding='utf-8').write(shell)
head = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<style>[hidden]{display:none!important}body{margin:0}</style>\n</head>\n<body>\n')
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(head + shell + '\n</body>\n</html>\n')
print('index.html', len(head + shell), 'bytes')
