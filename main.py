from modules.subdomain import find_subdomains
from modules.filter import classify_subdomains
from modules.alive import check_alive
from utils.output import print_results

def main():
    target = input("Enter target domain: ")

    subs = find_subdomains(target)

    if not subs:
        print("No subdomains found.")
        return

    classified = classify_subdomains(subs)
    print_results(classified)

    # Scan all subdomains
    important_subs = [r["subdomain"] for r in classified]

    # Alive check
    alive_results = check_alive(important_subs)

    if not alive_results:
        print("\n❌ No alive targets found.\n")
        return

    # 🔍 DEBUG OUTPUT
    print("\n🔍 DEBUG OUTPUT:\n")
    for line in alive_results:
        print(line)

    print("\n🎯 Interesting Targets:\n")

    # ✅ KEEP THIS INSIDE main()
    for line in alive_results:
        if "200" in line:
            print(f"[LIVE 🔥] {line}")
        elif "403" in line:
            print(f"[FORBIDDEN 👀] {line}")
        elif "401" in line:
            print(f"[AUTH REQUIRED 🔐] {line}")
        elif "301" in line or "302" in line:
            print(f"[REDIRECT 🔁] {line}")
        else:
            print(f"[OTHER] {line}")

if __name__ == "__main__":
    main()
