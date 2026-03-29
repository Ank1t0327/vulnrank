import subprocess

def check_alive(subdomains):
    print("\n[+] Checking alive domains...\n")

    try:
        process = subprocess.Popen(
            ["httpx", "-silent", "-status-code", "-title", "-follow-redirects"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )

        input_data = "\n".join(subdomains)
        output, _ = process.communicate(input_data)

        return output.splitlines()

    except Exception as e:
        print(f"Error: {e}")
        return []
