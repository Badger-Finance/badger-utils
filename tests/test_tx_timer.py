from utils.tx_timer import tx_timer
from utils.tx_timer import TxTimer
from brownie import accounts


def test_tx_timer_gets_emptied_after_run():
    tx_timer.prepare_timer(accounts[0], "Harvest")
    assert tx_timer.sender == accounts[0]
    assert tx_timer.tx_type == "Harvest"
    tx_timer.start_timer(accounts[0], 'Harvest')
    tx_timer.end_timer()

    assert tx_timer.sender is None
    assert tx_timer.waiting is False
    assert tx_timer.tx_type == ''


def test_tx_timer_webhook_is_called(mocker):
    timer = TxTimer(time_threshold=1)
    request = mocker.patch(
        "utils.tx_timer.requests.post",
    )
    timer.prepare_timer(accounts[0], "Harvest")
    timer.webhook = "https://test.webhook"
    timer.track_tx()
    assert request.called
