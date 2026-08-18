import "@testing-library/jest-dom/vitest";

// Mock ResizeObserver for React Flow and DOM components in jsdom
globalThis.ResizeObserver = class ResizeObserver {
  observe() {}
  unobserve() {}
  disconnect() {}
};

// Mock DOMMatrixReadOnly for React Flow
if (typeof DOMMatrixReadOnly === "undefined") {
  (globalThis as unknown as { DOMMatrixReadOnly: unknown }).DOMMatrixReadOnly = class DOMMatrixReadOnly {
    m22 = 1;
    m11 = 1;
  };
}

if (typeof WebGL2RenderingContext === "undefined") {
  (globalThis as unknown as { WebGL2RenderingContext: unknown }).WebGL2RenderingContext = class WebGL2RenderingContext {};
}
if (typeof WebGLRenderingContext === "undefined") {
  (globalThis as unknown as { WebGLRenderingContext: unknown }).WebGLRenderingContext = class WebGLRenderingContext {};
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
(HTMLCanvasElement.prototype as any).getContext = function () {
  const glMock = new Proxy(

    {
      canvas: this,
      FRAMEBUFFER_COMPLETE: 36053,
      getExtension: () => null,
      getParameter: () => 0,
      createProgram: () => ({}),
      createShader: () => ({}),
      getShaderParameter: () => true,
      getProgramParameter: () => true,
      createBuffer: () => ({}),
      createFramebuffer: () => ({}),
      createTexture: () => ({}),
      createRenderbuffer: () => ({}),
      checkFramebufferStatus: () => 36053,
    },
    {
      get(target, prop) {
        if (prop in target) {
          return (target as Record<string | symbol, unknown>)[prop];
        }
        return () => {};
      },
    }
  );
  return glMock as unknown as RenderingContext;
};



