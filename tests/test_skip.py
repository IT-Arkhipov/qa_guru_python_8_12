import pytest


class TestSkip:

    @pytest.mark.skip
    def test_fail1(self):
        assert False

    @pytest.mark.skip
    def test_skip2(self):
        assert False

    @pytest.mark.skip
    def test_fail3(self):
        assert False

    @pytest.mark.skip
    def test_fail4(self):
        assert False

    @pytest.mark.skip
    def test_fail5(self):
        assert False
