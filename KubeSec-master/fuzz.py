import os
import tempfile
import traceback
from parser import find_json_path_keys, count_initial_comment_line
from graphtaint import getValidTaints
from scanner import scanForResourceLimits, scanForSecrets



def fuzz(method, arguments, should_print_output = True, should_print_trace = False):
    
    summary = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "details": []
    }
    total_cases = len(arguments)

    for index, args in enumerate(arguments, start = 1):
        summary["total"] += 1
        try:
            result = method(*args)
            summary["passed"] += 1
            detail = {"index": index, "args": args, "status": "PASSED", "result": result}
            print(f"[{index}/{total_cases}] {method.__name__}{args!r} → PASS: {result!r}")
        except Exception as exc:
            summary["failed"] += 1
            trace = traceback.format_exc()
            detail = {"index": index, "args": args, "status": "FAILED", "exception": str(exc), "traceback": trace}
            print(f"[{index}/{total_cases}] {method.__name__}{args!r} → FAIL: {type(exc).__name__}: {exc}")
            if should_print_trace:
                print(trace)
        summary["details"].append(detail)

    if should_print_output:
        print("")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Fuzzing {method.__name__}: {summary['passed']}/{summary['total']} PASSED, {summary['failed']} FAILED")
    return summary



def make_temp_file(content: str) -> str:
    tf = tempfile.NamedTemporaryFile('w+', delete=False)
    tf.write(content)
    tf.flush()
    tf.close()
    return tf.name



if __name__ == "__main__":

    # parser.py - find_json_path_keys()
    test_data = [
        {},
        [],
        {"a": 1},
        {"a": {"b": 2}},
        {"a.b": 3},
        {"a": None},
        {"a": [ {"b": [ {"c": 9} ]} ]},
        [None, None],
        {1.23: "float-key"},
        {None: "none-key"},
        {frozenset([1,2]): "frozenset-keys"},
        b"bytes",
    ]
    arguments = [(arg,) for arg in test_data]
    fuzz_result = fuzz(find_json_path_keys, arguments, should_print_output = True)
    print(fuzz_result)
    print("\n\n\n")


    # parser.py - count_initial_comment_line()
    test_data = [
        "# line1 comment\n# line2 comment\nactual: data\n",
        "\n\n# only one comment\n\nvalue: 1\n",
        "---\n#front matter\n---\nkey: val\n",
        "\n\n\njust: value\n",
        "just: value\nmore: stuff\n",
        "",
        123,
        None,
        [],
        "nonexistent_file.yaml",
        "/path/to/directory",
    ]
    temp_paths = [make_temp_file(txt) if isinstance(txt, str) else "no_file" for txt in test_data]
    arguments = [(path,) for path in temp_paths]
    fuzz_result = fuzz(count_initial_comment_line, arguments, should_print_output = True)
    print(fuzz_result)
    print("\n\n\n")
    for path in temp_paths:
        if path != "no_file":
            os.remove(path)

    
    # graphtaint.py - getValidTaints()
    test_data = [
        [],
        [("script1", "helm.release.key")],
        [("script2", "nodot")],
        [("script3", "a.b.c.d")],
        [("s1", "one.two"), ("s2", "three")],
        [("only_one_element",)],
        [("three","elements","here")],
        [(None, "test")],
        [123],
    ]
    arguments = [(arg,) for arg in test_data]
    fuzz_result = fuzz(getValidTaints, arguments, should_print_output = True)
    print(fuzz_result)
    print("\n\n\n")


    # scanner.py - scanForResourceLimits()
    test_data = [
        "",
        None,
        "invalid: test2: yaml: :::",
        "kind: Service\nmetadata:\n  name: test3\n",
        "kind: Pod\nmetadata:\n  name: test4\n",
    ]
    temp_paths = [make_temp_file(txt) if isinstance(txt, str) else "no_file" for txt in test_data]
    arguments = [(path,) for path in temp_paths]
    fuzz_result = fuzz(scanForResourceLimits, arguments, should_print_output = True)
    print(fuzz_result)
    print("\n\n\n")
    for path in temp_paths:
        if path != "no_file":
            os.remove(path)
    

    # scanner.py - scanForResourceLimits()
    test_data = [
        {},
        {"user": "username", "pass": "secret", "apikey": "XYZ"},
        {"nested": {"password": "pass", "key_id": "1235"}, "other": "val"},
        {"level1": [{"username": "admin"}]},
        ["invalid", "input"],
        None,
        123,
        [],
        "test",
        fuzz_result,
    ]
    arguments = [(arg,) for arg in test_data]
    fuzz_result = fuzz(scanForSecrets, arguments, should_print_output = True)
    print(fuzz_result)
    print("\n")
    print("Finished fuzzing")
