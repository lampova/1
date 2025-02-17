import subprocess
import re

from ipwhois import IPWhois


def trace_ip(ip):
    tracert_output = subprocess.run(['tracert', ip], capture_output=True, text=True)
    hops = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', tracert_output.stdout)

    for hop in hops:
        print(f"\nIP Address: {hop}")
        try:
            obj = IPWhois(hop)
            results = obj.lookup_rdap()
            info = results['asn']
            descript = results['asn_description']
            print(f"AS number: {info}")
            print(f"AS description: {descript}")
        except Exception as ex:
            print(f"Error retrieving AS information for {hop}: {ex}")


if __name__ == "__main__":
    ip = input("IP адрес или домен: ")
    trace_ip(ip)
