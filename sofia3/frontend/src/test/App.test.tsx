import { describe, expect, it, vi, beforeEach, afterEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Provider } from "react-redux";
import { store } from "../store";
import App from "../App";

describe("App shell", () => {
  beforeEach(() => {
    globalThis.fetch = vi.fn().mockImplementation((url: string) => {
      if (url === "/api/health") {
        return Promise.resolve({
          ok: true,
          json: async () => ({ status: "SYS_OK", service: "sofia3", version: "3.0.0", degraded: false }),
        });
      }
      if (url === "/api/graph") {
        return Promise.resolve({
          ok: true,
          json: async () => ({ graph: { nodes: [], edges: [] } }),
        });
      }
      return Promise.resolve({ ok: true, json: async () => ({}) });
    }) as unknown as typeof fetch;
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it("renders brand, nav tabs without GRAPH tab, and detail panel", async () => {
    const { container } = render(
      <Provider store={store}>
        <App />
      </Provider>
    );

    expect(screen.getByText(/SOFIA/i)).toBeInTheDocument();
    const navTabs = container.querySelector(".nav-tabs")!;
    expect(navTabs.querySelector("button:nth-child(1)")).toHaveTextContent("UNIFIED GRAPH");
    expect(navTabs.querySelector("button:nth-child(2)")).toHaveTextContent("TASKS");
    expect(navTabs.querySelector("button:nth-child(3)")).toHaveTextContent("WIKI");
    expect(screen.queryByRole("button", { name: "GRAPH" })).not.toBeInTheDocument();
  });

  it("switches active tab when nav buttons are clicked", async () => {
    const { container } = render(
      <Provider store={store}>
        <App />
      </Provider>
    );

    const navTabs = container.querySelector(".nav-tabs")!;
    const unifiedBtn = navTabs.querySelector("button:nth-child(1)")!;
    const tasksBtn = navTabs.querySelector("button:nth-child(2)")!;

    expect(unifiedBtn).toHaveClass("active");
    expect(tasksBtn).not.toHaveClass("active");

    fireEvent.click(tasksBtn);

    expect(tasksBtn).toHaveClass("active");
    expect(unifiedBtn).not.toHaveClass("active");
  });
});


