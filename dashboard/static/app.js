// =============================================================================
// SOFIA // UNIFIED KNOWLEDGE VAULT & DASHBOARD CONTROLLER
// =============================================================================

let ws = null;
let currentTasks = [];
let currentPages = [];
let currentMemories = [];
let currentSkills = [];

let activeVaultCategory = 'all';
let activeVaultDomain = 'all'; // 'all' | 'pages' | 'memories'
let activeFeedMode = 'all'; // 'all' | 'pages' | 'memories'

let selectedVaultItem = null; // { type: 'page'|'memory', data: object }
let activeTaskStatusFilter = 'all';

document.addEventListener('DOMContentLoaded', () => {
    initDynamicCyberBackground();
    initNavigation();
    initWebSocket();
    initTaskTrailFilters();
    initModals();
    initUnifiedVault();
    initSkills();
    initModels();
    initTestbed();
    initControls();
});

// -----------------------------------------------------------------------------
// Navigation & Tab Switching
// -----------------------------------------------------------------------------
function initNavigation() {
    const tabs = document.querySelectorAll('.tab-btn');
    const sections = document.querySelectorAll('.view-section');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));

            tab.classList.add('active');
            const target = tab.getAttribute('data-target');
            const targetSection = document.getElementById(target);
            if (targetSection) {
                targetSection.classList.add('active');
            }

            if (target === 'wiki') loadUnifiedVault();
            if (target === 'skills') loadSkillsCatalog();
            if (target === 'models') loadModelsCatalog();
        });
    });
}

// -----------------------------------------------------------------------------
// WebSocket Real-time Telemetry
// -----------------------------------------------------------------------------
function initWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const wsUrl = `${protocol}//${window.location.host}/ws`;
    const indicator = document.getElementById('ws-indicator');
    const statusText = document.getElementById('ws-status');

    try {
        ws = new WebSocket(wsUrl);

        ws.onopen = () => {
            indicator.className = 'ws-badge connected';
            statusText.textContent = 'PON TELEMETRY: ACTIVE';
        };

        ws.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                handleTelemetryUpdate(data);
            } catch (err) {
                console.error('Error parsing WS frame:', err);
            }
        };

        ws.onclose = () => {
            indicator.className = 'ws-badge disconnected';
            statusText.textContent = 'OFFLINE (RECONNECTING...)';
            setTimeout(initWebSocket, 2500);
        };

        ws.onerror = () => {
            ws.close();
        };
    } catch (e) {
        console.error('WebSocket connection failed:', e);
    }
}

function handleTelemetryUpdate(data) {
    if (!data || !data.system) return;

    const sys = data.system;
    document.getElementById('val-cpu').textContent = `${Math.round(sys.cpu_percent || 0)}%`;
    document.getElementById('bar-cpu').style.width = `${Math.min(100, sys.cpu_percent || 0)}%`;

    document.getElementById('val-ram').textContent = `${sys.memory_used_gb || 0} / ${sys.memory_total_gb || 0} GB`;
    document.getElementById('val-ram-pct').textContent = `${sys.memory_percent || 0}% allocated`;
    document.getElementById('bar-ram').style.width = `${Math.min(100, sys.memory_percent || 0)}%`;

    if (data.tasks) {
        document.getElementById('val-tasks-success').textContent = `${data.tasks.success || 0} OK`;
        document.getElementById('val-tasks-running').textContent = `${data.tasks.running || 0} RUN`;
        document.getElementById('val-tasks-failed').textContent = `${data.tasks.failed || 0} ERR`;
        document.getElementById('val-tasks-total').textContent = `Total: ${data.tasks.total || 0} recorded in SQLite`;
        document.getElementById('trail-count-badge').textContent = data.tasks.total || 0;
        document.getElementById('tab-count-monitor').textContent = data.tasks.total || 0;
    }

    if (data.wiki) {
        const totalItems = (data.wiki.pages || 0) + (data.wiki.memories || 0);
        document.getElementById('val-wiki-total-items').textContent = `${totalItems} items`;
        document.getElementById('val-wiki-breakdown').textContent = `${data.wiki.pages || 0} pages • ${data.wiki.memories || 0} memories`;
        document.getElementById('tab-count-vault').textContent = totalItems;
    }

    if (data.recent_tasks) {
        currentTasks = data.recent_tasks;
        renderTaskTrailTable();
    }

    // Dynamic background heartbeat on reactive PON telemetry
    pulseBackgroundNetwork();
}

