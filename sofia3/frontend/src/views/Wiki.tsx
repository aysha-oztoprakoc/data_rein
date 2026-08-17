import { useCallback, useEffect, useMemo, useState } from "react";

interface PageSummary {
  slug: string;
  title: string;
  category: string;
  owner: string;
  updated_at?: string;
}
interface PageDetail {
  slug: string;
  title: string;
  content: string;
  category: string;
  owner: string;
  source_path?: string;
  metadata_json?: string;
  updated_at?: string;
}
interface MemoryItem {
  uid: string;
  text: string;
  category: string;
  owner: string;
  source?: string;
  session_id?: string;
  timestamp?: string;
}
interface WikiStats {
  stats: { pages: number; memories: number };
  categories: string[];
}

type Tab = "browse" | "memories";

function formatTime(ts: string | undefined): string {
  if (!ts) return "—";
  try {
    return new Date(ts).toLocaleString([], { hour12: false });
  } catch {
    return ts;
  }
}

export function WikiView() {
  const [stats, setStats] = useState<WikiStats | null>(null);
  const [tab, setTab] = useState<Tab>("browse");
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState<{ pages: PageSummary[]; memories: MemoryItem[] } | null>(null);
  const [pages, setPages] = useState<PageSummary[]>([]);
  const [pageTotal, setPageTotal] = useState(0);
  const [memories, setMemories] = useState<MemoryItem[]>([]);
  const [memTotal, setMemTotal] = useState(0);
  const [offset, setOffset] = useState(0);
  const [category, setCategory] = useState("all");
  const [memCategory, setMemCategory] = useState("all");
  const [selectedPage, setSelectedPage] = useState<PageDetail | null>(null);
  const [loading, setLoading] = useState(false);
  const LIMIT = 30;

  // Load stats once
  useEffect(() => {
    fetch("/api/wiki/stats")
      .then((r) => r.json())
      .then((d) => { setStats(d); if (d.categories?.length) setCategory(d.categories[0]); })
      .catch(() => {});
  }, []);

  // Load pages
  const loadPages = useCallback(
    (cat: string, off: number) => {
      setLoading(true);
      const params = new URLSearchParams({ limit: String(LIMIT), offset: String(off) });
      if (cat && cat !== "all") params.set("category", cat);
      fetch(`/api/wiki/pages?${params}`)
        .then((r) => r.json())
        .then((d) => {
          setPages(d.pages ?? []);
          setPageTotal(d.total ?? 0);
          setOffset(off);
        })
        .catch(() => {})
        .finally(() => setLoading(false));
    },
    [],
  );

  useEffect(() => {
    if (tab === "browse") loadPages(category, 0);
  }, [tab, category, loadPages]);

  // Load memories
  const loadMemories = useCallback(
    (cat: string, off: number) => {
      setLoading(true);
      const params = new URLSearchParams({ limit: String(LIMIT), offset: String(off) });
      if (cat && cat !== "all") params.set("category", cat);
      fetch(`/api/wiki/memories?${params}`)
        .then((r) => r.json())
        .then((d) => {
          setMemories(d.memories ?? []);
          setMemTotal(d.total ?? 0);
        })
        .catch(() => {})
        .finally(() => setLoading(false));
    },
    [],
  );

  useEffect(() => {
    if (tab === "memories") loadMemories(memCategory, 0);
  }, [tab, memCategory, loadMemories]);

  // Search
  useEffect(() => {
    if (!search) { setSearchResults(null); return; }
    const t = setTimeout(() => {
      fetch(`/api/wiki/search?q=${encodeURIComponent(search)}&limit=12`)
        .then((r) => r.json())
        .then((d) => setSearchResults(d))
        .catch(() => {});
    }, 300);
    return () => clearTimeout(t);
  }, [search]);

  // Select page
  const openPage = useCallback((slug: string) => {
    setSelectedPage(null);
    fetch(`/api/wiki/page/${encodeURIComponent(slug)}`)
      .then((r) => r.json())
      .then((d) => setSelectedPage(d.page))
      .catch(() => {});
  }, []);

  const categories = useMemo(() => {
    if (searchResults) {
      const set = new Set(searchResults.pages.map((p) => p.category));
      return Array.from(set).sort();
    }
    return stats?.categories ?? [];
  }, [stats, searchResults]);

  const pageCount = pageTotal;
  const totalPages = Math.ceil(pageCount / LIMIT);

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
      {/* Stats + nav tabs */}
      <div className="grid two">
        <div className="panel">
          <div className="panel-title">WIKI // KNOWLEDGE BASE</div>
          {stats ? (
            <div style={{ display: "flex", gap: 24, flexWrap: "wrap" }}>
              <span style={{ color: "var(--red-primary)", fontWeight: 700, fontSize: 22 }}>
                {stats.stats.pages}
              </span>
              <span style={{ color: "var(--text-dim)", fontSize: 12, lineHeight: "22px" }}>pages</span>
              <span style={{ color: "var(--red-primary)", fontWeight: 700, fontSize: 22 }}>
                {stats.stats.memories}
              </span>
              <span style={{ color: "var(--text-dim)", fontSize: 12, lineHeight: "22px" }}>memories</span>
              <span style={{ color: "var(--red-accent)", fontWeight: 700, fontSize: 22 }}>
                {stats.categories.length}
              </span>
              <span style={{ color: "var(--text-dim)", fontSize: 12, lineHeight: "22px" }}>categories</span>
            </div>
          ) : (
            <div className="empty">WIKI OFFLINE</div>
          )}
        </div>
        <div className="panel">
          <div className="panel-title">SEARCH</div>
          <input
            type="text"
            placeholder="search wiki…"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{
              width: "100%",
              background: "rgba(9,3,0,0.6)",
              border: "1px solid var(--border)",
              borderRadius: "var(--radius)",
              padding: "8px 12px",
              color: "var(--text)",
              fontFamily: "var(--font-mono)",
              fontSize: 13,
            }}
          />
          {searchResults && (
            <div style={{ marginTop: 8, fontSize: 12, color: "var(--text-dim)" }}>
              {searchResults.pages.length} pages · {searchResults.memories.length} memories
            </div>
          )}
        </div>
      </div>

      {/* Search results */}
      {searchResults && searchResults.pages.length > 0 && (
        <div className="panel">
          <div className="panel-title">SEARCH RESULTS — PAGES</div>
          <div className="task-list">
            {searchResults.pages.slice(0, 8).map((p) => (
              <div
                key={p.slug}
                className="task-row"
                style={{ cursor: "pointer", gridTemplateColumns: "2fr 1fr 1fr" }}
                onClick={() => openPage(p.slug)}
              >
                <span className="task-id">{p.title}</span>
                <span className="task-meta">{p.category}</span>
                <span className="task-meta">{p.owner}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Tabs */}
      <div className="nav-tabs" style={{ padding: 0 }}>
        {(["browse", "memories"] as Tab[]).map((t) => (
          <button
            key={t}
            className={`nav-tab${tab === t ? " active" : ""}`}
            onClick={() => setTab(t)}
          >
            {t === "browse" ? "PAGES" : "MEMORIES"}
          </button>
        ))}
      </div>

      {/* Category filter */}
      {categories.length > 0 && (
        <div style={{ display: "flex", gap: 4, flexWrap: "wrap" }}>
          <button
            className={`nav-tab${tab === "browse" ? (category === "all" ? " active" : "") : memCategory === "all" ? " active" : ""}`}
            onClick={() => {
              if (tab === "browse") setCategory("all");
              else setMemCategory("all");
            }}
          >
            all
          </button>
          {categories.slice(0, 20).map((c) => (
            <button
              key={c}
              className={`nav-tab${tab === "browse" ? (category === c ? " active" : "") : memCategory === c ? " active" : ""}`}
              onClick={() => {
                if (tab === "browse") setCategory(c);
                else setMemCategory(c);
              }}
            >
              {c}
            </button>
          ))}
        </div>
      )}

      {/* Page list (browse) */}
      {tab === "browse" && !selectedPage && (
        <div className="panel">
          <div className="panel-title">PAGES — {pageCount} TOTAL</div>
          {loading ? (
            <div className="empty">LOADING…</div>
          ) : (
            <div className="task-list">
              {pages.map((p) => (
                <div
                  key={p.slug}
                  className="task-row"
                  style={{ cursor: "pointer", gridTemplateColumns: "2fr 1fr 1fr 1fr" }}
                  onClick={() => openPage(p.slug)}
                >
                  <span className="task-id">{p.title}</span>
                  <span className="task-meta">{p.category}</span>
                  <span className="task-node">{p.owner}</span>
                  <span className="task-meta">{formatTime(p.updated_at)}</span>
                </div>
              ))}
              {pages.length === 0 && <div className="empty">NO PAGES</div>}
            </div>
          )}
          {totalPages > 1 && (
            <div style={{ display: "flex", gap: 6, marginTop: 10, justifyContent: "center" }}>
              {Array.from({ length: Math.min(totalPages, 10) }, (_, i) => (
                <button
                  key={i}
                  className={`nav-tab${offset / LIMIT === i ? " active" : ""}`}
                  onClick={() => loadPages(category, i * LIMIT)}
                >
                  {i + 1}
                </button>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Memories tab */}
      {tab === "memories" && (
        <div className="panel">
          <div className="panel-title">MEMORIES — {memTotal} TOTAL</div>
          {loading ? (
            <div className="empty">LOADING…</div>
          ) : (
            <div className="task-list">
              {memories.map((m) => (
                <div key={m.uid} className="task-row" style={{ gridTemplateColumns: "2fr 1fr 1fr" }}>
                  <span className="task-id" title={m.text}>{m.text.slice(0, 120)}</span>
                  <span className="task-meta">{m.category}</span>
                  <span className="task-node">{m.owner}</span>
                </div>
              ))}
              {memories.length === 0 && <div className="empty">NO MEMORIES</div>}
            </div>
          )}
        </div>
      )}

      {/* Page detail */}
      {selectedPage && (
        <div className="panel">
          <div className="panel-title" style={{ justifyContent: "space-between" }}>
            <span>PAGE — {selectedPage.title}</span>
            <button
              className="nav-tab"
              onClick={() => setSelectedPage(null)}
              style={{ borderColor: "var(--red-strong)" }}
            >
              ← BACK
            </button>
          </div>
          <div style={{ fontSize: 11, color: "var(--text-dim)", marginBottom: 12, display: "flex", gap: 16 }}>
            <span>slug: {selectedPage.slug}</span>
            <span>category: {selectedPage.category}</span>
            <span>owner: {selectedPage.owner}</span>
          </div>
          <div
            style={{
              background: "rgba(9,3,0,0.5)",
              border: "1px solid var(--border)",
              borderRadius: "var(--radius)",
              padding: 16,
              fontSize: 13,
              lineHeight: 1.7,
              whiteSpace: "pre-wrap",
              wordBreak: "break-word",
              maxHeight: "65vh",
              overflowY: "auto",
              color: "var(--text)",
            }}
          >
            {selectedPage.content}
          </div>
        </div>
      )}
    </div>
  );
}