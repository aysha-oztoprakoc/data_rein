# // data_rein Harness Skills — Canonical Registry

This directory is the **single source of truth** for every skill available to
agents operating under the `data_rein` harness.

**Prime Agent Philosophy (Skills are Executable):**
Skills are not just passive Markdown files to stuff into context windows. Under the RLM paradigm, skills are executable Python modules, prompts, or REPL hooks that the agent invokes programmatically. The YAML frontmatter in `SKILL.md` provides discovery and routing context.

Exactly the 154 registered entries below are canonical. Each is a real,
non-symlink directory containing a `SKILL.md` and their respective programmatic hooks.

## Registered skills

| Skill | Purpose |
|---|---|
| `address-sanitizer` | AddressSanitizer detects memory errors during fuzzing. Use when fuzzing C/C++ code to find buffer overflows and use-after-free bugs. |
| `aflpp` | AFL++ is a fork of AFL with better fuzzing performance and advanced features. Use for multi-core fuzzing of C/C++ projects. |
| `agentic-actions-auditor` | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations. |
| `agy-pon-compliance` | Notification-Oriented Paradigm (PON) architectural law — zero polling, amdy/tell split, FBE, graceful degradation. Lo... |
| `algorand-vulnerability-scanner` | Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal). |
| `archify` | Create polished, validated architecture, workflow, sequence, data-flow, and lifecycle/state diagrams as explorable st... |
| `ask-matt` | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| `atheris` | Atheris is a coverage-guided Python fuzzer based on libFuzzer. Use for fuzzing pure Python code and Python C extensions. |
| `audit-augmentation` | Augments Trailmark code graphs with external audit findings from SARIF static analysis results, weAudit annotation files, and version-gated Trailmark 0.4.x binary-analysis graph exports. Maps findings to graph nodes by file and line overlap, creates severity-based subgraphs, and enables cross-referencing findings with pre-analysis data (blast radius, taint, etc.). Use when projecting SARIF results onto a code graph, overlaying weAudit |
| `audit-context-building` | Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit, threat model, or architecture review on unfamiliar code, and before any vulnerability-hunting pass. |
| `audit-prep-assistant` | Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments). |
| `aws-ami-builder` | Build Amazon Machine Images (AMIs) with Packer using the amazon-ebs builder. Use when creating custom AMIs for E... |
| `azure-image-builder` | Build Azure managed images and Azure Compute Gallery images with Packer. Use when creating custom images for Azu... |
| `azure-verified-modules` | Azure Verified Modules (AVM) requirements and best practices for developing certified Azure Terraform modules. U... |
| `book-to-skill` | Converts books and documents (PDF, EPUB, DOCX, HTML, Markdown, plain text, RTF, MOBI/AZW with Calibre) into structure... |
| `burpsuite-project-parser` | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project. |
| `c-review` | Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code. |
| `cairo-vulnerability-scanner` | Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects. |
| `cargo-fuzz` | cargo-fuzz is the de facto fuzzing tool for Rust projects using Cargo. Use for fuzzing Rust code with libFuzzer backend. |
| `chrome-mcp-troubleshooting` | Imported Trail of Bits security skill. |
| `claude-handoff` | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| `code-maturity-assessor` | Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations. |
| `code-review` | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code... |
| `codebase-design` | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find... |
| `codeql` | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "build codeql database", "SAST scan", "taint analysis", "dataflow analysis", or "find vulnerabilities in this repo". Covers Python, JavaScript/TypeScript, Go, Java/Kotlin, C/C++, C#, Ruby, and Swift. Supports "run all" (security-and-quality + security-experimental) and "important only" (high-precision) scan modes, and creates data extension models for project-specific sources |
| `constant-time-analysis` | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby. |
| `constant-time-testing` | Constant-time testing detects timing side channels in cryptographic code. Use when auditing crypto implementations for timing vulnerabilities. |
| `cosmos-vulnerability-scanner` | Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x. |
| `coverage-analysis` | Coverage analysis measures code exercised during fuzzing. Use when assessing harness effectiveness or identifying fuzzing blockers. |
| `crypto-protocol-diagram` | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols. |
| `data_rein` | Universal data_rein harness — unified wiki DB, model-agnostic routing, PON, memory sync. Canonical skill for Odysseus... |
| `deep-research-paper` | Optimize the workflow for writing massive, extremely deep academic papers and monographs by chunking generation, orga... |
| `design-an-interface` | Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants t... |
| `devcontainer-setup` | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces. |
| `diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports ... |
| `diagramming-code` | Generates Mermaid diagrams from Trailmark code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and attack surface data flow visualizations. Use when visualizing code architecture, drawing call graphs, generating class diagrams, creating dependency maps, producing complexity heatmaps, or visualizing data flow and attack surface paths as Mermaid diagrams. |
| `differential-review` | Performs security-focused differential review of code changes (PRs, commits, diffs). Adapts analysis depth to codebase size, uses git history for context, calculates blast radius, checks test coverage, and generates comprehensive markdown reports. Automatically detects and prevents security regressions. |
| `dimensional-analysis` | Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early. |
| `domain-modeling` | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md... |
| `dwarf-expert` | Analyzes DWARF debug information in compiled binaries. Use when inspecting .debug_* sections, DIE trees, or DW_TAG_/DW_AT_ entries with dwarfdump/llvm-dwarfdump or readelf, verifying debug info with llvm-dwarfdump --verify, answering DWARF standard questions, or writing code that parses DWARF (libdwarf, pyelftools, gimli). |
| `edit-article` | Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to ... |
| `entry-point-analyzer` | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations. |
| `firebase-apk-scanner` | Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only. |
| `fp-check` | Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for each. Use when asked whether a specific finding is real, exploitable, or a false positive, or to verify or validate a suspected vulnerability — not for hunting or discovering new bugs. |
| `fuzzing-dictionary` | Fuzzing dictionaries guide fuzzers with domain-specific tokens. Use when fuzzing parsers, protocols, or format-specific code. |
| `fuzzing-obstacles` | Techniques for patching code to overcome fuzzing obstacles. Use when checksums, global state, or other barriers block fuzzer progress. |
| `genotoxic` | Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist. |
| `gh-cli` | Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues. |
| `git-cleanup` | Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work. |
| `git-guardrails-claude-code` | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they exe... |
| `github-triage` | Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs — incrementally merging passing automated/bot PRs and maintainer-approved ones, and spawning review subagents for never-reviewed ones — then closes already-resolved issues with comments citing the resolving PR or commit, cross-links issues with their pending fix PRs, and assigns local-only priority and change-size estimates for everything outstanding. Use when triaging, grooming, or reviewing a repository's open issues and PRs. |
| `graph-evolution` | Compares Trailmark code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast radius growth, taint propagation changes, and privilege boundary modifications that text diffs miss. Use when comparing code between commits or tags, analyzing structural evolution, detecting attack surface growth, reviewing what changed between |
| `grill-me` | A relentless interview to sharpen a plan or design. |
| `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `grilling` | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, o... |
| `guidelines-advisor` | Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations. |
| `handoff` | Compact the current conversation into a handoff document for another agent to pick up. |
| `harness-writing` | Techniques for writing effective fuzzing harnesses across languages. Use when creating new fuzz targets or improving existing harness code. |
| `hermes-persona` | Assume the Data-Hermes persona: the fused orchestrator of the data_rein harness. Handover context + mission objectives. |
| `implement` | Implement a piece of work based on a spec or set of tickets. |
| `improve-codebase-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one y... |
| `insecure-defaults` | Audits a project for insecure default configurations (SAST/networking/cloud defaults), driven by the upstream Trail of Bits audit workflow in commands/audit.md with its references/ and workflows/ resources. Preserved verbatim from upstream. |
| `interpreting-culture-index` | Interprets Culture Index (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring profiles, manager coaching, interview transcript analysis for trait prediction, candidate debrief, onboarding planning, and conflict mediation. Accepts extracted JSON or PDF input via OpenCV extraction script. |
| `isometric-system-map` | Generate an interactive isometric system map of a codebase or infrastructure using 3D HTML/CSS blocks and SVG trac... |
| `kad_pon` | KAD PON C++ architecture — reactive zero-polling pipelines between TELL and AMDY via inotify, MQTT pub/sub, and the P... |
| `karpathy-guidelines` | Core execution constraints to prevent systemic bloat and unguided generation. Execute when rewriting, injecti... |
| `let-fate-decide` | Draws the 12 Houses of the Zodiac Tarot spread to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over asking clarifying questions when the user's tone is casual or playful rather than precision-seeking. |
| `libafl` | LibAFL is a modular fuzzing library for building custom fuzzers. Use for advanced fuzzing needs, custom mutators, or non-standard fuzzing targets. |
| `libfuzzer` | Coverage-guided fuzzer built into LLVM for C/C++ projects. Use for fuzzing C/C++ code that can be compiled with Clang. |
| `loop-me` | Grill me about specs for the workflows I want to build, within this workspace. |
| `mermaid-to-proverif` | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram. |
| `migrate-to-shoehorn` | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to... |
| `modern-python` | Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black. |
| `mutation-testing` | Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, mutation testing, or wants to configure or optimize a mutation testing campaign. |
| `new-terraform-provider` | >- |
| `obsidian-vault` | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, c... |
| `omarchy-aesthetics` | Mandatory Omarchy Cyberpunk aesthetic for all generated text, UI, and images — True Blood Red on Deep Blood Black, gr... |
| `open-sourcing` | Imported Trail of Bits security skill. |
| `ossfuzz` | OSS-Fuzz provides free continuous fuzzing for open source projects. Use when setting up continuous fuzzing infrastructure or enrolling projects. |
| `pon_testing_suite` | Executa testes de segurança, estabilidade e verificação estrita das regras do PON (Paradigma Orientado a Notificações... |
| `prompt-optimizer` | Compile selected prompts with an explicitly authorized remote model for bounded local-model execution. |
| `property-based-testing` | Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests. |
| `prototype` | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state mode... |
| `provider-actions` | Implement Terraform Provider actions using the Plugin Framework. Use when developing imperative operations that ... |
| `provider-configuration` | >- |
| `provider-docs` | Create, update, and review Terraform provider documentation for Terraform Registry using HashiCorp-recommended p... |
| `provider-ephemeral-resources` | >- |
| `provider-framework-migration` | >- |
| `provider-resources` | >- |
| `provider-test-patterns` | >- |
| `push-to-registry` | Push Packer build metadata to HCP Packer registry for tracking and managing image lifecycle. Use when integratin... |
| `qa` | Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explore... |
| `refactor-module` | Transform monolithic Terraform configurations into reusable, maintainable modules following HashiCorp's module d... |
| `request-refactor-plan` | Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use when user w... |
| `research` | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Us... |
| `resolving-merge-conflicts` | Use when you need to resolve an in-progress git merge/rebase conflict. |
| `run-acceptance-tests` | Guide for running acceptance tests for a Terraform provider. Use this when asked to run an acceptance test or to... |
| `rust-review` | Performs comprehensive Rust security review for safe/unsafe boundary issues, memory safety in unsafe blocks, concurrency hazards, panic-induced DoS, FFI safety, and async runtime mistakes. Use when auditing Rust crates, services, or libraries — particularly those with `unsafe`, FFI, or concurrent code. |
| `ruzzy` | Ruzzy is a coverage-guided Ruby fuzzer by Trail of Bits. Use for fuzzing pure Ruby code and Ruby C extensions. |
| `sarif-parsing` | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output". Handles filtering, deduplication, format conversion, and CI/CD integration of SARIF data. Does NOT run scans — use the Semgrep or CodeQL skills for that. |
| `scaffold-exercises` | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when u... |
| `second-opinion` | Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion. |
| `secure-workflow-guide` | Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas. |
| `semgrep` | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and writes scans.json, and merges the output to SARIF. Supports two scan modes, "run all" for full ruleset coverage and "important only" for security findings at medium-to-high confidence and impact. Uses Semgrep Pro for |
| `semgrep-rule-creator` | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. |
| `semgrep-rule-variant-creator` | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language. |
| `setup-matt-pocock-skills` | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc la... |
| `setup-pre-commit` | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when use... |
| `setup-ts-deep-modules` | Wire dependency-cruiser into a TypeScript repo so each package is a deep module — implementation hidden in subfolders... |
| `sharp-edges` | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration. |
| `skill-improver` | Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly. |
| `slicing-code-context` | Selects bounded, graph-informed source slices with Trailmark and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloading function-, class-, caller-, callee-, call-path-, entrypoint-, or line-focused code tasks to constrained or locally hosted models without exposing the full repository. |
| `solana-vulnerability-scanner` | Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs. |
| `spec-to-code-compliance` | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. Use when comparing an implementation against a whitepaper, protocol spec, or design document. |
| `substrate-vulnerability-scanner` | Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets. |
| `supply-chain-risk-auditor` | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script execution. Use when asked to audit dependencies, assess supply-chain or third-party package risk, or review a dependency tree before an engagement. |
| `tdd` | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refact... |
| `teach` | Teach the user a new skill or concept, within this workspace. |
| `terraform-policy` | "Write, test, or convert Terraform Policy files (.policy.hcl, .policytest.hcl, Sentinel→tfpolicy). Triggers: pol... |
| `terraform-search-import` | Discover existing cloud resources using Terraform Search queries and bulk import them into Terraform management.... |
| `terraform-stacks` | Comprehensive guide for working with HashiCorp Terraform Stacks. Use when creating, modifying, or validating Ter... |
| `terraform-style-guide` | Generate Terraform HCL code following HashiCorp's official style conventions and best practices. Use when writin... |
| `terraform-test` | Comprehensive guide for writing and running Terraform tests. Use when creating test files (.tftest.hcl), writing... |
| `testing-handbook-generator` | Meta-skill that analyzes the Trail of Bits Testing Handbook (appsec.guide) and generates Claude Code skills for security testing tools and techniques. Use when creating new skills based on handbook content. |
| `to-questionnaire` | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| `to-spec` | Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis ... |
| `to-tickets` | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edge... |
| `token-integration-analyzer` | Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations. |
| `ton-vulnerability-scanner` | Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts. |
| `trailmark` | Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, entry point enumeration, proxy/unresolved-call tracking, type/reference queries, structural traversal, graph diffs, audit augmentation, declared cross-language/FFI/external links via `.trailmark/links.toml`, and SQL schema graphs. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, importing SARIF/weAudit/binary findings, linking source graphs across language or RPC boundaries, or building a code graph for audit prioritization. Feature-gate version-specific Trailmark APIs before using them; prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot. |
| `trailmark-finding-triage` | Performs graph-assisted triage of a single security finding, SARIF result, weAudit annotation, suspicious function, or report excerpt using Trailmark reachability, entrypoint paths, taint, privilege-boundary, blast-radius, caller/callee, and neighborhood evidence. Use when deciding whether one candidate issue is reachable, prioritizing a finding before PoC work, preparing evidence for exploit validation, or checking whether a static-analysis result is actionable. |
| `trailmark-review-gate` | Runs a Trailmark structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, removed validation or authorization calls, privilege-boundary drift, blast-radius growth, complexity growth, and newly reachable sensitive sinks. Use when reviewing a PR, branch, remediation commit, or release diff where graph-level security regressions should be checked before merge. |
| `trailmark-structural` | Runs full Trailmark structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack surface, and version-gated Trailmark 0.4+/0.5+ data such as proxy counts, subgraph edges, type/reference summaries, and entrypoint attributes. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots, proxy nodes, type references. |
| `trailmark-summary` | Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview. |
| `trailmark-variant-neighborhood` | Expands one confirmed or suspected vulnerability into a Trailmark graph neighborhood of variant candidates by finding sibling functions, shared callers and callees, common sensitive sinks, common entrypoint paths, interface implementations, override relationships, type/reference neighbors, and structurally similar nodes. Use after one issue is found to seed variant-analysis, semgrep-rule-creator, static-analysis, or manual review with graph-derived candidate locations. |
| `triage` | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write... |
| `ubiquitous-language` | Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing ca... |
| `utfpr-tcc-abnt` | Strict guidelines for creating technical documents, monographs, and papers following UTFPR (Universidade Tecnológica ... |
| `variant-analysis` | Imported Trail of Bits security skill. |
| `vector-forge` | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives. |
| `vulnerability-triage-brocards` | This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is valid", "review a security finding", "dismiss a vulnerability", "should we fix this CVE", "prioritize a vulnerability report", or needs to determine whether an incoming vulnerability report warrants investigation. Applies 7 brocards (rules of thumb) to systematically |
| `wait-what` | Stop. That last message did not land — re-pitch it. |
| `wayfinder` | Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision tickets on your issue ... |
| `windows-builder` | Build Windows images with Packer using WinRM communicator and PowerShell provisioners. Use when creating Windows... |
| `wizard` | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning inf... |
| `writing-beats` | Writing, exploit — assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| `writing-for-agents` | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| `writing-fragments` | Writing, explore — mine raw fragments, no structure yet. |
| `writing-great-skills` | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |
| `writing-lean-proofs` | Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics or specifications in Lean 4, defining new types or definitions in a Lean library, reviewing Lean proofs for readability and maintainability, refactoring long tactic proofs into lemmas, filling in sorry placeholders in a Lean development, setting up CI or linters for a Lean project, diagnosing slow proofs or maxHeartbeats timeouts, or writing custom tactics, macros, or linters. |
| `writing-shape` | Writing, exploit — shape raw material into an article, paragraph by paragraph. |
| `wycheproof` | Wycheproof provides test vectors for validating cryptographic implementations. Use when testing crypto code for known attacks and edge cases. |
| `yara-rule-authoring` | Guides authoring of high-quality YARA-X detection rules for malware identification. Use when writing, reviewing, or optimizing YARA rules. Covers naming conventions, string selection, performance optimization, migration from legacy YARA, and false positive reduction. Triggers on: YARA, YARA-X, malware detection, threat hunting, IOC, signature, crx module, dex module. |
| `zeroize-audit` | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data. |

## How each environment picks these up

All environments share these canonical skills via `scripts/install_skills.sh`
(or `reins skills install`), which links each skill into the location that
environment scans:

| Environment | Skills location it scans |
|---|---|
| Odysseus | `odysseus/data/skills/` |
| Claude Code | `~/.claude/skills/` |
| Antigravity | `.agents/skills/` |
| Codex | `~/.codex/skills/` |
| Odysseus Codex plugin | `odysseus/integrations/codex/skills/` |
| VS Code | integrated terminal -> `reins skills list` |

The installer symlinks (never copies) so there is exactly one editable source:
this directory. Re-run it any time; it is idempotent and PON-compliant.

## Discover from any shell
```bash
reins skills list            # list registered skills
reins skills install         # link them into every environment
reins wiki search "<topic>"  # skills are also ingested into the wiki
```