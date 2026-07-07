from reins.harness import chunking


def test_no_context_blocks_yields_single_empty_chunk():
    chunks = chunking.plan_chunks("do the thing", [])
    assert len(chunks) == 1
    assert chunks[0].goal == "do the thing"
    assert chunks[0].context == ""


def test_small_blocks_pack_into_one_chunk():
    chunks = chunking.plan_chunks("goal", ["short a", "short b", "short c"])
    assert len(chunks) == 1
    assert "short a" in chunks[0].context
    assert "short c" in chunks[0].context


def test_oversized_total_splits_across_chunks():
    budget_chars = chunking.context_budget_tokens("qwen2.5-coder:7b") * chunking.CHARS_PER_TOKEN
    big_block = "x" * (budget_chars - 10)
    chunks = chunking.plan_chunks("goal", [big_block, big_block, big_block])
    assert len(chunks) >= 2
    for c in chunks:
        assert len(c.context) <= budget_chars


def test_single_block_bigger_than_budget_is_hard_sliced():
    budget_chars = chunking.context_budget_tokens("qwen2.5-coder:7b") * chunking.CHARS_PER_TOKEN
    huge = "y" * (budget_chars * 3)
    chunks = chunking.plan_chunks("goal", [huge])
    assert len(chunks) == 3
    assert all(len(c.context) <= budget_chars for c in chunks)


def test_context_budget_reserves_room_for_output_and_scaffold():
    budget = chunking.context_budget_tokens("qwen2.5-coder:7b")
    assert budget < chunking.MODEL_CONTEXT_LIMITS["qwen2.5-coder:7b"]
    assert budget >= chunking.MIN_BUDGET_TOKENS