// -----------------------------------------------------------------------------
// Task Trail Monitor
// -----------------------------------------------------------------------------
function renderTaskTrailTable() {
    const tbody = document.getElementById('trail-table-body');
    const filterText = (document.getElementById('task-filter-input').value || '').toLowerCase();

    let filtered = currentTasks.filter(task => {
        const matchesStatus = activeTaskStatusFilter === 'all' || 
            (task.status && task.status.toLowerCase() === activeTaskStatusFilter);
        
        const taskString = JSON.stringify(task).toLowerCase();
        const matchesText = !filterText || taskString.includes(filterText);
        return matchesStatus && matchesText;
    });

    if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="empty-state">[NO MATCHING TASKS RECORDED]</td></tr>`;
        return;
    }

    tbody.innerHTML = filtered.map(task => {
        const idShort = (task.task_id || '').substring(0, 10) + '...';
        const st = (task.status || 'pending').toLowerCase();
        let pillClass = 'pill-running';
        if (st === 'success') pillClass = 'pill-success';
        if (st === 'failed') pillClass = 'pill-failed';

        let promptPreview = task.prompt || task.task_type || '-';
        if (typeof promptPreview === 'object') promptPreview = JSON.stringify(promptPreview);
        if (promptPreview.length > 55) promptPreview = promptPreview.substring(0, 55) + '...';

        const timestampStr = task.timestamp ? new Date(task.timestamp * 1000).toLocaleTimeString() : '--:--:--';

        return `
            <tr>
                <td><span style="font-family:'Fira Code', monospace; color:var(--primary-red); font-weight:bold;">${idShort}</span></td>
                <td>${task.task_type || '-'}</td>
                <td><span class="tag-badge">${task.target_node || 'amdy'}</span></td>
                <td><span class="stat-pill ${pillClass}">${st.toUpperCase()}</span></td>
                <td style="color:var(--text-muted); font-size:0.82rem;">${escapeHtml(promptPreview)}</td>
                <td style="font-size:0.8rem; color:var(--dim-gray);">${timestampStr}</td>
                <td>
                    <button class="cyber-btn btn-secondary" style="padding:4px 12px; font-size:0.75rem;" onclick="inspectTask('${escapeHtml(task.task_id)}')">INSPECT</button>
                </td>
            </tr>
        `;
    }).join('');
}

function initTaskTrailFilters() {
    const taskInput = document.getElementById('task-filter-input');
    if (taskInput) {
        taskInput.addEventListener('input', () => {
            renderTaskTrailTable();
        });
    }

    document.querySelectorAll('.filter-pills .filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-pills .filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            activeTaskStatusFilter = btn.getAttribute('data-status') || 'all';
            renderTaskTrailTable();
        });
    });
}

window.inspectTask = function(taskId) {
    const task = currentTasks.find(t => t.task_id === taskId);
    if (!task) return;
    document.getElementById('task-modal-id').textContent = `TASK: ${taskId}`;
    document.getElementById('task-modal-json').textContent = JSON.stringify(task, null, 2);
    openModal('modal-task-detail');
};

// -----------------------------------------------------------------------------
// UNIFIED KNOWLEDGE VAULT (WIKI & MEMORIES COMBINED)
// -----------------------------------------------------------------------------
function initUnifiedVault() {
    const searchInput = document.getElementById('vault-global-search');
    const clearBtn = document.getElementById('btn-clear-vault-search');
    let debounceTimer = null;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.trim();
        clearBtn.style.display = query ? 'block' : 'none';
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            if (query.length > 0) {
                searchVaultFTS(query);
            } else {
                loadUnifiedVault();
            }
        }, 220);
    });

    clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        clearBtn.style.display = 'none';
        loadUnifiedVault();
    });

    // Feed Tabs Switcher (ALL vs PAGES vs MEMORIES)
    const feedTabAll = document.getElementById('feed-tab-all');
    const feedTabPages = document.getElementById('feed-tab-pages');
    const feedTabMemories = document.getElementById('feed-tab-memories');

    feedTabAll.addEventListener('click', () => {
        setFeedMode('all');
    });

    feedTabPages.addEventListener('click', () => {
        setFeedMode('pages');
    });

    feedTabMemories.addEventListener('click', () => {
        setFeedMode('memories');
    });

    // Document & Memory Toolbar Actions
    document.getElementById('btn-copy-doc-markdown').addEventListener('click', () => {
        if (!selectedVaultItem || selectedVaultItem.type !== 'page' || !selectedVaultItem.data.content) return;
        navigator.clipboard.writeText(selectedVaultItem.data.content);
        showToast('Raw Markdown copied to clipboard!', 'success');
    });

    document.getElementById('btn-copy-doc-slug').addEventListener('click', () => {
        if (!selectedVaultItem || selectedVaultItem.type !== 'page' || !selectedVaultItem.data.slug) return;
        navigator.clipboard.writeText(selectedVaultItem.data.slug);
        showToast(`Slug "${selectedVaultItem.data.slug}" copied!`, 'success');
    });

    document.getElementById('btn-copy-mem-text').addEventListener('click', () => {
        if (!selectedVaultItem || selectedVaultItem.type !== 'memory' || !selectedVaultItem.data.text) return;
        navigator.clipboard.writeText(selectedVaultItem.data.text);
        showToast('Memory text copied to clipboard!', 'success');
    });

    document.getElementById('btn-open-doc-editor').addEventListener('click', () => {
        if (!selectedVaultItem || selectedVaultItem.type !== 'page') return;
        openWikiPageEditor(selectedVaultItem.data.slug);
    });

    document.getElementById('btn-delete-active-doc').addEventListener('click', async () => {
        if (!selectedVaultItem || selectedVaultItem.type !== 'page') return;
        const slug = selectedVaultItem.data.slug;
        if (!confirm(`Delete page "${slug}" from Monolith WikiDB?`)) return;

        try {
            const res = await fetch(`/api/wiki/page/${encodeURIComponent(slug)}`, { method: 'DELETE' });
            if (res.ok) {
                showToast(`Page ${slug} deleted`, 'success');
                resetReaderPane();
                loadUnifiedVault();
            } else {
                showToast('Failed to delete page', 'error');
            }
        } catch (e) {
            showToast('Delete error: ' + e.message, 'error');
        }
    });

    document.getElementById('btn-delete-active-mem').addEventListener('click', async () => {
        if (!selectedVaultItem || selectedVaultItem.type !== 'memory') return;
        const uid = selectedVaultItem.data.uid;
        if (!confirm(`Delete memory ${uid}?`)) return;

        try {
            const res = await fetch(`/api/wiki/memory/${encodeURIComponent(uid)}`, { method: 'DELETE' });
            if (res.ok) {
                showToast('Memory deleted successfully', 'success');
                resetReaderPane();
                loadUnifiedVault();
            } else {
                showToast('Failed to delete memory', 'error');
            }
        } catch (e) {
            showToast('Delete error: ' + e.message, 'error');
        }
    });

    // Split Live Previews in Editor Modals
    const wikiEditContent = document.getElementById('wiki-edit-content');
    const wikiEditPreview = document.getElementById('wiki-edit-preview');
    wikiEditContent.addEventListener('input', () => {
        if (window.marked) wikiEditPreview.innerHTML = marked.parse(wikiEditContent.value);
    });

    const skillEditContent = document.getElementById('skill-edit-content');
    const skillEditPreview = document.getElementById('skill-edit-preview');
    skillEditContent.addEventListener('input', () => {
        if (window.marked) skillEditPreview.innerHTML = marked.parse(skillEditContent.value);
    });
}

function setFeedMode(mode) {
    activeFeedMode = mode;
    document.getElementById('feed-tab-all').classList.toggle('active', mode === 'all');
    document.getElementById('feed-tab-pages').classList.toggle('active', mode === 'pages');
    document.getElementById('feed-tab-memories').classList.toggle('active', mode === 'memories');
    renderVaultFeedItems();
}

async function loadUnifiedVault() {
    try {
        const [statsRes, pagesRes, memRes] = await Promise.all([
            fetch('/api/wiki/stats'),
            fetch(`/api/wiki/pages?category=${encodeURIComponent(activeVaultCategory)}&limit=80`),
            fetch(`/api/wiki/memories?category=${encodeURIComponent(activeVaultCategory)}&limit=100`)
        ]);

        const statsData = await statsRes.json();
        const pagesData = await pagesRes.json();
        const memData = await memRes.json();

        currentPages = pagesData.pages || [];
        currentMemories = memData.memories || [];

        const totalPages = statsData.stats ? statsData.stats.pages : currentPages.length;
        const totalMemories = statsData.stats ? statsData.stats.memories : currentMemories.length;
        const totalAll = totalPages + totalMemories;

        document.getElementById('feed-all-count').textContent = currentPages.length + currentMemories.length;
        document.getElementById('feed-pages-count').textContent = currentPages.length;
        document.getElementById('feed-memories-count').textContent = currentMemories.length;
        document.getElementById('tab-count-vault').textContent = totalAll;

        document.getElementById('current-category-display').textContent = activeVaultCategory.toUpperCase();

        renderSidebarCollections(statsData.categories, totalPages, totalMemories);
        renderVaultFeedItems();

        // Auto-select first item if none active
        if (!selectedVaultItem) {
            if (currentPages.length > 0) {
                selectVaultPage(currentPages[0].slug);
            } else if (currentMemories.length > 0) {
                selectVaultMemory(currentMemories[0].uid);
            }
        }
    } catch (e) {
        console.error('Failed to load Unified Vault:', e);
    }
}

function renderSidebarCollections(categories, totalPages, totalMemories) {
    const container = document.getElementById('sidebar-categories-tree');
    const totalCount = Object.keys(categories || {}).length;
    document.getElementById('sidebar-total-categories').textContent = totalCount;

    let html = `
        <div class="sidebar-cat-item ${activeVaultCategory === 'all' ? 'active' : ''}" onclick="selectVaultCategoryNav('all')">
            <span>🌐 ALL VAULT KNOWLEDGE</span>
            <span class="sidebar-cat-count">${totalPages + totalMemories}</span>
        </div>

        <div class="sidebar-group-header">⚡ MEMORY DOMAINS</div>
        <div class="sidebar-cat-item ${activeVaultCategory === 'models' ? 'active' : ''}" onclick="selectVaultCategoryNav('models')">
            <span>🧠 Model Specs & Context</span>
            <span class="sidebar-cat-count">18</span>
        </div>
        <div class="sidebar-cat-item ${activeVaultCategory === 'agents' ? 'active' : ''}" onclick="selectVaultCategoryNav('agents')">
            <span>🤖 Agent Personas</span>
            <span class="sidebar-cat-count">10</span>
        </div>
        <div class="sidebar-cat-item ${activeVaultCategory === 'system' ? 'active' : ''}" onclick="selectVaultCategoryNav('system')">
            <span>⚙️ System & PON Facts</span>
            <span class="sidebar-cat-count">${categories.system || 8}</span>
        </div>

        <div class="sidebar-group-header">📚 DOCUMENT COLLECTIONS</div>
    `;

    for (const [cat, count] of Object.entries(categories || {})) {
        if (['models', 'agents', 'system'].includes(cat)) continue;
        html += `
            <div class="sidebar-cat-item ${activeVaultCategory === cat ? 'active' : ''}" onclick="selectVaultCategoryNav('${escapeHtml(cat)}')">
                <span>📁 ${escapeHtml(cat)}</span>
                <span class="sidebar-cat-count">${count}</span>
            </div>
        `;
    }

    container.innerHTML = html;
}

window.selectVaultCategoryNav = function(cat) {
    activeVaultCategory = cat;
    loadUnifiedVault();
};

function renderVaultFeedItems() {
    const container = document.getElementById('vault-feed-items');
    let feedItems = [];

    if (activeFeedMode === 'all' || activeFeedMode === 'pages') {
        currentPages.forEach(p => feedItems.push({ type: 'page', data: p }));
    }
    if (activeFeedMode === 'all' || activeFeedMode === 'memories') {
        currentMemories.forEach(m => feedItems.push({ type: 'memory', data: m }));
    }

    if (feedItems.length === 0) {
        container.innerHTML = `<div class="empty-state">[NO ITEMS MATCHING CURRENT FILTER]</div>`;
        return;
    }

    container.innerHTML = feedItems.map(item => {
        if (item.type === 'page') {
            const page = item.data;
            const isSelected = selectedVaultItem && selectedVaultItem.type === 'page' && selectedVaultItem.data.slug === page.slug;
            return `
                <div class="feed-item-card ${isSelected ? 'active-item' : ''}" onclick="selectVaultPage('${escapeHtml(page.slug)}')">
                    <div class="feed-card-header">
                        <span class="feed-item-type-badge badge-doc">DOC</span>
                        <span style="font-size:0.68rem; color:var(--dim-gray); font-family:'Fira Code', monospace;">// ${escapeHtml(page.category || 'general')}</span>
                    </div>
                    <div class="feed-card-title">${escapeHtml(page.title || page.slug)}</div>
                    <div class="feed-card-snippet">${escapeHtml(page.snippet || page.content || '')}</div>
                </div>
            `;
        } else {
            const mem = item.data;
            const isSelected = selectedVaultItem && selectedVaultItem.type === 'memory' && selectedVaultItem.data.uid === mem.uid;
            
            let typeBadge = 'badge-memory';
            let badgeText = (mem.category || 'MEM').toUpperCase();
            if (mem.category === 'models') { typeBadge = 'badge-model'; badgeText = 'MODEL'; }
            if (mem.category === 'agents') { typeBadge = 'badge-agent'; badgeText = 'AGENT'; }

            let title = mem.owner || 'Memory Fact';
            let preview = mem.text || '';
            if (preview.includes('|')) {
                const parts = preview.split('|');
                title = parts[0].trim();
                preview = parts.slice(1).join(' | ').trim();
            }

            return `
                <div class="feed-item-card ${isSelected ? 'active-item' : ''}" onclick="selectVaultMemory('${escapeHtml(mem.uid)}')">
                    <div class="feed-card-header">
                        <span class="feed-item-type-badge ${typeBadge}">${badgeText}</span>
                        <span style="font-size:0.68rem; color:var(--dim-gray); font-family:'Fira Code', monospace;">UID: ${(mem.uid || '').substring(0, 8)}</span>
                    </div>
                    <div class="feed-card-title">${escapeHtml(title)}</div>
                    <div class="feed-card-snippet">${escapeHtml(preview)}</div>
                </div>
            `;
        }
    }).join('');
}

window.selectVaultPage = async function(slug) {
    try {
        const res = await fetch(`/api/wiki/page/${encodeURIComponent(slug)}`);
        if (!res.ok) throw new Error('Could not fetch page');
        const data = await res.json();
        
        selectedVaultItem = { type: 'page', data: data.page };

        document.getElementById('reader-empty-view').style.display = 'none';
        document.getElementById('reader-memory-view').style.display = 'none';
        document.getElementById('reader-doc-view').style.display = 'flex';

        const page = data.page;
        document.getElementById('doc-view-title').textContent = page.title || page.slug;
        document.getElementById('doc-view-slug').textContent = `// ${page.slug}`;
        document.getElementById('doc-view-category').textContent = (page.category || 'GENERAL').toUpperCase();
        document.getElementById('doc-view-trust').textContent = `TRUST: ${page.trust_score || 1.0}`;
        
        const dateStr = page.updated_at ? new Date(page.updated_at * 1000).toLocaleString() : 'N/A';
        document.getElementById('doc-view-date').textContent = `UPDATED: ${dateStr}`;

        document.getElementById('doc-view-source-path').textContent = page.source_path || 'internal://wiki.db';
        document.getElementById('doc-view-owner').textContent = page.owner || 'harness';
        document.getElementById('doc-view-metadata-json').textContent = page.metadata_json || '{}';

        const bodyContainer = document.getElementById('doc-view-rendered-body');
        if (window.marked) {
            bodyContainer.innerHTML = marked.parse(page.content || '');
        } else {
            bodyContainer.textContent = page.content || '';
        }

        renderVaultFeedItems();
    } catch (e) {
        showToast('Error loading document: ' + e.message, 'error');
    }
};

