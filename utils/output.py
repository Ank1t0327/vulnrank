def print_results(results):
    print("\n🔥 Vulnrank Results:\n")

    for r in results:
        print(f"[{r['tag']}] {r['subdomain']} (Score: {r['score']})")
