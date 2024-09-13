(function () {
  const webglProps = {
    unmaskedVendor: "Google Inc. (Intel)",
    unmaskedRenderer: "ANGLE (Intel, Intel(R) UHD Graphics (0x00009BA4) Direct3D11 vs_5_0 ps_5_0, D3D11)",
    vendor: "WebKit",
    renderer: "WebKit WebGL",
    shadingLanguage: "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
    version: "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
    maxAnisotropy: "16",
    shadingLanguage2: "WebGL GLSL ES 3.00 (OpenGL ES GLSL ES 3.0 Chromium)",
    version2: "WebGL 2.0 (OpenGL ES 3.0 Chromium)",
    aliasedLineWidthRange: [1, 1],
    aliasedPointSizeRange: [1, 1024],
    alphaBits: "8",
    blueBits: "8",
    depthBits: "24",
    greenBits: "8",
    maxCombinedTextureImageUnits: "32",
    maxCubeMapTextureSize: "16384",
    maxFragmentUniformVectors: "1024",
    maxRenderBufferSize: "16384",
    maxTextureImageUnits: "16",
    maxTextureSize: "16384",
    maxVaryingVectors: "30",
    maxVertexAttribs: "16",
    maxVertexTextureImageUnits: "16",
    maxVertexUniformVectors: "4096",
    maxViewportDims: [32767, 32767],
    redBits: "8",
    stencilBits: "8",
    subpixelBits: "4",
    sampleBuffers: "1",
    samples: "4",
    stencilBackValueMask: "2147483647",
    stencilBackWritemask: "2147483647",
    stencilValueMask: "2147483647",
    stencilWritemask: "2147483647",
    maxColorAttachmentsWebgl: "8",
    maxDrawBuffersWebgl: "8",
    webglContextAttributesDefaults: {
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
    }
  };

  // Override WebGL properties
  const originalGetParameter = WebGLRenderingContext.prototype.getParameter;
  WebGLRenderingContext.prototype.getParameter = function (parameter) {
    switch (parameter) {
      case this.UNMASKED_VENDOR_WEBGL:
        return webglProps.unmaskedVendor;
      case this.UNMASKED_RENDERER_WEBGL:
        return webglProps.unmaskedRenderer;
      case this.VENDOR:
        return webglProps.vendor;
      case this.RENDERER:
        return webglProps.renderer;
      case this.SHADING_LANGUAGE_VERSION:
        return webglProps.shadingLanguage;
      case this.VERSION:
        return webglProps.version;
      case this.MAX_TEXTURE_SIZE:
        return parseInt(webglProps.maxTextureSize);
      case this.MAX_RENDERBUFFER_SIZE:
        return parseInt(webglProps.maxRenderBufferSize);
      case this.ALPHA_BITS:
        return parseInt(webglProps.alphaBits);
      case this.BLUE_BITS:
        return parseInt(webglProps.blueBits);
      case this.GREEN_BITS:
        return parseInt(webglProps.greenBits);
      case this.RED_BITS:
        return parseInt(webglProps.redBits);
      case this.STENCIL_BITS:
        return parseInt(webglProps.stencilBits);
      case this.MAX_VIEWPORT_DIMS:
        return webglProps.maxViewportDims;
      case this.ALIASED_LINE_WIDTH_RANGE:
        return webglProps.aliasedLineWidthRange;
      case this.ALIASED_POINT_SIZE_RANGE:
        return webglProps.aliasedPointSizeRange;
      case this.MAX_TEXTURE_IMAGE_UNITS:
        return parseInt(webglProps.maxTextureImageUnits);
      case this.MAX_CUBE_MAP_TEXTURE_SIZE:
        return parseInt(webglProps.maxCubeMapTextureSize);
      case this.MAX_FRAGMENT_UNIFORM_VECTORS:
        return parseInt(webglProps.maxFragmentUniformVectors);
      case this.MAX_VERTEX_ATTRIBS:
        return parseInt(webglProps.maxVertexAttribs);
      case this.MAX_VERTEX_UNIFORM_VECTORS:
        return parseInt(webglProps.maxVertexUniformVectors);
      case this.MAX_VERTEX_TEXTURE_IMAGE_UNITS:
        return parseInt(webglProps.maxVertexTextureImageUnits);
      case this.MAX_VARYING_VECTORS:
        return parseInt(webglProps.maxVaryingVectors);
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
      ...webglProps.webglContextAttributesDefaults
    };
  };
})();