window.selectVaultMemory = function(uid) {
    const mem = currentMemories.find(m => m.uid === uid);
    if (!mem) return;

    selectedVaultItem = { type: 'memory', data: mem };

    document.getElementById('reader-empty-view').style.display = 'none';
    document.getElementById('reader-doc-view').style.display = 'none';
    document.getElementById('reader-memory-view').style.display = 'flex';

    let title = mem.owner || 'Memory Record';
    let bodyText = mem.text || '';
    if (bodyText.includes('|')) {
        const parts = bodyText.split('|');
        title = parts[0].trim();
        bodyText = parts.slice(1).join(' | ').trim();
    }

    document.getElementById('mem-view-title').textContent = title;
    document.getElementById('mem-view-category').textContent = (mem.category || 'SYSTEM').toUpperCase();
    document.getElementById('mem-view-trust').textContent = `TRUST: ${mem.trust_score || 1.0}`;
    
    const dateStr = mem.timestamp ? new Date(mem.timestamp * 1000).toLocaleString() : 'N/A';
    document.getElementById('mem-view-date').textContent = `RECORDED: ${dateStr}`;
    document.getElementById('mem-view-uid').textContent = `// UID: ${mem.uid || 'N/A'}`;
    document.getElementById('mem-view-owner').textContent = mem.owner || 'omnirouter';
    document.getElementById('mem-view-source').textContent = mem.source || 'harness:monolith';

    document.getElementById('mem-view-text').textContent = mem.text || '';

    renderVaultFeedItems();
};

