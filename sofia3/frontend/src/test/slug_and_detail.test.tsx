import { describe, expect, it, vi, beforeEach, afterEach } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { DetailPanel } from "../components/DetailPanel";
import type { SelectedNode } from "../api";

describe("DetailPanel slug and ID handling", () => {
  beforeEach(() => {
    vi.restoreAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it("renders empty placeholder when no node is selected", () => {
    render(<DetailPanel selected={null} />);
    expect(screen.getByText(/DETAIL \/\/ NO SELECTION/i)).toBeInTheDocument();
  });

  it("extracts page slug without double decoding and encodes in fetch URL", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        page: {
          slug: "knowledge/guide with space",
          title: "Guide Title",
          content: "# Markdown Content",
          category: "guide",
          owner: "agent",
        },
      }),
    });
    globalThis.fetch = fetchMock as unknown as typeof fetch;

    const selected: SelectedNode = {
      id: "page:knowledge/guide with space",
      type: "Page",
      content: "Guide Title",
    };

    render(<DetailPanel selected={selected} />);

    expect(fetchMock).toHaveBeenCalledWith(
      "/api/wiki/page/knowledge%2Fguide%20with%20space"
    );

    await waitFor(() => {
      expect(screen.getByText("# Markdown Content")).toBeInTheDocument();
    });
  });

  it("extracts memory uid and encodes in fetch URL", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        memory: {
          uid: "mem-uuid-1234",
          text: "Important memory text",
          category: "fact",
          owner: "odysseus",
        },
      }),
    });
    globalThis.fetch = fetchMock as unknown as typeof fetch;

    const selected: SelectedNode = {
      id: "memory:mem-uuid-1234",
      type: "Memory",
      content: "Memory snippet",
    };

    render(<DetailPanel selected={selected} />);

    expect(fetchMock).toHaveBeenCalledWith(
      "/api/wiki/memory/mem-uuid-1234"
    );

    await waitFor(() => {
      expect(screen.getByText("Important memory text")).toBeInTheDocument();
    });
  });

  it("extracts task id and renders immediately from props then hydrates", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        task: {
          task_id: "task-abc-123",
          status: "success",
          target_node: "amdy",
          timestamp: 1700000000,
          prompt: "Execute deployment",
          attempts: 1,
        },
      }),
    });
    globalThis.fetch = fetchMock as unknown as typeof fetch;

    const selected: SelectedNode = {
      id: "task:task-abc-123",
      type: "Task",
      content: "Execute deployment",
      properties: {
        status: "running",
        target_node: "amdy",
      },
    };

    render(<DetailPanel selected={selected} />);

    expect(fetchMock).toHaveBeenCalledWith("/api/tasks/task-abc-123");

    await waitFor(() => {
      expect(screen.getByText("Execute deployment")).toBeInTheDocument();
    });
  });

  it("renders property grid for hub nodes (Agent/Category/Owner)", () => {
    const selected: SelectedNode = {
      id: "agent:amdy",
      type: "Agent",
      content: "amdy",
      properties: {
        role: "Executor",
        node: "amdy",
      },
    };

    render(<DetailPanel selected={selected} />);

    expect(screen.getByText("AGENT // amdy")).toBeInTheDocument();
    expect(screen.getByText("role")).toBeInTheDocument();
    expect(screen.getByText("Executor")).toBeInTheDocument();
  });
});
