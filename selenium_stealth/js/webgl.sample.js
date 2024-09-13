// Override WebGL properties directly
const originalGetParameter = WebGLRenderingContext.prototype.getParameter;
WebGLRenderingContext.prototype.getParameter = function (parameter) {
  switch (parameter) {
    case this.UNMASKED_VENDOR_WEBGL:
      return "Google Inc. (Intel)";
    case this.UNMASKED_RENDERER_WEBGL:
      return "ANGLE (Intel, Intel(R) UHD Graphics (0x00009BA4) Direct3D11 vs_5_0 ps_5_0, D3D11)";
    case this.VENDOR:
      return "WebKit";
    case this.RENDERER:
      return "WebKit WebGL";
    case this.SHADING_LANGUAGE_VERSION:
      return "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)";
    case this.VERSION:
      return "WebGL 1.0 (OpenGL ES 2.0 Chromium)";
    case this.MAX_TEXTURE_SIZE:
      return 16384;
    case this.MAX_RENDERBUFFER_SIZE:
      return 16384;
    case this.ALPHA_BITS:
      return 8;
    case this.BLUE_BITS:
      return 8;
    case this.GREEN_BITS:
      return 8;
    case this.RED_BITS:
      return 8;
    case this.STENCIL_BITS:
      return 8;
    case this.MAX_VIEWPORT_DIMS:
      return [32767, 32767];
    case this.ALIASED_LINE_WIDTH_RANGE:
      return [1, 1];
    case this.ALIASED_POINT_SIZE_RANGE:
      return [1, 1024];
    case this.MAX_TEXTURE_IMAGE_UNITS:
      return 16;
    case this.MAX_CUBE_MAP_TEXTURE_SIZE:
      return 16384;
    case this.MAX_FRAGMENT_UNIFORM_VECTORS:
      return 1024;
    case this.MAX_VERTEX_ATTRIBS:
      return 16;
    case this.MAX_VERTEX_UNIFORM_VECTORS:
      return 4096;
    case this.MAX_VERTEX_TEXTURE_IMAGE_UNITS:
      return 16;
    case this.MAX_VARYING_VECTORS:
      return 30;
    default:
      return originalGetParameter.call(this, parameter);
  }
};

// Spoofing WebGL context attributes
const originalGetContextAttributes = WebGLRenderingContext.prototype.getContextAttributes;
WebGLRenderingContext.prototype.getContextAttributes = function () {
  const attributes = originalGetContextAttributes.call(this);
  return {
    ...attributes,
    alpha: true,
    antialias: true,
    depth: true,
    desynchronized: false,
    failIfMajorPerformanceCaveat: false,
    powerPreference: "default",
    premultipliedAlpha: true,
    preserveDrawingBuffer: false,
    stencil: false,
    xrCompatible: false
  };
};