function resetReaderPane() {
    selectedVaultItem = null;
    document.getElementById('reader-doc-view').style.display = 'none';
    document.getElementById('reader-memory-view').style.display = 'none';
    document.getElementById('reader-empty-view').style.display = 'flex';
}

async function searchVaultFTS(query) {
    try {
        const res = await fetch(`/api/wiki/search?q=${encodeURIComponent(query)}&limit=50`);
        const data = await res.json();
        currentPages = data.pages || [];
        currentMemories = data.memories || [];
        
        document.getElementById('feed-all-count').textContent = currentPages.length + currentMemories.length;
        document.getElementById('feed-pages-count').textContent = currentPages.length;
        document.getElementById('feed-memories-count').textContent = currentMemories.length;

        renderVaultFeedItems();

        if (currentPages.length > 0) {
            selectVaultPage(currentPages[0].slug);
        } else if (currentMemories.length > 0) {
            selectVaultMemory(currentMemories[0].uid);
        }
    } catch (e) {
        console.error('Vault FTS search error:', e);
    }
}

window.openWikiPageEditor = async function(slug) {
    try {
        const res = await fetch(`/api/wiki/page/${encodeURIComponent(slug)}`);
        if (!res.ok) throw new Error('Could not fetch page');
        const data = await res.json();
        const page = data.page;

        document.getElementById('wiki-modal-header-title').textContent = `EDIT PAGE: ${page.slug}`;
        document.getElementById('wiki-edit-title').value = page.title || '';
        document.getElementById('wiki-edit-slug').value = page.slug || '';
        document.getElementById('wiki-edit-category').value = page.category || 'general';
        document.getElementById('wiki-edit-content').value = page.content || '';

        const previewPane = document.getElementById('wiki-edit-preview');
        if (window.marked) previewPane.innerHTML = marked.parse(page.content || '');

        openModal('modal-wiki-page');
    } catch (e) {
        showToast('Error opening page: ' + e.message, 'error');
    }
};

