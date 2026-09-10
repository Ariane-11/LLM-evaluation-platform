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

def precision(y_true, y_pred):
    """
    Calculate the precision of predictions.

    Parameters:
    y_true: True/expected labels
    y_pred: Predictions produced by our AI system

    Returns:
    The proportion of positive predictions that were correct.
    """

    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")

    if len(y_true) == 0:
        raise ValueError("y_true and y_pred cannot be empty")

    true_positive = 0
    false_positive = 0

    for true_label, predicted_label in zip(y_true, y_pred):
        if predicted_label == 1:
            if true_label == 1:
                true_positive = true_positive + 1
            else:
                false_positive = false_positive + 1

    if true_positive + false_positive == 0:
        raise ValueError("No positive predictions to calculate precision.")

    return true_positive / (true_positive + false_positive)

def recall(y_true, y_pred):
    """
    Calculate the recall of predictions.

    Parameters:
    y_true: True/expected labels
    y_pred: Predictions produced by our AI system

    Returns:
    The proportion of actual positive cases correctly identified.
    """

    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")

    if len(y_true) == 0:
        raise ValueError("y_true and y_pred cannot be empty")

    true_positive = 0
    false_negative = 0

    for true_label, predicted_label in zip(y_true, y_pred):
        if true_label == 1:
            if predicted_label == 1:
                true_positive = true_positive + 1
            else:
                false_negative = false_negative + 1

    if true_positive + false_negative == 0:
        raise ValueError("No actual positive cases to calculate recall.")

    return true_positive / (true_positive + false_negative)


