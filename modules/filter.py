def classify_subdomains(subdomains):
    classified = []

    for sub in subdomains:
        score = 0
        tag = "LOW"

        if "admin" in sub:
            score += 10
        if "api" in sub:
            score += 8
        if "dev" in sub or "test" in sub:
            score += 7
        if "staging" in sub:
            score += 6
        if "login" in sub:
            score += 5

        if score >= 10:
            tag = "HIGH"
        elif score >= 6:
            tag = "MEDIUM"

        classified.append({
            "subdomain": sub,
            "score": score,
            "tag": tag
        })

    return sorted(classified, key=lambda x: x["score"], reverse=True)
