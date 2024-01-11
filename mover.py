import os
from os.path import isfile, join, isdir
import itertools
import subprocess
import pytest
import shutil
import json
from pytest_jsonreport.plugin import JSONReport

for file in os.listdir('outputs'):
    if "correct" in file:
        *prefix, question,bug_id_file = file.split('_')
        print("broke {}".format(file))
    else:
        prefix, question,bug_id_file = file.split('_')
        print("broken {}".format(file))
    bug_id = bug_id_file[:-3]
    extra = ''.join(map(lambda x:x[0],prefix)) 
    os.system(f"cp -r old_question_{question}/002 question_{question}/{extra}{bug_id}")
    os.system("bash -c 'rm question_{}/{}{}/wrong*.py'".format(question,extra,bug_id))
    os.system("bash -c 'rm question_{}/{}{}/test*.py'".format(question,extra,bug_id))
    os.system(f"cp outputs/{file} question_{question}/{extra}{bug_id}/")