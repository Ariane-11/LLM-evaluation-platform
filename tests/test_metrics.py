from evaluation.metrics import accuracy

def test_accuracy():
    y_true = [1,0,1,1,0]
    y_pred = [1,0,1,0,0]

    result = accuracy(y_true, y_pred)

    assert result == 0.8
    