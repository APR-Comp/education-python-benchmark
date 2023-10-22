import os
from os.path import isfile,join,isdir
import subprocess
import pytest
import shutil
import json
from pytest_jsonreport.plugin import JSONReport

questions = sorted([x for x in os.listdir() if not isfile(x) and "question" in x])


def execute_command(command: str, show_output=True, env=dict(), directory=None):
    # Print executed command and execute it in console
    command = command.encode().decode("ascii", "ignore")
    if not directory:
        directory = os.getcwd()
        print_command = command
    else:
        print_command = "[{}] {}".format(directory, command)
    print(print_command)
    command = "{{ {} ;}} 2> {}".format(command, "oof.log")
    if not show_output:
        command += " > /dev/null"
    # print(command)
    new_env = os.environ.copy()
    new_env.update(env)
    process = subprocess.Popen(
        [command], stdout=subprocess.PIPE, shell=True, env=new_env, cwd=directory
    )
    (output, error) = process.communicate()
    # out is the output of the command, and err is the exit value
    return int(process.returncode)

file = open("meta-data.candidate.json", "w")
file.write("[")
id = 0
cwd = os.getcwd()
for question in questions:
    os.chdir(cwd)
    bugs = sorted([
        x for x in os.listdir(question) if isdir(join(question,x))
    ])
    filtered_bugs = []
    for bug in bugs:
        if int(bug) % 5 == 2 :
            filtered_bugs.append(bug)
        else:
            shutil.rmtree(join(question,bug))

    targets = filtered_bugs[-20:]
    rest = filtered_bugs[:-20]

    for bug in rest:
        shutil.rmtree(join(question,bug))

    correct_set = sorted(os.listdir(os.path.join("base", question,"correct")))
                
    filtered_correct_set = []
    for i,correct_solution in enumerate(correct_set):
        if i % 9 == 0 and len(filtered_correct_set) < 30:
            filtered_correct_set.append(correct_solution)
        else:
            os.remove(os.path.join("base",question,"correct",correct_solution))

    for bug_id in targets:
        bug_index = int(bug_id)
        id = id + 1
        name = bug_id
        inputs = ",".join(
                [f'"{question}/ans/{x}"'
                for x in os.listdir(os.path.join("base", question,"ans"))
                if "input" in x]
        )
        correct_solutions = ",".join(
                [f'"{question}/ans/{x}"' for x in filtered_correct_set]
        )

        os.chdir(join(question,bug_id))
        os.system("/home/mmirchev/.local/bin/pytest --json-report --timeout=5")
        with open(".report.json") as f:
            report = json.loads(f.read())

        passing_test_count = report["summary"].get("passed",0)
        failing_test_count = report["summary"].get("failed",0)
        passing_tests = []
        failing_tests = []
        for test in report["tests"]:
            if test["outcome"] == "passed":
                passing_tests.append(test["nodeid"])
            else:
                failing_tests.append(test["nodeid"])
        os.remove(".report.json")
        os.chdir(cwd)

        data = """
        {{
            "id":{id},
            "subject":"{lab}",
            "bug_id":"{problem_id}",
            "source_file": "wrong_{question_id}_{bug_id}.py",
            "reference_file": "{correct_file}",
            "correct_files": [{correct_solutions}],
            "extra_files": [{extra_files}],
            "line_numbers": [],
            "passing_test": [{passing_tests}],
            "failing_test": [{failing_tests}],
            "count_pos": "{passing_test_count}",
            "count_neg": "{failing_test_count}",
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
            question_id=question.split('_')[1],
            bug_id=bug_id,
            correct_solutions=correct_solutions,
            extra_files = '"global.py"' if isfile(join(question,bug_id,'global.py')) else '',
            correct_file="reference.py",
            inputs=inputs,
            passing_tests = ','.join(map ( lambda f : '"{}"'.format(f), passing_tests)),
            failing_tests = ','.join(map ( lambda f : '"{}"'.format(f),failing_tests)),
            passing_test_count = passing_test_count,
            failing_test_count = failing_test_count
        )
        file.write(data)

file.write("]")
file.close()
