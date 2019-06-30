import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    #list of files ending with given suffix
    file_list = list()
    #if the path is a directory then list directory
    if os.path.isdir(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            #if file then look for the suffix. If the name is a directory then recursively call this function with the child directory
            if os.path.isfile(fullpath):
                if str.endswith(name,suffix):
                    file_list.append(fullpath)
            elif os.path.isdir(fullpath):
                file_list.extend(find_files(suffix,fullpath))
    return file_list

def test_function1():
    test_result = ["./testdir/subdir3/subsubdir1/b.c","./testdir/t1.c","./testdir/subdir5/a.c","./testdir/subdir1/a.c","./venv/lib/python2.7/config/config.c"]
    output = find_files(".c",".")
    print(output)

def test_function2():
    test_result = ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h', './venv/include/python2.7/classobject.h', './venv/include/python2.7/cellobject.h', './venv/include/python2.7/intrcheck.h', './venv/include/python2.7/pyarena.h', './venv/include/python2.7/sliceobject.h', './venv/include/python2.7/tupleobject.h', './venv/include/python2.7/bitset.h', './venv/include/python2.7/marshal.h', './venv/include/python2.7/py_curses.h', './venv/include/python2.7/errcode.h', './venv/include/python2.7/iterobject.h', './venv/include/python2.7/asdl.h', './venv/include/python2.7/rangeobject.h', './venv/include/python2.7/pystrtod.h', './venv/include/python2.7/intobject.h', './venv/include/python2.7/warnings.h', './venv/include/python2.7/pgen.h', './venv/include/python2.7/pycapsule.h', './venv/include/python2.7/pyerrors.h', './venv/include/python2.7/parsetok.h', './venv/include/python2.7/dictobject.h', './venv/include/python2.7/ceval.h', './venv/include/python2.7/pystate.h', './venv/include/python2.7/pygetopt.h', './venv/include/python2.7/floatobject.h', './venv/include/python2.7/cStringIO.h', './venv/include/python2.7/cobject.h', './venv/include/python2.7/longintrepr.h', './venv/include/python2.7/metagrammar.h', './venv/include/python2.7/structmember.h', './venv/include/python2.7/code.h', './venv/include/python2.7/pyctype.h', './venv/include/python2.7/patchlevel.h', './venv/include/python2.7/frameobject.h', './venv/include/python2.7/abstract.h', './venv/include/python2.7/modsupport.h', './venv/include/python2.7/pymactoolbox.h', './venv/include/python2.7/datetime.h', './venv/include/python2.7/node.h', './venv/include/python2.7/methodobject.h', './venv/include/python2.7/genobject.h', './venv/include/python2.7/pymem.h', './venv/include/python2.7/boolobject.h', './venv/include/python2.7/pgenheaders.h', './venv/include/python2.7/fileobject.h', './venv/include/python2.7/pyexpat.h', './venv/include/python2.7/stringobject.h', './venv/include/python2.7/pystrcmp.h', './venv/include/python2.7/pymath.h', './venv/include/python2.7/pyconfig.h', './venv/include/python2.7/weakrefobject.h', './venv/include/python2.7/bufferobject.h', './venv/include/python2.7/pymacconfig.h', './venv/include/python2.7/pyfpe.h', './venv/include/python2.7/enumobject.h', './venv/include/python2.7/moduleobject.h', './venv/include/python2.7/symtable.h', './venv/include/python2.7/ast.h', './venv/include/python2.7/compile.h', './venv/include/python2.7/eval.h', './venv/include/python2.7/setobject.h', './venv/include/python2.7/codecs.h', './venv/include/python2.7/grammar.h', './venv/include/python2.7/complexobject.h', './venv/include/python2.7/dtoa.h', './venv/include/python2.7/object.h', './venv/include/python2.7/structseq.h', './venv/include/python2.7/bytearrayobject.h', './venv/include/python2.7/import.h', './venv/include/python2.7/token.h', './venv/include/python2.7/timefuncs.h', './venv/include/python2.7/ucnhash.h', './venv/include/python2.7/osdefs.h', './venv/include/python2.7/pythonrun.h', './venv/include/python2.7/unicodeobject.h', './venv/include/python2.7/Python-ast.h', './venv/include/python2.7/traceback.h', './venv/include/python2.7/funcobject.h', './venv/include/python2.7/pythread.h', './venv/include/python2.7/Python.h', './venv/include/python2.7/memoryobject.h', './venv/include/python2.7/opcode.h', './venv/include/python2.7/descrobject.h', './venv/include/python2.7/objimpl.h', './venv/include/python2.7/pyport.h', './venv/include/python2.7/sysmodule.h', './venv/include/python2.7/longobject.h', './venv/include/python2.7/bytesobject.h', './venv/include/python2.7/listobject.h', './venv/include/python2.7/graminit.h', './venv/include/python2.7/pydebug.h', './venv/include/python2.7/bytes_methods.h']
    output = find_files(".h",".")
    print(output)

#the directory does not exist
#output will be empty
def test_function3():
    output = find_files(".c", "./dir")
    test_result = []
    print(output)

#no match does not exist
#output will be empty
def test_function4():
    output = find_files(".ch", "./dir")
    test_result = []
    print(output)

test_function1()
#["./testdir/subdir3/subsubdir1/b.c","./testdir/t1.c","./testdir/subdir5/a.c","./testdir/subdir1/a.c","./venv/lib/python2.7/config/config.c"]
test_function2()
#['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h', './venv/include/python2.7/classobject.h', './venv/include/python2.7/cellobject.h', './venv/include/python2.7/intrcheck.h', './venv/include/python2.7/pyarena.h', './venv/include/python2.7/sliceobject.h', './venv/include/python2.7/tupleobject.h', './venv/include/python2.7/bitset.h', './venv/include/python2.7/marshal.h', './venv/include/python2.7/py_curses.h', './venv/include/python2.7/errcode.h', './venv/include/python2.7/iterobject.h', './venv/include/python2.7/asdl.h', './venv/include/python2.7/rangeobject.h', './venv/include/python2.7/pystrtod.h', './venv/include/python2.7/intobject.h', './venv/include/python2.7/warnings.h', './venv/include/python2.7/pgen.h', './venv/include/python2.7/pycapsule.h', './venv/include/python2.7/pyerrors.h', './venv/include/python2.7/parsetok.h', './venv/include/python2.7/dictobject.h', './venv/include/python2.7/ceval.h', './venv/include/python2.7/pystate.h', './venv/include/python2.7/pygetopt.h', './venv/include/python2.7/floatobject.h', './venv/include/python2.7/cStringIO.h', './venv/include/python2.7/cobject.h', './venv/include/python2.7/longintrepr.h', './venv/include/python2.7/metagrammar.h', './venv/include/python2.7/structmember.h', './venv/include/python2.7/code.h', './venv/include/python2.7/pyctype.h', './venv/include/python2.7/patchlevel.h', './venv/include/python2.7/frameobject.h', './venv/include/python2.7/abstract.h', './venv/include/python2.7/modsupport.h', './venv/include/python2.7/pymactoolbox.h', './venv/include/python2.7/datetime.h', './venv/include/python2.7/node.h', './venv/include/python2.7/methodobject.h', './venv/include/python2.7/genobject.h', './venv/include/python2.7/pymem.h', './venv/include/python2.7/boolobject.h', './venv/include/python2.7/pgenheaders.h', './venv/include/python2.7/fileobject.h', './venv/include/python2.7/pyexpat.h', './venv/include/python2.7/stringobject.h', './venv/include/python2.7/pystrcmp.h', './venv/include/python2.7/pymath.h', './venv/include/python2.7/pyconfig.h', './venv/include/python2.7/weakrefobject.h', './venv/include/python2.7/bufferobject.h', './venv/include/python2.7/pymacconfig.h', './venv/include/python2.7/pyfpe.h', './venv/include/python2.7/enumobject.h', './venv/include/python2.7/moduleobject.h', './venv/include/python2.7/symtable.h', './venv/include/python2.7/ast.h', './venv/include/python2.7/compile.h', './venv/include/python2.7/eval.h', './venv/include/python2.7/setobject.h', './venv/include/python2.7/codecs.h', './venv/include/python2.7/grammar.h', './venv/include/python2.7/complexobject.h', './venv/include/python2.7/dtoa.h', './venv/include/python2.7/object.h', './venv/include/python2.7/structseq.h', './venv/include/python2.7/bytearrayobject.h', './venv/include/python2.7/import.h', './venv/include/python2.7/token.h', './venv/include/python2.7/timefuncs.h', './venv/include/python2.7/ucnhash.h', './venv/include/python2.7/osdefs.h', './venv/include/python2.7/pythonrun.h', './venv/include/python2.7/unicodeobject.h', './venv/include/python2.7/Python-ast.h', './venv/include/python2.7/traceback.h', './venv/include/python2.7/funcobject.h', './venv/include/python2.7/pythread.h', './venv/include/python2.7/Python.h', './venv/include/python2.7/memoryobject.h', './venv/include/python2.7/opcode.h', './venv/include/python2.7/descrobject.h', './venv/include/python2.7/objimpl.h', './venv/include/python2.7/pyport.h', './venv/include/python2.7/sysmodule.h', './venv/include/python2.7/longobject.h', './venv/include/python2.7/bytesobject.h', './venv/include/python2.7/listobject.h', './venv/include/python2.7/graminit.h', './venv/include/python2.7/pydebug.h', './venv/include/python2.7/bytes_methods.h']
test_function3()
#[] empty
test_function4()
#[]