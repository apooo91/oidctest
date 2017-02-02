import os
import shutil
import filecmp
import datetime
import subprocess


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def copy_if_not_same(src, dst, overwrite=False):
    try:
        os.stat(dst)
    except OSError:
        shutil.copy(src, dst)
        return True

    if filecmp.cmp(src, dst):
        return False
    else:
        if overwrite:
            shutil.copy(src, dst)
            return True

    return False


def oidc_op_setup(distroot):
    # for _dir in ['server']:
    #     _op_dir = os.path.join(distroot, 'test_tool', 'test_op', _dir)
    #     if os.path.isdir(_dir) is False:
    #         shutil.copytree(_op_dir, 'server')
    # os.chdir('server')

    for _dir in ['certs', 'keys', 'server_log', 'log', 'entities', 'jwks']:
        if os.path.isdir(_dir) is False:
            os.mkdir(_dir)

    _op_dir = os.path.join(distroot, 'test_tool', 'test_op', 'server')
    for _dir in ['flows', 'static', 'heart_mako', 'oidf_mako', 'entity_info']:
        _src = os.path.join(_op_dir, _dir)
        if os.path.isdir(_dir):
            shutil.rmtree(_dir)
        shutil.copytree(_src, _dir)

    for _fname in ['run.sh', 'heart_config_example.py',
                   'oidf_config_example.py', 'path2port.csv',
                   'config_server.py',
                   'tt_config_example.py']:
        _file = os.path.join(_op_dir, _fname)
        copy_if_not_same(_file, _fname, True)

    for _fname in ['run.sh']:
        _file = os.path.join(_op_dir, _fname)
        copy_if_not_same(_file, _fname)

    subprocess.call(
        ["make_entity_info.py", "-i", "https://example.com", "-p", "C.T.T.T",
         "-s", "-e", "-w", "diana@localhost:8040", "-t", "CTTT"])

    subprocess.call(
        ["make_entity_info.py", "-i", "https://example.com", "-p", "C.F.T.F",
         "-t", "CFTF"])

    subprocess.call(
        ["make_entity_info.py", "-i", "https://example.com", "-p", "C.F.F.F",
         "-t", "CFFF"])

    # os.chdir('..')


def oidc_rpinst_setup(distroot):
    for _dir in ['certs', 'keys', 'server_log', 'log']:
        if os.path.isdir(_dir) is False:
            os.mkdir(_dir)

    _op_dir = os.path.join(distroot, 'test_tool', 'test_rp', 'rpinst')
    for _dir in ['static', 'htdocs', 'flows']:
        _src = os.path.join(_op_dir, _dir)
        if os.path.isdir(_dir):
            shutil.rmtree(_dir)
        shutil.copytree(_src, _dir)

    for _fname in ['run.sh', 'example_conf.py', 'profiles.json',
                   'path2port.csv']:
        _file = os.path.join(_op_dir, _fname)
        copy_if_not_same(_file, _fname, True)


def oidc_cp_rplib_setup(distroot):
    for _dir in ['certs', 'keys', 'log']:
        if os.path.isdir(_dir) is False:
            os.mkdir(_dir)

    _tt_dir = os.path.join(distroot, 'test_tool', 'test_rp', 'cp_rplib', 'tool')
    for _dir in ['static', 'flows']:
        _src = os.path.join(_tt_dir, _dir)
        if os.path.isdir(_dir):
            shutil.rmtree(_dir)
        shutil.copytree(_src, _dir)

    for _fname in ['run_example.sh', 'example_conf.py', 'links.json',
                   'server.py']:
        _file = os.path.join(_tt_dir, _fname)
        copy_if_not_same(_file, _fname, True)


def oidc_rplib_setup(distroot):
    for _dir in ['certs', 'keys', 'log']:
        if os.path.isdir(_dir) is False:
            os.mkdir(_dir)

    _op_dir = os.path.join(distroot, 'test_tool', 'test_rp', 'rplib',
                           'op')

    for _dir in ['static', 'htdocs', '_static', 'flows']:
        _src = os.path.join(_op_dir, _dir)
        if os.path.isdir(_dir):
            shutil.rmtree(_dir)
        shutil.copytree(_src, _dir)

    for _fname in ['example_conf.py', 'test_rp_op.py', 'setup.py', 'run.sh',
                   'link.json']:
        _file = os.path.join(_op_dir, _fname)
        copy_if_not_same(_file, _fname, overwrite=True)
