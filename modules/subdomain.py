import subprocess

def find_subdomains(target):
    print(f"[+] Finding subdomains for {target}...")

    try:
        result = subprocess.run(
            ["subfinder", "-d", target],
            capture_output=True,
            text=True
        )

        subdomains = result.stdout.splitlines()
        return list(set(subdomains))  # remove duplicates

    except Exception as e:
        print(f"Error: {e}")
        return []
