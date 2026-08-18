import { describe, expect, it, vi, beforeEach, afterEach } from "vitest";
import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import { GraphView } from "../views/Graph";
import type { ApiGraphResponse } from "../api";

const mockGraphData: ApiGraphResponse = {
  graph: {
    nodes: [
      { id: "task:1", type: "Task", content: "Run tests" },
      { id: "agent:amdy", type: "Agent", content: "amdy" },
      { id: "owner:root", type: "Owner", content: "root" },
      { id: "page:doc", type: "Page", content: "Docs" },
      { id: "memory:mem1", type: "Memory", content: "Mem 1" },
      { id: "category:general", type: "Category", content: "general" },
    ],
    edges: [
      { source: "task:1", target: "agent:amdy", type: "assigned" },
      { source: "page:doc", target: "category:general", type: "in_category" },
    ],
  },
  stats: {
    node_count: 6,
    edge_count: 2,
    node_types: { Task: 1, Agent: 1, Owner: 1, Page: 1, Memory: 1, Category: 1 },
  },
};

describe("GraphView navigation and filtering", () => {
  beforeEach(() => {
    globalThis.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => mockGraphData,
    }) as unknown as typeof fetch;
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it("renders unified graph with all node types and counts", async () => {
    render(<GraphView trail={null} onSelect={vi.fn()} nav="unified" />);

    await waitFor(() => {
      expect(screen.getByText(/UNIFIED GRAPH — 6 VISIBLE/i)).toBeInTheDocument();
    });

    expect(screen.getByText(/Task \(1\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Page \(1\)/i)).toBeInTheDocument();
  });

  it("scopes visible nodes to Tasks family when nav is tasks", async () => {
    render(<GraphView trail={null} onSelect={vi.fn()} nav="tasks" />);

    await waitFor(() => {
      // Tasks nav allows Task, Agent, Owner (3 visible)
      expect(screen.getByText(/UNIFIED GRAPH — 3 VISIBLE/i)).toBeInTheDocument();
    });

    expect(screen.getByText(/Task \(1\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Agent \(1\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Owner \(1\)/i)).toBeInTheDocument();
    expect(screen.queryByText(/Page \(/i)).not.toBeInTheDocument();
  });

  it("scopes visible nodes to Wiki family when nav is wiki", async () => {
    render(<GraphView trail={null} onSelect={vi.fn()} nav="wiki" />);

    await waitFor(() => {
      // Wiki nav allows Page, Memory, Category, Owner, Session (4 visible: Page, Memory, Category, Owner)
      expect(screen.getByText(/UNIFIED GRAPH — 4 VISIBLE/i)).toBeInTheDocument();
    });

    expect(screen.getByText(/Page \(1\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Memory \(1\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Category \(1\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Owner \(1\)/i)).toBeInTheDocument();
    expect(screen.queryByText(/Task \(/i)).not.toBeInTheDocument();
  });

  it("resets active filter to all when nav prop changes", async () => {
    const { rerender } = render(<GraphView trail={null} onSelect={vi.fn()} nav="tasks" />);

    await waitFor(() => {
      expect(screen.getByText(/UNIFIED GRAPH — 3 VISIBLE/i)).toBeInTheDocument();
    });

    // Click filter button 'Task'
    const taskBtn = screen.getByRole("button", { name: /Task \(1\)/i });
    fireEvent.click(taskBtn);
    expect(taskBtn).toHaveClass("active");

    // Switch nav to 'wiki'
    rerender(<GraphView trail={null} onSelect={vi.fn()} nav="wiki" />);

    await waitFor(() => {
      // Filter should have reset to 'all'
      const allBtn = screen.getByRole("button", { name: /all \(4\)/i });
      expect(allBtn).toHaveClass("active");
    });
  });

  it("shows error banner when graph bridge returns error response", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue({
      ok: false,
      status: 500,
    }) as unknown as typeof fetch;

    render(<GraphView trail={null} onSelect={vi.fn()} nav="unified" />);

    await waitFor(() => {
      expect(screen.getByText(/GRAPH DEGRADED:/i)).toBeInTheDocument();
    });
  });
});
