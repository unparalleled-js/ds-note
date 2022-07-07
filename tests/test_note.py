def test_0(contract, owner):
    receipt = contract.test_0(sender=owner)
    logs = [log for log in receipt.decode_logs()]
    assert logs


def test_1(contract, owner):
    receipt = contract.test_1(sender=owner)
    logs = [log for log in receipt.decode_logs()]
    assert logs

def test_2(contract, owner):
    receipt = contract.test_2(sender=owner)
    logs = [log for log in receipt.decode_logs()]
    assert logs

def test_3(contract, owner):
    receipt = contract.test_3(sender=owner)
    logs = [log for log in receipt.decode_logs()]
    assert logs

def test_4(contract, owner):
    receipt = contract.test_4(sender=owner)
    logs = [log for log in receipt.decode_logs()]
    assert logs