// -----------------------------------------------------------------------------
// Skills Directory & Studio
// -----------------------------------------------------------------------------
function initSkills() {
    const searchInput = document.getElementById('skills-search-input');
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        renderSkillsCatalog(query);
    });
}

async function loadSkillsCatalog() {
    try {
        const res = await fetch('/api/skills');
        const data = await res.json();
        currentSkills = data.skills || [];
        renderSkillsCatalog();
        document.getElementById('tab-count-skills').textContent = currentSkills.length;
    } catch (e) {
        console.error('Failed to load skills:', e);
    }
}

function renderSkillsCatalog(filter = '') {
    const container = document.getElementById('skills-catalog-grid');
    const filtered = currentSkills.filter(s => {
        if (!filter) return true;
        const text = `${s.name} ${s.description} ${s.tags}`.toLowerCase();
        return text.includes(filter);
    });

    if (filtered.length === 0) {
        container.innerHTML = `<div class="empty-state" style="grid-column: 1/-1;">[NO CANONICAL SKILLS MATCH]</div>`;
        return;
    }

    container.innerHTML = filtered.map(s => {
        const tags = (s.tags || '').split(',').map(t => t.trim()).filter(Boolean);
        const tagsHtml = tags.map(t => `<span class="tag-badge">${escapeHtml(t)}</span>`).join('');

        return `
            <div class="skill-card" onclick="openSkillStudio('${escapeHtml(s.slug)}')">
                <div class="skill-card-top">
                    <div class="skill-card-name">// ${escapeHtml(s.name)}</div>
                    <div class="skill-card-desc">${escapeHtml(s.description)}</div>
                </div>
                <div class="skill-card-tags">
                    ${tagsHtml}
                </div>
            </div>
        `;
    }).join('');
}

window.openSkillStudio = async function(slug) {
    try {
        const res = await fetch(`/api/skill/${encodeURIComponent(slug)}`);
        if (!res.ok) throw new Error('Skill not found');
        const skill = await res.json();

        document.getElementById('skill-modal-title').textContent = `SKILL STUDIO: ${skill.name}`;
        document.getElementById('skill-edit-slug').value = skill.slug;
        document.getElementById('skill-edit-content').value = skill.content;

        const preview = document.getElementById('skill-edit-preview');
        if (window.marked) preview.innerHTML = marked.parse(skill.body || skill.content);

        openModal('modal-skill-studio');
    } catch (e) {
        showToast('Error opening skill: ' + e.message, 'error');
    }
};

// -----------------------------------------------------------------------------
// Models, Archetypes & Combos
// -----------------------------------------------------------------------------
function initModels() {}

