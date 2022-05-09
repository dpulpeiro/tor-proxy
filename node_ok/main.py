import datetime
from time import sleep

import docker


def clean_invalid_containers(cli):
    print(datetime.datetime.now())
    containers = cli.containers.list()
    all_ips = set()
    tor_containers = list(filter(lambda c: c.image.tags[0] == "dperson/torproxy:latest", containers))
    good = 0
    for container in tor_containers:
        try:
            res = container.exec_run("curl ifconfig.me -s --connect-timeout 1 -x localhost:8118")
            if res.exit_code != 0:
                print(f"Invalid exit code: -> killing '{container.name}'")
                container.kill()
            else:
                ip = res.output.decode("utf-8")
                if ip not in all_ips and len(ip) <= 15:
                    all_ips.add(ip)
                    good += 1
                else:
                    print(f"removing duplicate IP '{container.name}'")
                    container.kill()
        except Exception as ex:
            print(f"Exception: killing '{container.name}'")
            container.kill()
    print("Total: ", len(tor_containers))
    print("Good : ", good)
    print("----------------------------------------------------------")


if __name__ == '__main__':
    cli = docker.from_env()
    while True:
        clean_invalid_containers(cli)
        sleep(60)
