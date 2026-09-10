def accuracy(y_true, y_pred):  # y_true: True/expected answers | y_pred: predictions produced by our AI system
    """
    Calculate the accuracy of predictions.

    Parameters:
    y_true: True/expected answers
    y_pred: predictions produced by our AI system

    Returns:
    The proportion of correct predictions.
    """

    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")

    if len(y_true) == 0:
        raise ValueError("y_true and y_pred cannot be empty")

    correct = 0

    for true_label, predicted_label in zip(y_true, y_pred):
        if true_label == predicted_label:
            correct = correct + 1

    return correct / len(y_true)

"""
Compact form: 
correct = sum(
    true_label == predicted_label
    for true_label, predicted_label in zip(y_true, y_pred)
)
"""
