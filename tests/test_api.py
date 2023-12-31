# -*- coding: utf-8 -*-

from afwf_ops import api


def test():
    _ = api


if __name__ == "__main__":
    from afwf_ops.tests import run_cov_test

    run_cov_test(__file__, "afwf_ops.api", preview=False)
