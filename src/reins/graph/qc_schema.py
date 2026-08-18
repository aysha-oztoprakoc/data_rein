def init_qc_schema(kuzu_db):
    """Initializes the Quality Control baseline schema in KuzuDB."""
    try:
        kuzu_db.execute("CREATE NODE TABLE IF NOT EXISTS ModuleHealth (name STRING, complexity INT64, coverage DOUBLE, PRIMARY KEY (name))")
        kuzu_db.execute("CREATE NODE TABLE IF NOT EXISTS QualityReport (commit STRING, risk STRING, passed BOOLEAN, PRIMARY KEY (commit))")
        kuzu_db.execute("CREATE REL TABLE IF NOT EXISTS EVALUATED_MODULE (FROM QualityReport TO ModuleHealth)")
    except Exception as e:
        # Tables might already exist, catch safely depending on Kuzu version
        import logging
        logging.info(f"Schema init note: {e}")
