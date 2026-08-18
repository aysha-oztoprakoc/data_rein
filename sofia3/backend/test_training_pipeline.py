import json
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

from sofia3.backend.training_pipeline import export_training_data

@patch("sofia3.backend.training_pipeline.WikiDB")
def test_export_training_data_schema(mock_wikidb, tmp_path):
    # Setup mock WikiDB
    mock_db = MagicMock()
    mock_wikidb.return_value.__enter__.return_value = mock_db
    
    # Mock active pages
    mock_db.conn.execute.return_value.fetchall.side_effect = [
        [{"title": "Test Page", "content": "Test Content", "category": "test"}], # pages
        [{"text": "Test Memory", "category": "test"}] # memories
    ]
    
    # Run the export with patched data directory
    out_dir = tmp_path / "data-workspace"
    out_file = out_dir / "training_ready.jsonl"
    
    with patch("sofia3.backend.training_pipeline.Path", return_value=out_dir):
        export_training_data()
        
    assert out_file.exists()
    
    # Validate JSONL
    records = []
    with open(out_file, "r") as f:
        for line in f:
            records.append(json.loads(line))
            
    assert len(records) == 2
    
    # Check page schema
    assert records[0]["instruction"] == "Explain the knowledge base entry for 'Test Page' (Category: test)."
    assert records[0]["context"] == ""
    assert records[0]["response"] == "Test Content"
    
    # Check memory schema
    assert records[1]["instruction"] == "Recall a memory regarding test."
    assert records[1]["context"] == ""
    assert records[1]["response"] == "Test Memory"
