import { configureStore } from "@reduxjs/toolkit";
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import trailReducer, { setConnected, updateTrailSnapshot } from "./trailSlice";
import telemetryReducer, { updateTelemetry } from "./telemetrySlice";
import uiReducer, { setHealth } from "./uiSlice";
import type { TrailSnapshot } from "../api";

export const store = configureStore({
  reducer: {
    trail: trailReducer,
    telemetry: telemetryReducer,
    ui: uiReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

/**
 * Global reactive hook that connects the Redux store to the Sofia³ WebSocket bridge.
 * Zero polling — strictly event-driven.
 */
export function useLiveBridge(): { connected: boolean } {
  const dispatch = useAppDispatch();
  const connected = useAppSelector((state) => state.trail.connected);

  useEffect(() => {
    // Initial health check
    fetch("/api/health")
      .then((r) => r.json())
      .then((data) => dispatch(setHealth(data)))
      .catch(() => dispatch(setHealth(null)));

    let ws: WebSocket | null = null;
    let retryTimer: number | undefined;
    let disposed = false;

    const connect = () => {
      if (disposed) return;
      const proto = location.protocol === "https:" ? "wss" : "ws";
      ws = new WebSocket(`${proto}://${location.host}/ws`);

      ws.onopen = () => {
        if (!disposed) dispatch(setConnected(true));
      };

      ws.onmessage = (ev) => {
        try {
          const data = JSON.parse(ev.data) as TrailSnapshot;
          if (data.kind === "trail") {
            dispatch(updateTrailSnapshot(data));
            if (data.telemetry) {
              dispatch(updateTelemetry(data.telemetry));
            }
          }
        } catch {
          /* keepalive or malformed — ignore */
        }
      };

      ws.onclose = () => {
        if (!disposed) {
          dispatch(setConnected(false));
          retryTimer = window.setTimeout(connect, 3000);
        }
      };
    };

    connect();

    return () => {
      disposed = true;
      if (retryTimer) window.clearTimeout(retryTimer);
      ws?.close();
    };
  }, [dispatch]);

  return { connected };
}
