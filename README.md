# afterwill: a simple CLI application for more effective To-Do execution and habit formation

## Usage
```
$ python afterwill -h
usage:
    $ python afterwill  \
    > --task_set 'grocery shop' meditate vacuum  \
    > --task_set jog 'eat lunch' 'work on scala course' 'apply to job'

    After I grocery shop, I will meditate
    After I meditate, I will vacuum

    After I jog, I will eat lunch
    After I eat lunch, I will work on scala course
    After I work on scala course, I will apply to job

optional arguments:
  -h, --help            show this help message and exit
  --task_set task [task ...]
                        A set of "After I ___, I will ___" tasks. Can define multiple tasksets comprised of as many tasks as you want.
```

## Features to add
- [ ] allow ingest of tasks from file
    - [ ] figure out which format(s) to support
- browser as UI
    - [ ] local-to-browser intergation
      - [ ] generate temporary HTML file (see test.html + jinja2 docs)
      - [ ] open in default browser (webbrowser.open('file://{full_path_to_html}'))
    - [ ] wrap in flask app
