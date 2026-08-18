import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import type { TaskRecord, TrailSnapshot } from "../api";

export interface TrailState {
  tasks: TaskRecord[];
  summary: Record<string, number>;
  total: number;
  connected: boolean;
  lastUpdated: number | null;
}

const initialState: TrailState = {
  tasks: [],
  summary: {},
  total: 0,
  connected: false,
  lastUpdated: null,
};

export const trailSlice = createSlice({
  name: "trail",
  initialState,
  reducers: {
    setConnected: (state, action: PayloadAction<boolean>) => {
      state.connected = action.payload;
    },
    updateTrailSnapshot: (state, action: PayloadAction<TrailSnapshot>) => {
      if (action.payload.tasks) {
        state.tasks = action.payload.tasks;
      }
      if (action.payload.summary) {
        state.summary = action.payload.summary;
      }
      if (action.payload.total !== undefined) {
        state.total = action.payload.total;
      }
      state.lastUpdated = Date.now();
    },
  },
});

export const { setConnected, updateTrailSnapshot } = trailSlice.actions;
export default trailSlice.reducer;
