import importlib
import os


import importlib.util


def test_solutions():
    project_dir = os.path.dirname(__file__)
    python_dir = os.path.normpath(os.path.join(project_dir, '..\\python'))
    # for name in os.listdir(python_dir)[:3]:
    for name in ['problem{}.py'.format(n) for n in range(1, 10 + 1)]:
        module_path = '{}\\{}'.format(python_dir, name)
        spec = importlib.util.spec_from_file_location(name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, 'ANSWER') and hasattr(module, 'main'):
            print(name, module.ANSWER)
            assert module.main() == module.ANSWER
    print('OK')
    assert False
