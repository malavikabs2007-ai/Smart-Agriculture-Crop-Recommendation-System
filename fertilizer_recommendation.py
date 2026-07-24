def fertilizer_advice(N, P, K):
    
    if N < 50:
        return "Nitrogen level is low. Use nitrogen-rich fertilizer."

    elif P < 40:
        return "Phosphorus level is low. Use phosphate fertilizer."

    elif K < 40:
        return "Potassium level is low. Use potassium fertilizer."

    else:
        return "Soil nutrients are balanced. Use organic fertilizer for healthy crop growth."