async function loadModelsCatalog() {
    try {
        const res = await fetch('/api/models');
        const data = await res.json();

        const archContainer = document.getElementById('archetypes-catalog');
        if (data.archetypes) {
            archContainer.innerHTML = Object.entries(data.archetypes).map(([key, val]) => {
                const caps = (val.capabilities || []).map(c => `<span class="cap-badge">${escapeHtml(c)}</span>`).join('');
                
                const amdyModels = (val.amdy || []).map(m => m.model).join(', ') || 'None';
                const tellModels = (val.tell || []).map(m => m.model).join(', ') || 'None';

                return `
                    <div class="archetype-card">
                        <div class="archetype-title">ARCHETYPE: ${escapeHtml(key)}</div>
                        <div class="archetype-desc">${escapeHtml(val.description || '')}</div>
                        <div class="archetype-capabilities">${caps}</div>
                        <div class="archetype-models-list">
                            <div><strong style="color:var(--primary-red)">amdy (Exec):</strong> ${escapeHtml(amdyModels)}</div>
                            <div><strong style="color:var(--accent-yellow)">tell (State):</strong> ${escapeHtml(tellModels)}</div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        const tbody = document.getElementById('combos-table-body');
        if (data.combos && data.combos.length > 0) {
            tbody.innerHTML = data.combos.map(c => {
                let tierClass = 'pill-running';
                if (c.tier === 'local') tierClass = 'pill-success';
                if (c.tier === 'paid') tierClass = 'pill-failed';

                return `
                    <tr>
                        <td style="font-weight:bold; color:var(--primary-red);">${escapeHtml(c.id)}</td>
                        <td>${escapeHtml((c.provider || '').toUpperCase())}</td>
                        <td>${escapeHtml(c.model)}</td>
                        <td><span class="stat-pill ${tierClass}">${(c.tier || '').toUpperCase()}</span></td>
                        <td><span class="tag-badge">${(c.power || 'standard').toUpperCase()}</span></td>
                        <td>${c.score || '--'}</td>
                        <td style="font-size:0.75rem; color:var(--dim-gray);">${escapeHtml(c.secret_key || 'LOCAL OPEN-WEIGHTS')}</td>
                    </tr>
                `;
            }).join('');
        }
    } catch (e) {
        console.error('Failed to load models:', e);
    }
}

// -----------------------------------------------------------------------------
// Interactive Prompt Testbed / Lab
// -----------------------------------------------------------------------------
function initTestbed() {
    const runBtn = document.getElementById('btn-run-test-prompt');
    const promptInput = document.getElementById('testbed-prompt-input');
    const consoleBox = document.getElementById('testbed-output-console');
    const durationBadge = document.getElementById('testbed-duration-badge');

    if (!runBtn || !promptInput) return;

    const dispatchPrompt = async () => {
        const category = document.getElementById('testbed-category-select').value;
        const prompt = promptInput.value.trim();
        if (!prompt) {
            showToast('Please enter a test prompt', 'error');
            return;
        }

        runBtn.disabled = true;
        document.getElementById('testbed-btn-text').textContent = 'DISPATCHING PROMPT...';
        consoleBox.textContent = `// Dispatching to [${category}] via ModelRouter...\n// Awaiting response from local/remote provider...\n`;
        durationBadge.textContent = '...';

        try {
            const res = await fetch('/api/models/test-prompt', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ category, prompt })
            });
            const data = await res.json();
            durationBadge.textContent = `${data.duration_seconds || 0}s`;
            consoleBox.textContent = data.output || '[No output returned]';
        } catch (e) {
            consoleBox.textContent = `// ERROR: ${e.message}`;
            durationBadge.textContent = 'ERR';
        } finally {
            runBtn.disabled = false;
            document.getElementById('testbed-btn-text').textContent = '🚀 DISPATCH TO HARNESS';
        }
    };

    runBtn.addEventListener('click', dispatchPrompt);

    // Ctrl+Enter or Cmd+Enter shortcut
    promptInput.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            e.preventDefault();
            dispatchPrompt();
        }
    });
}

