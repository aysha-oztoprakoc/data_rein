def test_rlm_importable():
    # TDD law: Each harness core module must be referenced by at least one test file.
    import reins.harness.rlm
    assert reins.harness.rlm is not None
