import os
from os.path import isfile, join, isdir
import itertools
import subprocess
import pytest
import shutil
import json
from pytest_jsonreport.plugin import JSONReport

file = open("meta-data.candidate.json", "w")
file.write("[")
id = 0
root = os.getcwd()

questions = sorted([x for x in os.listdir() if not isfile(x) and "question" in x and "old_" not in x])
def make_entry(
    id,
    question,
    bug_id,
    name,
    inputs,
    correct_solutions,
    passing_test_identifiers_count,
    failing_test_identifiers_count,
    passing_test_identifiers,
    failing_test_identifiers,
    file_name
):
    data = """
        {{
            "id":{id},
            "subject":"{lab}",
            "bug_id":"{problem_id}",
            "source_file": "{file_name}",
            "reference_file": "{correct_file}",
            "correct_files": [{correct_solutions}],
            "extra_files": [{extra_files}],
            "line_numbers": [],
            "failing_test_identifiers": [{failing_test_identifiers}],
            "passing_test_identifiers": [{passing_test_identifiers}],
            "count_pos": {passing_test_identifiers_count},
            "count_neg": {failing_test_identifiers_count},
            "exploit_file_list": [{inputs}],
            "test_timeout": 5,
            "bug_type": "",
            "config_script": "",
            "build_script": "",
            "test_script": "run_test",
            "language": "python",
            "test_framework": "pytest"
        }},
        """.format(
        id=id,
        lab=question,
        problem_id=name,
        question_id=question.split("_")[1],
        bug_id=bug_id,
        file_name=file_name,
        correct_solutions=correct_solutions,
        extra_files='"global.py"'
        if isfile(join(question, str(bug_id), "global.py"))
        else "",
        correct_file="reference.py",
        inputs=inputs,
        passing_test_identifiers=",".join(map(lambda f: '"{}"'.format(f), passing_test_identifiers)),
        failing_test_identifiers=",".join(map(lambda f: '"{}"'.format(f), failing_test_identifiers)),
        passing_test_identifiers_count=passing_test_identifiers_count,
        failing_test_identifiers_count=failing_test_identifiers_count,
    )

    return data


def get_test_info(question, bug_id):
    shutil.copy(os.path.join(root, 'run_test_local'),
            os.path.join(question, bug_id, 'run_test'))
    
    os.chdir(join(question, bug_id))
    #print(os.getcwd())
    #input()

    passing_test_identifiers = []
    failing_test_identifiers = []
    #print("I AM IN {}".format(os.getcwd()))
    for test in sorted(os.listdir()):
        if os.path.isdir(test) or not test.endswith(".py") or test.startswith("wrong") or test.startswith('reference') or test.startswith('global'):
            continue
        test_file = test[:-len('.py')]
            
        test_name = test_file
        
        if test_file.startswith('newtest'):
            test_name = 't' + test_file[len('newt'):]
        if test_file.startswith('private_newtest'):
            test_name = 't' + test_file[len('private_newt'):]

        qualified_test_name = "{}::{}".format(
            test, test_name)
        #print(qualified_test_name)
        res = os.system("./run_test '{}'".format(qualified_test_name))
        #input()
        # print(res)
        if res == 0:
            passing_test_identifiers.append(qualified_test_name)
        else:
            failing_test_identifiers.append(qualified_test_name)
            
    os.chdir(root)
    shutil.copy(os.path.join(root, 'run_test'),
                os.path.join(question, bug_id, 'run_test'))
    return len(passing_test_identifiers), len(failing_test_identifiers), passing_test_identifiers, failing_test_identifiers

for question in questions:
    os.chdir(root)
    bugs = sorted([x for x in os.listdir(question) if isdir(join(question, x))])
   
    correct_set = sorted(os.listdir(os.path.join("base", question, "correct")))

    filtered_correct_set = []
    mutation_set = []
    for i, correct_solution in enumerate(correct_set):
        if i % 9 == 4 and len(filtered_correct_set) < 30:
            filtered_correct_set.append(correct_solution)
        if i % 9 == 3 and len(mutation_set) < 5:
            mutation_set.append(correct_solution)
        else:
            # os.remove(os.path.join("base",question,"correct",correct_solution))
            pass

   
    for i,bug_id in enumerate(bugs):
        if i % 5 == 4: #Added as the number of generated subjects was 25 and not 20
            continue
        id = id + 1
        
        name = bug_id
        inputs = ",".join(
            [
                f'"{question}/ans/{x}"'
                for x in os.listdir(os.path.join("base", question, "ans"))
                if "input" in x
            ]
        )
        correct_solutions = ",".join(
            [f'"{question}/ans/{x}"' for x in filtered_correct_set]
        )
        (
            passing_test_identifiers_count,
            failing_test_identifiers_count,
            passing_test_identifiers,
            failing_test_identifiers,
        ) = get_test_info(question, bug_id)


        x =os.listdir(os.path.join(question, bug_id))
        prob = list(filter(lambda x: x.startswith('wrong'), x))[0]
        
        data = make_entry(
            id,
            question,
            bug_id,
            name,
            inputs,
            correct_solutions,
            passing_test_identifiers_count,
            failing_test_identifiers_count,
            passing_test_identifiers,
            failing_test_identifiers,
            prob
        )
        file.write(data)
        #input()
file.write("]")
file.close()