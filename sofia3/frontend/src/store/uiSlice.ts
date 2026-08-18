import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import type { Health, SelectedNode } from "../api";

export type NavTab = "unified" | "tasks" | "wiki" | "hardware" | "routing" | "pon";

export interface UiState {
  selected: SelectedNode | null;
  nav: NavTab;
  health: Health | null;
  visibleWidgets: Record<string, boolean>;
}

const initialState: UiState = {
  selected: null,
  nav: "unified",
  health: null,
  visibleWidgets: {
    graph: true,
    detail: true,
    tasks: true,
    hardware: true,
    routing: true,
    pon: true,
    coord: true,
  },
};

export const uiSlice = createSlice({
  name: "ui",
  initialState,
  reducers: {
    setSelected: (state, action: PayloadAction<SelectedNode | null>) => {
      state.selected = action.payload;
    },
    setNav: (state, action: PayloadAction<NavTab>) => {
      state.nav = action.payload;
    },
    setHealth: (state, action: PayloadAction<Health | null>) => {
      state.health = action.payload;
    },
    toggleWidget: (state, action: PayloadAction<string>) => {
      state.visibleWidgets[action.payload] = !state.visibleWidgets[action.payload];
    },
    setAllWidgets: (state, action: PayloadAction<Record<string, boolean>>) => {
      state.visibleWidgets = action.payload;
    },
  },
});

export const { setSelected, setNav, setHealth, toggleWidget, setAllWidgets } = uiSlice.actions;
export default uiSlice.reducer;