// -----------------------------------------------------------------------------
// System Controls & Modals
// -----------------------------------------------------------------------------
function initControls() {
    const crtBtn = document.getElementById('btn-scanlines-toggle');
    if (crtBtn) {
        crtBtn.addEventListener('click', () => {
            document.body.classList.toggle('crt-enabled');
            const enabled = document.body.classList.contains('crt-enabled');
            crtBtn.textContent = enabled ? 'CRT: ON' : 'CRT: OFF';
            showToast(`Scanlines: ${enabled ? 'ENABLED' : 'DISABLED'}`, 'info');
        });
    }

    const consolidateBtn = document.getElementById('btn-quick-consolidate');
    if (consolidateBtn) {
        consolidateBtn.addEventListener('click', async () => {
            const originalText = consolidateBtn.textContent;
            consolidateBtn.disabled = true;
            consolidateBtn.textContent = 'SYNCING...';
            showToast('Initiating Wiki Consolidation...', 'info');
            try {
                const res = await fetch('/api/control/consolidate', { method: 'POST' });
                const data = await res.json();
                if (data.returncode === 0) {
                    showToast('Wiki consolidated successfully!', 'success');
                    loadUnifiedVault();
                } else {
                    showToast('Consolidation finished with warnings', 'error');
                }
            } catch (e) {
                showToast('Consolidation failed: ' + e.message, 'error');
            } finally {
                consolidateBtn.disabled = false;
                consolidateBtn.textContent = originalText;
            }
        });
    }

    const syncSkillsBtn = document.getElementById('btn-quick-skills-sync');
    if (syncSkillsBtn) {
        syncSkillsBtn.addEventListener('click', async () => {
            const originalText = syncSkillsBtn.textContent;
            syncSkillsBtn.disabled = true;
            syncSkillsBtn.textContent = 'INSTALLING...';
            showToast('Linking canonical skills into all environments...', 'info');
            try {
                const res = await fetch('/api/control/sync-skills', { method: 'POST' });
                const data = await res.json();
                if (data.returncode === 0) {
                    showToast('Skills installed & linked!', 'success');
                    loadSkillsCatalog();
                } else {
                    showToast('Skills install returned error', 'error');
                }
            } catch (e) {
                showToast('Skills sync failed: ' + e.message, 'error');
            } finally {
                syncSkillsBtn.disabled = false;
                syncSkillsBtn.textContent = originalText;
            }
        });
    }

    const saveWikiBtn = document.getElementById('btn-save-wiki-page');
    if (saveWikiBtn) {
        saveWikiBtn.addEventListener('click', async () => {
            const title = document.getElementById('wiki-edit-title').value.trim();
            const slug = document.getElementById('wiki-edit-slug').value.trim();
            const category = document.getElementById('wiki-edit-category').value.trim();
            const content = document.getElementById('wiki-edit-content').value;

            if (!title || !content) {
                showToast('Title and content are required', 'error');
                return;
            }

            try {
                const res = await fetch(`/api/wiki/page/${encodeURIComponent(slug)}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ title, slug, category, content })
                });
                if (res.ok) {
                    showToast('Page saved to Monolith WikiDB', 'success');
                    closeModal('modal-wiki-page');
                    loadUnifiedVault();
                    selectVaultPage(slug);
                } else {
                    showToast('Failed to save page', 'error');
                }
            } catch (e) {
                showToast('Save error: ' + e.message, 'error');
            }
        });
    }

    const deleteWikiBtn = document.getElementById('btn-delete-wiki-page');
    if (deleteWikiBtn) {
        deleteWikiBtn.addEventListener('click', async () => {
            const slug = document.getElementById('wiki-edit-slug').value.trim();
            if (!slug) return;
            if (!confirm(`Permanently delete page "${slug}"?`)) return;

            try {
                const res = await fetch(`/api/wiki/page/${encodeURIComponent(slug)}`, { method: 'DELETE' });
                if (res.ok) {
                    showToast('Page deleted from WikiDB', 'success');
                    closeModal('modal-wiki-page');
                    resetReaderPane();
                    loadUnifiedVault();
                } else {
                    showToast('Failed to delete page', 'error');
                }
            } catch (e) {
                showToast('Delete error: ' + e.message, 'error');
            }
        });
    }

    const saveSkillBtn = document.getElementById('btn-save-skill');
    if (saveSkillBtn) {
        saveSkillBtn.addEventListener('click', async () => {
            const slug = document.getElementById('skill-edit-slug').value;
            const content = document.getElementById('skill-edit-content').value;

            try {
                const res = await fetch(`/api/skill/${encodeURIComponent(slug)}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ content })
                });
                if (res.ok) {
                    showToast(`Skill ${slug} saved!`, 'success');
                    closeModal('modal-skill-studio');
                    loadSkillsCatalog();
                } else {
                    showToast('Failed to save skill', 'error');
                }
            } catch (e) {
                showToast('Skill save error: ' + e.message, 'error');
            }
        });
    }

    const createPageBtn = document.getElementById('btn-create-page');
    if (createPageBtn) {
        createPageBtn.addEventListener('click', () => {
            document.getElementById('wiki-modal-header-title').textContent = 'CREATE NEW WIKI PAGE';
            document.getElementById('wiki-edit-title').value = '';
            document.getElementById('wiki-edit-slug').value = '';
            document.getElementById('wiki-edit-category').value = 'architecture';
            document.getElementById('wiki-edit-content').value = '# New Document\n\nEnter architectural facts and documentation...';
            const preview = document.getElementById('wiki-edit-preview');
            if (window.marked && preview) preview.innerHTML = marked.parse('# New Document\n\nEnter architectural facts and documentation...');
            openModal('modal-wiki-page');
        });
    }

    const createMemBtn = document.getElementById('btn-create-memory');
    if (createMemBtn) {
        createMemBtn.addEventListener('click', () => {
            document.getElementById('new-memory-text').value = '';
            openModal('modal-create-memory');
        });
    }

    const submitMemBtn = document.getElementById('btn-submit-memory');
    if (submitMemBtn) {
        submitMemBtn.addEventListener('click', async () => {
            const category = document.getElementById('new-memory-category').value.trim() || 'models';
            const owner = document.getElementById('new-memory-owner').value.trim() || 'omnirouter';
            const text = document.getElementById('new-memory-text').value.trim();
            if (!text) {
                showToast('Memory specification text is required', 'error');
                return;
            }

            try {
                const res = await fetch('/api/wiki/memory', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ category, owner, text, source: 'dashboard:user_entry' })
                });
                if (res.ok) {
                    showToast('Memory injected into vault', 'success');
                    closeModal('modal-create-memory');
                    loadUnifiedVault();
                } else {
                    showToast('Failed to inject memory', 'error');
                }
            } catch (e) {
                showToast('Memory creation error: ' + e.message, 'error');
            }
        });
    }

    const createSkillBtn = document.getElementById('btn-create-skill');
    if (createSkillBtn) {
        createSkillBtn.addEventListener('click', () => {
            document.getElementById('new-skill-name').value = '';
            document.getElementById('new-skill-desc').value = '';
            openModal('modal-create-skill');
        });
    }

    const submitSkillBtn = document.getElementById('btn-submit-create-skill');
    if (submitSkillBtn) {
        submitSkillBtn.addEventListener('click', async () => {
            const name = document.getElementById('new-skill-name').value.trim();
            const description = document.getElementById('new-skill-desc').value.trim();
            const tags = document.getElementById('new-skill-tags').value.trim();
            if (!name || !description) {
                showToast('Skill name and description are required', 'error');
                return;
            }

            try {
                const res = await fetch('/api/skill', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, description, tags })
                });
                if (res.ok) {
                    showToast(`Skill ${name} initialized!`, 'success');
                    closeModal('modal-create-skill');
                    loadSkillsCatalog();
                } else {
                    showToast('Failed to create skill', 'error');
                }
            } catch (e) {
                showToast('Skill init error: ' + e.message, 'error');
            }
        });
    }
}

