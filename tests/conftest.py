import shutil
import pytest

def pytest_runtest_logreport(report):
    if report.when == 'call':
        total, used, free = shutil.disk_usage("/")
        print(f"\n[METRICS] {report.nodeid}: {used // (2**30)}GB used, {free // (2**30)}GB free, time: {report.duration:.2f}s")
