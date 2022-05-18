# `test_cpu_and_gpu_work` needs to be executed before any of the dask tests
# because the AMD OpenCL driver won't load on Ubuntu 14.04 otherwise.
# We simply make it first here.

def pytest_collection_modifyitems(session, config, items):
    for index, item in enumerate(tuple(items)):
        if item.name == 'test_cpu_and_gpu_work':
            items.insert(0, items.pop(index))
            return