function initModals() {
    document.querySelectorAll('[data-close]').forEach(btn => {
        btn.addEventListener('click', () => {
            const modalId = btn.getAttribute('data-close');
            closeModal(modalId);
        });
    });

    document.querySelectorAll('.modal-overlay').forEach(overlay => {
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                overlay.classList.remove('active');
            }
        });
    });

    // Keyboard ESC shortcut to close any open modal
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal-overlay.active').forEach(modal => {
                modal.classList.remove('active');
            });
        }
    });
}

window.openModal = function(id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.add('active');
};

window.closeModal = function(id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.remove('active');
};

function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

function escapeHtml(str) {
    if (typeof str !== 'string') return '';
    return str.replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;')
              .replace(/'/g, '&#039;');
}

// =============================================================================
// DYNAMIC CYBERPUNK BACKGROUND ENGINE (PARALLAX, PARTICLES & PULSE)
// =============================================================================
let bgNetworkPulseAlpha = 0;

function pulseBackgroundNetwork() {
    bgNetworkPulseAlpha = 1.0;
}

function initDynamicCyberBackground() {
    const canvas = document.getElementById('bg-cyber-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = Math.min(65, Math.floor((width * height) / 22000));

    for (let i = 0; i < particleCount; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.45,
            vy: (Math.random() - 0.5) * 0.45,
            radius: Math.random() * 1.8 + 0.8,
            baseAlpha: Math.random() * 0.4 + 0.2,
            color: Math.random() > 0.85 ? '#ffcf3d' : '#ff4040'
        });
    }

    // Dynamic Parallax on Mouse Movement
    let mouse = { x: -1000, y: -1000 };
    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    // Dynamic Parallax on Page Scroll
    let lastScrollY = window.scrollY;
    window.addEventListener('scroll', () => {
        const delta = window.scrollY - lastScrollY;
        lastScrollY = window.scrollY;
        particles.forEach(p => {
            p.y -= delta * 0.2;
            if (p.y < 0) p.y += height;
            if (p.y > height) p.y -= height;
        });
    }, { passive: true });

    // Also listen to internal workspace scroll events
    document.addEventListener('wheel', (e) => {
        const scrollDelta = e.deltaY * 0.08;
        particles.forEach(p => {
            p.y -= scrollDelta;
            if (p.y < 0) p.y += height;
            if (p.y > height) p.y -= height;
        });
    }, { passive: true });

    function renderFrame() {
        ctx.clearRect(0, 0, width, height);

        // Render Connections
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 130) {
                    const lineAlpha = (1 - dist / 130) * 0.15 + (bgNetworkPulseAlpha * 0.25);
                    ctx.strokeStyle = `rgba(255, 64, 64, ${Math.min(0.8, lineAlpha)})`;
                    ctx.lineWidth = lineAlpha > 0.2 ? 1.2 : 0.7;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }

        // Render Particles
        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;

            // Mouse gentle repulsion
            const mdx = p.x - mouse.x;
            const mdy = p.y - mouse.y;
            const mDist = Math.sqrt(mdx * mdx + mdy * mdy);
            if (mDist < 120) {
                const force = (1 - mDist / 120) * 0.8;
                p.x += (mdx / mDist) * force;
                p.y += (mdy / mDist) * force;
            }

            // Screen wrap
            if (p.x < 0) p.x = width;
            if (p.x > width) p.x = 0;
            if (p.y < 0) p.y = height;
            if (p.y > height) p.y = 0;

            const alpha = Math.min(1, p.baseAlpha + bgNetworkPulseAlpha * 0.5);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = alpha;
            ctx.shadowBlur = 8;
            ctx.shadowColor = p.color;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fill();

            ctx.shadowBlur = 0;
            ctx.globalAlpha = 1.0;
        });

        // Decay pulse
        if (bgNetworkPulseAlpha > 0.01) {
            bgNetworkPulseAlpha *= 0.94;
        } else {
            bgNetworkPulseAlpha = 0;
        }

        requestAnimationFrame(renderFrame);
    }

    renderFrame();
}
