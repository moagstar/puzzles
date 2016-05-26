import os, sys, fnmatch, itertools, urllib, string


PY2 = sys.version_info[0] == 2
if PY2:
    urlquote = urllib.quote
else:
    import urllib.parse
    urlquote = urllib.parse.quote


if len(sys.argv) < 2:
    raise Exception('expected commit message as parameter')


base_url = 'http://nbviewer.jupyter.org/github/moagstar/puzzles/blob/master/'


# get notebooks
root_path = os.path.dirname(os.path.abspath(__file__)) + '/'
it = [
    os.path.split(os.path.join(root, filename).replace(root_path, ''))
    for root, dirs, files in os.walk(root_path)
    for filename in fnmatch.filter(files, '*.ipynb')
    if '.ipynb_checkpoints' not in root
]
it = sorted(it, key=lambda x: x[0])
it = itertools.groupby(it, key=lambda x: x[0])


# generate links
links = []
for group, items in it:
    links += ['## ' + group]
    links += [
        '<a href="{0}{1}" target="_blank">{2}</a><br>'.format(
            base_url,
            urlquote('/'.join(item)),
            os.path.splitext(item[1])[0]
        )
        for item in items
    ]


# generate README.md
with open(os.path.join(root_path, 'README.template')) as i:
    links = '\n'.join(links)
    readme = string.Template(i.read()).substitute(links=links)
with open(os.path.join(root_path, 'README.md'), 'w') as o:
    o.write(readme)


# add, commit and push
os.system('git add .')
os.system('git commit -m "' + sys.argv[1] + '"')
os.system('git push origin master')
