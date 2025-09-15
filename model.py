"""
Run this files to start chat with the models.
Run with type
'python model.py'
"""

import numpy as np
import hashlib

def text_to_matrix(text):
  """Convert text to ASCII value matrix (square matrix)"""
    ascii_values = [ord(char) for char in text]
    n = int(np.ceil(np.sqrt(len(ascii_values))))
    padded_values = ascii_values + [0] * (n*n - len(ascii_values))
    matrix = np.array(padded_values).reshape(n, n)
    return matrix

def math_operations(matrix):
  """Perform various mathematical operations on matrices"""
    results = {}
    flattened = matrix.flatten()

    # 1. Determinant
    try:
        det = np.linalg.det(matrix)
        results['det'] = det
    except:
        results['det'] = 0

    # 2. Trace (diagonal amount)
    trace = np.trace(matrix)
    results['trace'] = trace

    # 3. Eigenvalues (just take the real part)
    try:
        eigenvalues = np.linalg.eigvals(matrix)
        eigen_sum = np.sum(eigenvalues.real)
        results['eigen_sum'] = eigen_sum
    except:
        results['eigen_sum'] = 0

    # 4. Dot product
    dot_product = np.dot(flattened, flattened)
    results['dot'] = dot_product

    # 5. Norm vector
    norm = np.linalg.norm(flattened)
    results['norm'] = norm

    # 6. Cross product (only for matrix 3x3)
    if matrix.shape == (3, 3):
        try:
            cross = np.cross(matrix[0], matrix[1])
            results['cross'] = np.sum(cross)
        except:
            results['cross'] = 0
    else:
        results['cross'] = 0

    # 7. Cosine similarity
    if len(flattened) >= 2:
        try:
            cosine_sim = np.dot(flattened[:-1], flattened[1:]) / (np.linalg.norm(flattened[:-1]) * np.linalg.norm(flattened[1:]))
            results['cosine'] = cosine_sim
        except:
            results['cosine'] = 0
    else:
        results['cosine'] = 0

    # 8. Hashing (MD5 hash converted to integer)
    try:
        text_hash = int(hashlib.md5(str(flattened).encode()).hexdigest(), 16)
        results['hash'] = text_hash
    except:
        results['hash'] = 0

    return results

def decision(results):
  """YES/NO decisions are based on a combination of mathematical operations"""
    decision_score = 0

    # 1. Determinant of even? 
    if results['det'] % 2 == 0: 
        decision_score += 1 

    # 2. Even trace? 
    if results['trace'] % 2 == 0: 
        decision_score += 1 

    # 3. Even sum eigenvalues? 
    if results['eigen_sum'] % 2 == 0: 
        decision_score += 1 

    # 4. Dot product even?
    if results['dot'] % 2 == 0:
        decision_score += 1

    # 5. Norm > 100?
    if results['norm'] > 100:
        decision_score += 1

    # 6. Is the cross product even?
    if results['cross'] % 2 == 0:
        decision_score += 1

    # 7. Cosine similarity positive?
    if results['cosine'] > 0:
        decision_score += 1

    # 8. Even hash?
    if results['hash'] % 2 == 0:
        decision_score += 1

    # Final decision
    return "YES" if decision_score >= 5 else "NO"

def chatbot():
    print("=== CHATBOT MODEL (YES/NO) ===")
    print("Type 'exit' to Clear.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: BYE!")
            break

        # Convert text to matrix
        matrix = text_to_matrix(user_input)

        # Perform mathematical operations
        results = math_operations(matrix)

        # Decisions YES/NO
        response = decision(results)

        print(f"Chatbot: {response}\n")

        # Display the results of mathematical operations
        print("Math Operations Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
        print("---\n")

# Run the chatbot
chatbot()
