def load_file(filepath, num_lines):
    transactions = []
    with open(f'{filepath}.dat', 'r') as f:
        for i, line in enumerate(f):
            if num_lines is not None and i >= num_lines:
                break
            items = [item for item in line.strip().split(' ') if item]
            if items:
                transactions.append(items)
    return transactions