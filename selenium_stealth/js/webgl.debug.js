function getWebGLInfo() {
  const canvas = document.createElement("canvas");
  const gl =
    canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
  if (!gl) {
    return "WebGL not supported";
  }

  // Add WEBGL_debug_renderer_info extension for unmasked renderer and vendor
  const debugInfo = gl.getExtension("WEBGL_debug_renderer_info");

  const parameters = [
    "VENDOR",
    "RENDERER",
    "SHADING_LANGUAGE_VERSION",
    "VERSION",
    "MAX_TEXTURE_SIZE",
    "MAX_RENDERBUFFER_SIZE",
    "ALPHA_BITS",
    "BLUE_BITS",
    "GREEN_BITS",
    "RED_BITS",
    "STENCIL_BITS",
    "MAX_VIEWPORT_DIMS",
    "ALIASED_LINE_WIDTH_RANGE",
    "ALIASED_POINT_SIZE_RANGE",
    "MAX_TEXTURE_IMAGE_UNITS",
    "MAX_CUBE_MAP_TEXTURE_SIZE",
    "MAX_FRAGMENT_UNIFORM_VECTORS",
    "MAX_VERTEX_ATTRIBS",
    "MAX_VERTEX_UNIFORM_VECTORS",
    "MAX_VERTEX_TEXTURE_IMAGE_UNITS",
    "MAX_VARYING_VECTORS"
  ];

  const webGLInfo = {};

  parameters.forEach((param) => {
    webGLInfo[param] = gl.getParameter(gl[param]);
  });

  // Add unmasked renderer and vendor information if available
  if (debugInfo) {
    webGLInfo.UNMASKED_VENDOR_WEBGL = gl.getParameter(
      debugInfo.UNMASKED_VENDOR_WEBGL
    );
    webGLInfo.UNMASKED_RENDERER_WEBGL = gl.getParameter(
      debugInfo.UNMASKED_RENDERER_WEBGL
    );
  }

  webGLInfo['navigator.vendor'] = navigator.vendor;

  return webGLInfo;
}

function runInAllFrames() {
  // Helper function to get WebGL info in a single window (frame/iframe)
  function getWebGLInfo() {
    const canvas = document.createElement("canvas");
    const gl =
      canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
    if (!gl) {
      return "WebGL not supported";
    }

    // Add WEBGL_debug_renderer_info extension for unmasked renderer and vendor
    const debugInfo = gl.getExtension("WEBGL_debug_renderer_info");

    const parameters = [
      "VENDOR",
      "RENDERER",
      "SHADING_LANGUAGE_VERSION",
      "VERSION",
      "MAX_TEXTURE_SIZE",
      "MAX_RENDERBUFFER_SIZE",
      "ALPHA_BITS",
      "BLUE_BITS",
      "GREEN_BITS",
      "RED_BITS",
      "STENCIL_BITS",
      "MAX_VIEWPORT_DIMS",
      "ALIASED_LINE_WIDTH_RANGE",
      "ALIASED_POINT_SIZE_RANGE",
      "MAX_TEXTURE_IMAGE_UNITS",
      "MAX_CUBE_MAP_TEXTURE_SIZE",
      "MAX_FRAGMENT_UNIFORM_VECTORS",
      "MAX_VERTEX_ATTRIBS",
      "MAX_VERTEX_UNIFORM_VECTORS",
      "MAX_VERTEX_TEXTURE_IMAGE_UNITS",
      "MAX_VARYING_VECTORS"
    ];

    const webGLInfo = {};

    parameters.forEach((param) => {
      webGLInfo[param] = gl.getParameter(gl[param]);
    });

    // Add unmasked renderer and vendor information if available
    if (debugInfo) {
      webGLInfo.UNMASKED_VENDOR_WEBGL = gl.getParameter(
        debugInfo.UNMASKED_VENDOR_WEBGL
      );
      webGLInfo.UNMASKED_RENDERER_WEBGL = gl.getParameter(
        debugInfo.UNMASKED_RENDERER_WEBGL
      );
    }

    webGLInfo['navigator.vendor'] = navigator.vendor;

    return webGLInfo;
  }

  // Function to collect WebGL info from a single frame
  function collectWebGLInfoFromFrame(win) {
    try {
      return win.JSON.stringify(getWebGLInfo());
    } catch (error) {
      return `Error in frame: ${error.message}`;
    }
  }

  // Collect results from main window
  const results = [];
  results.push({ frame: 'main', info: collectWebGLInfoFromFrame(window) });

  // Collect results from all frames
  for (let i = 0; i < window.frames.length; i++) {
    try {
      const frameWindow = window.frames[i];
      const frameResult = collectWebGLInfoFromFrame(frameWindow);
      results.push({ frame: `frame-${i}`, info: frameResult });
    } catch (error) {
      results.push({ frame: `frame-${i}`, info: `Error: ${error.message}` });
    }
  }

  return results;
}

const main_result = {
  frames: runInAllFrames(),
  main_window: getWebGLInfo()
}
return JSON.stringify(main_result);