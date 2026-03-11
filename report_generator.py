def generate_report(blur, resolution, edge_score):

    risk_score = 0
    signals = []

    # Blur detection
    if blur:
        risk_score += 30
        signals.append("Image appears blurry")

    # Resolution check
    if resolution == "Low":
        risk_score += 25
        signals.append("Low resolution image")

    # Edge artifact detection
    if edge_score > 2000000:
        risk_score += 20
        signals.append("Unusual edge artifacts detected")

    # Risk classification
    if risk_score <= 25:
        verdict = "Likely Genuine"
    elif risk_score <= 50:
        verdict = "Moderate Risk"
    else:
        verdict = "High Fraud Risk"

    return {
        "risk_score": risk_score,
        "verdict": verdict,
        "signals": signals
    }