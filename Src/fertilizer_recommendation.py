def fertilizer_advice(N, P, K):
    
    if N < 50:
        return "Nitrogen level is low. Use Nitrogen-rich fertilizer."

    elif P < 40:
        return "Phosphorus level is low. Use Phosphate fertilizer."

    elif K < 40:
        return "Potassium level is low. Use Potassium fertilizer."

    else:
        return "Soil nutrients are balanced. Use organic fertilizer for better growth."