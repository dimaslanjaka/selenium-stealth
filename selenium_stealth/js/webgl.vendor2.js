/* eslint-disable */
// https://github.com/berstend/puppeteer-extra/blob/c44c8bb0224c6bba2554017bfb9d7a1d0119f92f/packages/puppeteer-extra-plugin-stealth/evasions/webgl.vendor/index.js

(webglProps = {}) => {
  if (typeof webglProps == 'string') {
    webglProps = JSON.parse(webglProps);
  }
  const getParameterProxyHandler = {
    apply: function (target, ctx, args) {
      const param = (args || [])[0];

      // UNMASKED_VENDOR_WEBGL
      if (param === 37445) {
        return webglProps.unmaskedVendor || 'Intel Inc.'; // default in headless: Google Inc.
      }
      // UNMASKED_RENDERER_WEBGL
      if (param === 37446) {
        return webglProps.unmaskedRenderer || 'Intel Iris OpenGL Engine'; // default in headless: Google SwiftShader
      }
      // VERSION
      if (param === 7938) {
        return webglProps.version || 'WebGL 1.0 (OpenGL ES 2.0 Chromium)'; // default firefox "WebGL 1.0"
      }
      // RENDERER
      if (param === 7937) {
        return webglProps.renderer || 'WebKit WebGL';
      }
      // VENDOR
      if (param === 7936) {
        return webglProps.vendor || 'WebKit'; // default firefox "Mozilla"
      }
      // SHADING_LANGUAGE_VERSION
      if (param === 35724) {
        return webglProps.shadingLanguage || 'WebGL GLSL ES 1.0';
      }

      // Additional WebGL properties from webglProps
      if (param === 3379) { // MAX_TEXTURE_SIZE
        return webglProps.maxTextureSize || 16384;
      }
      if (param === 34024) { // MAX_RENDERBUFFER_SIZE
        return webglProps.maxRenderBufferSize || 16384;
      }
      if (param === 3413) { // ALPHA_BITS
        return webglProps.alphaBits || 8;
      }
      if (param === 3412) { // BLUE_BITS
        return webglProps.blueBits || 8;
      }
      if (param === 3411) { // GREEN_BITS
        return webglProps.greenBits || 8;
      }
      if (param === 3410) { // RED_BITS
        return webglProps.redBits || 8;
      }
      if (param === 3415) { // STENCIL_BITS
        return webglProps.stencilBits || 8;
      }
      if (param === 3386) { // MAX_VIEWPORT_DIMS
        return webglProps.maxViewportDims || [32767, 32767];
      }
      if (param === 33902) { // ALIASED_LINE_WIDTH_RANGE
        return webglProps.aliasedLineWidthRange || [1, 1];
      }
      if (param === 33901) { // ALIASED_POINT_SIZE_RANGE
        return webglProps.aliasedPointSizeRange || [1, 1024];
      }
      if (param === 35660) { // MAX_TEXTURE_IMAGE_UNITS
        return webglProps.maxTextureImageUnits || 16;
      }
      if (param === 34076) { // MAX_CUBE_MAP_TEXTURE_SIZE
        return webglProps.maxCubeMapTextureSize || 16384;
      }
      if (param === 35659) { // MAX_FRAGMENT_UNIFORM_VECTORS
        return webglProps.maxFragmentUniformVectors || 1024;
      }
      if (param === 34921) { // MAX_VERTEX_ATTRIBS
        return webglProps.maxVertexAttribs || 16;
      }
      if (param === 35658) { // MAX_VERTEX_UNIFORM_VECTORS
        return webglProps.maxVertexUniformVectors || 4096;
      }
      if (param === 35657) { // MAX_VERTEX_TEXTURE_IMAGE_UNITS
        return webglProps.maxVertexTextureImageUnits || 16;
      }
      if (param === 35659) { // MAX_VARYING_VECTORS
        return webglProps.maxVaryingVectors || 30;
      }

      return utils.cache.Reflect.apply(target, ctx, args);
    }
  };

  // Proxy handling for WebGLRenderingContext and WebGL2RenderingContext
  const addProxy = (obj, propName) => {
    utils.replaceWithProxy(obj, propName, getParameterProxyHandler);
  };

  addProxy(WebGLRenderingContext.prototype, 'getParameter');
  addProxy(WebGL2RenderingContext.prototype, 'getParameter');
}
