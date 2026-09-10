from evaluation.metrics import accuracy, precision, recall


def test_accuracy():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 1, 0, 0]

    result = accuracy(y_true, y_pred)

    assert result == 0.8


def test_precision():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 1, 0, 1]

    result = precision(y_true, y_pred)

    assert result == 0.75

def test_recall():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 0, 0, 1]

    result = recall(y_true, y_pred)

    assert result == 2 / 3