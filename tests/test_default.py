from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_packages(Package):
    present = [
        "hdparm",
        "sysbench",
        "wget"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_files(File):
    absent = [
        "/tmp/server_information"
    ]
    if absent:
        for file in absent:
            d = File(file)
            assert not d.exists
