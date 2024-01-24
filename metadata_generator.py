import os
from os.path import isfile, join, isdir
import itertools
import subprocess
import pytest
import shutil
import json
from pytest_jsonreport.plugin import JSONReport

questions = sorted([x for x in os.listdir() if not isfile(x) and "question" in x and "old_" not in x])


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
    #print(output)
    #print(error)
    # out is the output of the command, and err is the exit value
    return int(process.returncode)


file = open("meta-data.candidate.json", "w")
file.write("[")
id = 0
cwd = os.getcwd()


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
):
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
            "failing_test_identifiers": [{passing_test_identifiers}],
            "passing_test_identifiers": [{failing_test_identifiers}],
            "count_neg": "{passing_test_identifiers_count}",
            "count_pos": "{failing_test_identifiers_count}",
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
    os.chdir(join(question, bug_id))

    os.system("/home/mmirchev/.local/bin/pytest --json-report --timeout=5")
    with open(".report.json") as f:
        report = json.loads(f.read())
    passing_test_identifiers_count = report["summary"].get("passed",0)
    failing_test_identifiers_count = report["summary"].get("failed",0)
    passing_test_identifiers = []
    failing_test_identifiers = []
    for test in report["tests"]:
       if test["outcome"] == "passed":
           passing_test_identifiers.append(test["nodeid"])
       else:
           failing_test_identifiers.append(test["nodeid"])
    os.remove(".report.json")
    os.chdir(cwd)
    return passing_test_identifiers_count, failing_test_identifiers_count, passing_test_identifiers, failing_test_identifiers

def identity_op(question, bug_id):
    q_num = question.split("_")[1]
    execute_command(
        f"cp {question}/{bug_id}/wrong_{q_num}_{bug_id}.py outputs/wrong_{q_num}_{bug_id}.py", True
    )


def syntactic_mutation(question, bug_id):
    q_num = question.split("_")[1]
    execute_command(
        f"bash -c 'java -jar transformer.java {question}/{bug_id}/wrong_{q_num}_{bug_id}.py syntax > outputs/wrong_{q_num}_{bug_id}.py'", True
    )


def semantic_mutation(question, bug_id):
    q_num = question.split("_")[1]
    execute_command(
        f"java -jar transformer.java {question}/{bug_id}/wrong_{q_num}_{bug_id}.py semantics > outputs/wrong_{q_num}_{bug_id}.py", True
    )


def semantic_mutation_correct(question, file):
    pass
    execute_command(f'java -jar transformer.java base/{question}/correct/{file} semantics > outputs/wrong_{file}',True)


for question in questions:
    os.chdir(cwd)
    bugs = sorted([x for x in os.listdir(question) if isdir(join(question, x))])
    filtered_bugs = []
    for bug in bugs:
        if int(bug) % 5 == 4:
            filtered_bugs.append(bug)
        else:
            # shutil.rmtree(join(question,bug))
            pass

    targets = filtered_bugs[-15:]
    rest = filtered_bugs[:-20]

    # for bug in rest:
    #    shutil.rmtree(join(question,bug))

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

    original, syntax, semantic = targets[:5], targets[5:10], targets[10:]
    print(mutation_set,original, "-", syntax, "-", semantic)
    # (lambda x,y: None)
    for modification, bug_list in zip(
        [
            lambda x,y: None,
            lambda x,y: None,
            lambda x,y: None,
            lambda x,y: None,
            # semantic_mutation_correct,
            # identity_op,
            # syntactic_mutation,
            # semantic_mutation,
        ],
        [mutation_set, original, syntax, semantic],
    ):
        for bug_id in bug_list:
            modification(question, bug_id)
            
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
            )
            file.write(data)
            #input()

file.write("]")
file.close()
