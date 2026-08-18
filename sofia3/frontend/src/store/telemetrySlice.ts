import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import type {
  ClusterProfile,
  ComboItem,
  CoordinatorStatus,
  ModelCategoryItem,
  PonHealth,
  TelemetrySnapshot,
  TokenBudgetReport,
} from "../api";

export interface TelemetryState {
  hardware: ClusterProfile | null;
  hardwareGaps: Record<string, unknown> | null;
  combos: ComboItem[];
  categories: Record<string, ModelCategoryItem>;
  tokens: TokenBudgetReport | null;
  coord: CoordinatorStatus | null;
  agentBudgets: Record<string, unknown> | null;
  training: Record<string, unknown> | null;
  pon: PonHealth | null;
  lastUpdated: number | null;
}

const initialState: TelemetryState = {
  hardware: null,
  hardwareGaps: null,
  combos: [],
  categories: {},
  tokens: null,
  coord: null,
  agentBudgets: null,
  training: null,
  pon: null,
  lastUpdated: null,
};

export const telemetrySlice = createSlice({
  name: "telemetry",
  initialState,
  reducers: {
    updateTelemetry: (state, action: PayloadAction<TelemetrySnapshot | undefined>) => {
      if (!action.payload) return;
      const p = action.payload;
      if (p.hardware) state.hardware = p.hardware;
      if (p.hardware_gaps) state.hardwareGaps = p.hardware_gaps;
      if (p.combos) state.combos = p.combos;
      if (p.categories) state.categories = p.categories;
      if (p.tokens) state.tokens = p.tokens;
      if (p.coord) state.coord = p.coord;
      if (p.agent_budgets) state.agentBudgets = p.agent_budgets;
      if (p.training) state.training = p.training;
      if (p.pon) state.pon = p.pon;
      state.lastUpdated = Date.now();
    },
  },
});

export const { updateTelemetry } = telemetrySlice.actions;
export default telemetrySlice.reducer;
