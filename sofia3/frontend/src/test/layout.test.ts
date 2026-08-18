import { describe, expect, it } from "vitest";
import { computeLayout } from "../layout";
import type { GraphData } from "../api";

describe("layout engine (d3-force)", () => {
  it("computes reproducible coordinates for empty graph", () => {
    const res = computeLayout({ nodes: [], edges: [] });
    expect(res.positions).toEqual({});
    expect(res.width).toBe(1600);
    expect(res.height).toBe(1000);
  });

  it("assigns positions to all nodes", () => {
    const data: GraphData = {
      nodes: [
        { id: "task:1", type: "Task", content: "Task 1" },
        { id: "agent:amdy", type: "Agent", content: "amdy" },
        { id: "page:home", type: "Page", content: "Home" },
      ],
      edges: [
        { source: "task:1", target: "agent:amdy", type: "assigned_to" },
      ],
    };

    const res = computeLayout(data, 800, 600);
    expect(Object.keys(res.positions)).toHaveLength(3);
    expect(res.positions["task:1"]).toBeDefined();
    expect(typeof res.positions["task:1"].x).toBe("number");
    expect(typeof res.positions["task:1"].y).toBe("number");
    expect(res.positions["agent:amdy"]).toBeDefined();
    expect(res.positions["page:home"]).toBeDefined();
  });

  it("is deterministic given identical input", () => {
    const data: GraphData = {
      nodes: [
        { id: "A", type: "Node" },
        { id: "B", type: "Node" },
        { id: "C", type: "Node" },
      ],
      edges: [
        { source: "A", target: "B", type: "link" },
        { source: "B", target: "C", type: "link" },
      ],
    };

    const run1 = computeLayout(data);
    const run2 = computeLayout(data);

    expect(run1.positions["A"].x).toBeCloseTo(run2.positions["A"].x, 4);
    expect(run1.positions["A"].y).toBeCloseTo(run2.positions["A"].y, 4);
    expect(run1.positions["B"].x).toBeCloseTo(run2.positions["B"].x, 4);
    expect(run1.positions["C"].y).toBeCloseTo(run2.positions["C"].y, 4);
  });
});
